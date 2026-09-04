#!/usr/bin/env python3
"""从 UI 组件市场详情页抓出组件源码（selector-UI-patch 技能的执行器）。

用法：
    python3 extract.py "<详情页 URL>" [-o Component.tsx] [--proxy http://127.0.0.1:10808] [--pick N]

退出码：
    0  拿到真实源码
    1  抓到内容但自检未全过（已存盘，供人工确认）
    2  页面无代码块 / --pick 越界
    3  只拿到「用法示例薄壳」，组件实现源码未下发 —— 必须换数据通道，重试无用

注意：sys.exit("消息") 在 Python 里退出码恒为 1，要区分码必须 print(stderr) + sys.exit(N)
"""
import argparse
import html
import re
import sys
import urllib.request

UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/131.0 Safari/537.36")
strip = lambda s: re.sub(r"<[^>]+>", "", s)          # shiki 把每个 token 包进 <span>


def slug_of(url):
    """从详情页 URL 取组件 slug，用于识别「导入自己」的薄壳 demo。"""
    m = re.search(r"/components/([^/?#]+)", url)
    return m.group(1) if m else ""


def classify(code, slug):
    """判别抓到的是真实源码，还是只有用法示例。

    21st.dev 上大量组件页的 <pre> 只有 5~30 行的 demo 薄壳：
        import X from "@/components/ui/x"; export default function Demo(){ return <X/> }
    组件实现（const/function X）压根不在页面里 —— 这是信息不在场，任何解析技巧都取不到。
    """
    n = len(code.splitlines())
    imports_self = bool(slug) and bool(
        re.search(r'from\s+["\']@/components/ui/' + re.escape(slug) + r'["\']', code))
    if n <= 30 and imports_self:
        return 3, f"仅 {n} 行的用法示例（import 本组件后直接 return），实现源码未下发"
    if n < 12 and re.search(r"return\s*\(?\s*<\w+\s*/?>", code):
        return 3, f"仅 {n} 行的用法示例，实现源码未下发"
    ok = [code.lstrip().startswith(("'use client'", '"use client"', "import")),
          "export default" in code,
          80 <= n <= 400]
    return (0 if sum(ok) == 3 else 1), f"{n} 行 | 自检 {sum(ok)}/3 {ok}"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("url", help="组件详情页 URL")
    ap.add_argument("-o", "--out", default="Component.tsx")
    ap.add_argument("--proxy", help="如 http://127.0.0.1:10808")
    ap.add_argument("--pick", type=int, default=1, help="取第 N 长的代码块（默认 1）")
    a = ap.parse_args()

    if a.proxy:
        urllib.request.install_opener(urllib.request.build_opener(
            urllib.request.ProxyHandler({"http": a.proxy, "https": a.proxy})))

    h = urllib.request.urlopen(
        urllib.request.Request(a.url, headers={"User-Agent": UA}), timeout=45
    ).read().decode("utf-8", "replace")

    pres = re.findall(r"<pre[^>]*>(.*?)</pre>", h, re.S)
    if not pres:
        print(f"无 <pre>（页面 {len(h)}B, shiki={h.count('shiki')}）"
              f"→ 客户端渲染，源码不在 HTML 里，需走退路", file=sys.stderr)
        sys.exit(2)

    blocks = sorted(pres, key=lambda b: len(strip(b)), reverse=True)
    if not 1 <= a.pick <= len(blocks):
        print(f"只有 {len(blocks)} 个代码块，--pick {a.pick} 越界", file=sys.stderr)
        sys.exit(2)

    code = html.unescape(strip(blocks[a.pick - 1]))   # 实体 &lt; &quot; &#x27; 必须反转义
    rc, msg = classify(code, slug_of(a.url))
    print(f"{len(h)}B | <pre>×{len(pres)} | {msg} → {a.out}")
    open(a.out, "w").write(code)

    if rc == 3:
        print("\n[退出码 3] 页面只有用法示例，组件实现源码未下发到浏览器。", file=sys.stderr)
        print("  这是服务端访问控制（信息不在场），改 UA / 换解析方式 / 重试都无效。",
              file=sys.stderr)
        # 组件页的 Source 字段带 utm_source=21st.dev，这是唯一可靠锚点。
        # 别用宽松的 github.com 匹配 —— 会抓到 CSS reset 注释里的 gecko-dev 之类噪音。
        srcs = sorted({html.unescape(s.replace("\\", "")) for s in
                       re.findall(r'https?://[^"\\ ]+utm_source=21st\.dev[^"\\ ]*', h)})
        if srcs:
            print("  组件页标注的 Source（优先去这些开源站取）:", file=sys.stderr)
            for s in srcs[:4]:
                print(f"    {s}", file=sys.stderr)
        else:
            print("  该组件页未标注 Source 开源站。", file=sys.stderr)
        print("  下一步：拿上面的 Source 走 scripts/registry.py（开源上游，免费且完整）；"
              "无 Source 则 WebSearch \"<组件名> github\"。详见 SKILL.md。", file=sys.stderr)
        sys.exit(3)

    if rc == 1:
        print("\n自检未全过（可能抓到了 install 命令块或过短片段）。各块预览，改 --pick N 重选：")
        for i, b in enumerate(blocks[:3], 1):
            first = html.unescape(strip(b)).strip().splitlines()
            print(f"  --pick {i}  {len(first):4d} 行  {first[0][:66] if first else '(空)'}")
        sys.exit(1)


if __name__ == "__main__":
    main()
