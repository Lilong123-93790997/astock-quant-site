# -*- coding: utf-8 -*-
import os, io
from PIL import Image
IMG = "images"

# 1) banner.png（三图横排）
names = ["dashboard.png", "diagnosis.png", "backtest.png"]
imgs = [Image.open(os.path.join(IMG, n)).convert("RGB") for n in names]
H = 360
tiles = []
for im in imgs:
    r = H / im.height
    im2 = im.resize((int(im.width * r), H))
    tiles.append(im2)
wsum = sum(t.width for t in tiles)
canvas = Image.new("RGB", (wsum, H), (11, 21, 38))
x = 0
for t in tiles:
    canvas.paste(t, (x, 0)); x += t.width
canvas.save(os.path.join(IMG, "banner.png"))
print("banner", canvas.size)

zh = io.open("index.html", encoding="utf-8").read()
# 在 research.png 那条后面追加诊断/回测两张
anchor = '<div class="shot"><img src="images/research.png" alt="研究实验室：因子体检、专业回测、计划书"><div>🧬 研究实验室：因子/回测/计划书/驾驶舱，全部程序内可视化弹窗</div></div>'
add = anchor + '''
<div class="shot"><img src="images/diagnosis.png" alt="个股综合诊断弹窗"><div>🧭 双击任意股票 → 个股综合诊断：K线+RSI/MACD+因子快照</div></div>
<div class="shot"><img src="images/backtest.png" alt="专业回测弹窗"><div>⚡ 专业回测：净值/回撤/月度热力图/绩效，程序内弹窗直出</div></div>'''
assert anchor in zh
zh = zh.replace(anchor, add, 1)
# og:image 换成 banner
zh = zh.replace('content="images/dashboard.png"', 'content="images/banner.png"', 1)
# CTA 加功能页链接
zh = zh.replace('<a class="btn sub" href="https://github.com/Lilong123-93790997/astock-quant-site">查看仓库</a>',
                '<a class="btn sub" href="features.html">功能与版本</a>\n<a class="btn sub" href="https://github.com/Lilong123-93790997/astock-quant-site">查看仓库</a>', 1)
io.open("index.html", "w", encoding="utf-8").write(zh)
print("index.html updated")

en = io.open("index_en.html", encoding="utf-8").read()
anchor_en = '<div class="shot"><img src="images/research.png" alt="Research lab"><div>Factor lab, backtesting and trade-plan generator</div></div>'
add_en = anchor_en + '''
<div class="shot"><img src="images/diagnosis.png" alt="Stock diagnosis"><div>Double-click any stock for a full diagnosis popup (K-line + RSI/MACD + factors)</div></div>
<div class="shot"><img src="images/backtest.png" alt="Backtest popup"><div>Professional backtest rendered right inside the app</div></div>'''
assert anchor_en in en
en = en.replace(anchor_en, add_en, 1)
en = en.replace('content="images/dashboard.png"', 'content="images/banner.png"', 1)
io.open("index_en.html", "w", encoding="utf-8").write(en)
print("index_en.html updated")

features = """<!DOCTYPE html><html lang="zh"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>功能与版本｜A股量化研究工作站</title>
<style>body{background:#0b1526;color:#e2e8f0;font-family:'Microsoft YaHei',system-ui,sans-serif;max-width:1000px;margin:0 auto;padding:40px 22px;line-height:1.8}
h1{color:#fff}table{width:100%;border-collapse:collapse;background:#1e293b;border:1px solid #334155;border-radius:12px;overflow:hidden;font-size:14px}
th,td{padding:10px 12px;border-bottom:1px solid #334155;text-align:left}th{color:#93c5fd;background:#0b1526}
td{color:#cbd5e1}.y{color:#4ade80}.n{color:#64748b}
a{color:#60a5fa}</style></head><body>
<h1>功能模块总览</h1>
<table><tr><th>模块</th><th>说明</th></tr>
<tr><td>多市场实时行情</td><td>A股/港股/美股：实时价、K线、盘口；默认仅实时，收盘自动标注，不显示假价</td></tr>
<tr><td>全市场名单</td><td>全A股+港股+美股（断网用内置名单兜底，只补名称不带假价）</td></tr>
<tr><td>K线与个股综合诊断</td><td>交互式K线；双击一键弹窗：K线+RSI/MACD+158因子快照</td></tr>
<tr><td>研究实验室-因子</td><td>Alpha101/Alpha158、IC/RankIC 体检、自动因子挖掘</td></tr>
<tr><td>专业回测</td><td>多策略模板、参数寻优、Walk-Forward 样本外验证、成本/滑点/止损</td></tr>
<tr><td>自然语言生成策略</td><td>一句话描述→可回测策略（可选大模型结构化）</td></tr>
<tr><td>策略库</td><td>保存/载入/回测/计划书闭环</td></tr>
<tr><td>组合诊断驾驶舱</td><td>多基准归因、风格暴露(RBSA)、MCTR/CVaR、持仓效率象限</td></tr>
<tr><td>职业交易计划书</td><td>市场状态→头寸→合规预检→情景计划</td></tr>
<tr><td>AI诊股/大模型解读</td><td>免费/低价通道，无Key自动本地降级</td></tr>
<tr><td>盘前简报/每日复盘</td><td>自动生成并推送 Bark/Server酱/企业微信</td></tr>
<tr><td>程序内可视化</td><td>所有研究结果弹窗看图看表，不用翻文件夹</td></tr>
</table>

<h1>版本说明（以商家报价为准）</h1>
<table><tr><th>版本</th><th>定位</th><th>行情</th><th>研究/回测/计划书</th><th>授权</th></tr>
<tr><td>免费试用</td><td>体验</td><td class="y">✓</td><td class="y">✓（7天）</td><td>7天试用码</td></tr>
<tr><td>客户版</td><td>个人研究</td><td class="y">✓</td><td class="y">✓</td><td>年/永久授权</td></tr>
<tr><td>专业版</td><td>深度研究/多屏</td><td class="y">✓</td><td class="y">✓（全部研究功能）</td><td>年授权</td></tr>
<tr><td>机构/带教版</td><td>私募/教学/白标</td><td class="y">✓</td><td class="y">✓</td><td>定制授权</td></tr>
</table>
<p style="color:#94a3b8;font-size:13px">⚠️ 研究/教学工具定位，不构成投资建议；具体价格与版本请私信咨询。</p>
<p><a href="index.html">← 返回首页</a></p>
</body></html>"""
io.open("features.html", "w", encoding="utf-8").write(features)
io.open("robots.txt", "w", encoding="utf-8").write("User-agent: *\nAllow: /\n")
print("features.html + robots.txt written")

readme = """# A股量化研究工作站 · A-Share Quant Research Workbench

> 从“研究一只股票”到“生成交易计划书”，一个软件闭环。
> From "researching one stock" to "a trade plan", in one closed loop.

![banner](images/banner.png)

Live site: https://lilong123-93790997.github.io/astock-quant-site/ · 中文首页 [index.html](index.html) · English [index_en.html](index_en.html) · 功能与版本 [features.html](features.html)

## 功能特性 Features
- 多市场实时行情（A股/港股/美股）：默认仅实时；收盘显示最近一笔真实价并标注；**绝不拿模拟数据冒充实时**。
- 全市场名单：全A股 + 港股 + 美股（断网用内置名单兜底，只补名称不带假价）。
- 交互式K线 + 双击“个股综合诊断”（K线+RSI/MACD+158因子快照）。
- 研究实验室：Alpha101/Alpha158 因子、IC/RankIC 体检、遗传规划自动挖因子。
- 专业回测：多策略模板、参数寻优、Walk-Forward 样本外验证、手续费/滑点/止损。
- 自然语言生成策略：一句话描述 → 自动变可回测策略（可选大模型结构化）。
- 策略库：保存/载入/回测/生成交易计划书。
- 组合诊断驾驶舱：多基准归因、RBSA 风格暴露、MCTR/CVaR 风险分解、持仓效率象限。
- 职业交易计划书：市场状态 → 技术快照 → 头寸计算 → 实盘合规预检 → 情景计划。
- 盘前作战简报 / 每日复盘：自动生成并推送（Bark / Server酱 / 企业微信）。
- 程序内可视化弹窗：研究结果直接弹窗看图看表，无需去文件夹找文件。

## 体验 Trial
- 平台：Windows 10/11（64位），单文件绿色运行。
- 试用：7 天全功能免费试用；正式授权码请联系作者。

## 免责声明 Disclaimer
本软件为量化研究/教学工具，不构成任何投资建议；历史回测不代表未来表现；股市有风险，入市需谨慎。
This software is a research/education tool. It does NOT provide investment advice. Past backtests do not guarantee future results.
"""
io.open("README.md", "w", encoding="utf-8").write(readme)
print("README.md updated")
