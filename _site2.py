# -*- coding: utf-8 -*-
import io
zh = """<!DOCTYPE html><html lang="zh"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>A股量化研究工作站｜从研究到交易计划，一个软件闭环</title>
<meta name="description" content="A股+港股+美股多市场量化研究台：实时数据(绝不模拟冒充)、因子体检、自动挖因子、专业回测(Walk-Forward)、AI诊股、职业交易计划书、程序内可视化弹窗。">
<meta property="og:title" content="A股量化研究工作站">
<meta property="og:description" content="从研究一只股票到生成交易计划书的桌面量化研究闭环。">
<meta property="og:image" content="images/dashboard.png">
<meta property="og:type" content="website">
<script type="application/ld+json">{"@context":"https://schema.org","@type":"SoftwareApplication","name":"A股量化研究工作站","operatingSystem":"Windows","applicationCategory":"FinanceApplication","description":"Multi-market quant research workbench with factor lab, professional backtesting, AI diagnosis and trade-plan generator.","offers":{"@type":"Offer","price":"Trial","priceCurrency":"CNY"}}</script>
<style>
:root{--bg:#0b1526;--card:#1e293b;--line:#334155;--fg:#e2e8f0;--mut:#94a3b8;--blue:#3b82f6}
*{box-sizing:border-box;margin:0;padding:0}
body{background:linear-gradient(160deg,#0b1526,#0f172a 55%,#101c33);color:var(--fg);font-family:'Microsoft YaHei','PingFang SC',system-ui,sans-serif;line-height:1.75}
.wrap{max-width:1060px;margin:0 auto;padding:52px 22px}
.tag{color:#93c5fd;letter-spacing:2px;font-size:13px}
h1{font-size:38px;color:#fff;line-height:1.3;margin:10px 0 8px}
h2{color:#fff;font-size:24px;margin:40px 0 14px}
.led{color:#7dd3fc}
.hero{background:var(--card);border:1px solid var(--line);border-radius:18px;padding:24px 26px;margin:18px 0}
.hero b{color:#60a5fa}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:14px;margin:16px 0}
.card{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:18px 20px}
.card h3{color:#7dd3fc;font-size:16px;margin-bottom:8px}
.card p{color:var(--mut);font-size:14px}
.shots{display:grid;grid-template-columns:repeat(auto-fit,minmax(330px,1fr));gap:16px;margin:14px 0}
.shot{background:var(--card);border:1px solid var(--line);border-radius:14px;overflow:hidden}
.shot img{width:100%;display:block;border-bottom:1px solid var(--line)}
.shot div{padding:10px 14px;font-size:13px;color:var(--mut)}
.badge{display:inline-block;background:#123b2a;color:#4ade80;border:1px solid #1f5c40;border-radius:999px;padding:2px 12px;font-size:12px;margin-bottom:8px}
.pills{display:flex;flex-wrap:wrap;gap:8px;margin:16px 0}
.pill{background:#17233b;border:1px solid var(--line);color:#cbd5e1;border-radius:999px;padding:6px 14px;font-size:13px}
.cta{text-align:center;margin:30px 0}
.btn{display:inline-block;background:var(--blue);color:#fff;padding:13px 34px;border-radius:10px;text-decoration:none;font-weight:bold;font-size:16px}
.btn.sub{background:#1e293b;border:1px solid var(--line);margin-left:8px}
ul{margin:8px 0 8px 20px;color:#d7e2f0}
.faq summary{cursor:pointer;color:#e2e8f0;font-weight:bold}
.faq p{color:var(--mut);margin:6px 0 14px}
.foot{color:#64748b;font-size:12px;margin-top:36px;border-top:1px solid var(--line);padding-top:16px}
</style></head><body><div class="wrap">
<div class="tag">A股 · 港股 · 美股 · 多市场量化</div>
<h1>A股量化研究工作站<br>从“研究一只股票”到“生成交易计划书”，一个软件闭环</h1>
<div class="hero"><b>一句话：</b>行情只是入口，我们交付的是一条研究流水线——
多市场实时数据（断网绝不显示假价）→ 因子体检与自动挖因子 → 专业回测（Walk-Forward 防过拟合）→ AI 诊股与大模型解读 → 策略库 → 市场状态与职业交易计划书（仓位/止损/合规预检）→ 全程程序内可视化弹窗，不用去文件夹翻报告。</div>

<div class="pills">
<span class="pill">实时价·收盘自动标注</span><span class="pill">Alpha101/158 因子</span><span class="pill">自动挖因子</span>
<span class="pill">Walk-Forward 回测</span><span class="pill">自然语言生成策略</span><span class="pill">组合驾驶舱</span>
<span class="pill">交易计划书</span><span class="pill">盘前简报·自动推送</span><span class="pill">程序内弹窗看图</span>
</div>

<h2>真实界面</h2>
<div class="shots">
<div class="shot"><img src="images/dashboard.png" alt="行情看板：实时行情与市场情绪"><div>📊 行情看板：多市场实时行情 · 市场情绪 · 自动刷新（每3秒）</div></div>
<div class="shot"><img src="images/kline.png" alt="K线图：交互式K线、均线与技术指标"><div>📈 交互式K线：均线/成交量/技术指标，双击可一键“综合诊断”</div></div>
<div class="shot"><img src="images/research.png" alt="研究实验室：因子体检、专业回测、计划书"><div>🧬 研究实验室：因子/回测/计划书/驾驶舱，全部程序内可视化弹窗</div></div>
</div>

<h2>能做什么</h2>
<div class="grid">
<div class="card"><h3>🗂 多市场全名单</h3><p>全A股 + 港股 + 美股，实时接入；断网/接口失败时显示最近收盘并标注，绝不拿模拟价冒充实时。</p></div>
<div class="card"><h3>🧬 研究实验室</h3><p>Alpha101/Alpha158 因子、IC/RankIC 体检、遗传规划自动挖因子——把“感觉”变成可检验的统计。</p></div>
<div class="card"><h3>⚡ 专业回测</h3><p>多策略模板、参数寻优、Walk-Forward 样本外验证、手续费/滑点/止损——专治“回测骗自己”。</p></div>
<div class="card"><h3>🤖 AI 融合</h3><p>一句话生成策略、大模型诊股与情绪解读（内置免费/低价通道，无 Key 自动本地降级）。</p></div>
<div class="card"><h3>🧭 组合诊断</h3><p>多基准归因、风格暴露(RBSA)、MCTR/CVaR 风险分解、持仓效率象限。</p></div>
<div class="card"><h3>📋 职业交易计划书</h3><p>市场状态→技术快照→头寸计算→实盘合规预检→情景计划，把分析落成可执行清单。</p></div>
</div>

<h2>为什么值得信任</h2>
<ul>
<li><span class="badge">仅实时</span> 默认只显示实时/最近收盘真实数据；模拟数据默认关闭，绝不冒充</li>
<li><span class="badge">本地单文件</span> Windows 桌面单文件运行，数据本地化，无需自建服务器</li>
<li><span class="badge">7天试用</span> 全功能免费试用，满意再考虑授权</li>
<li><span class="badge">研究工具定位</span> 不荐股、不承诺收益，全程合规风险提示</li>
</ul>

<div class="cta">
<a class="btn" href="mailto:astockquant@example.com">私信领取试用码</a>
<a class="btn sub" href="https://github.com/Lilong123-93790997/astock-quant-site">查看仓库</a>
</div>

<h2>常见问题</h2>
<div class="faq">
<details><summary>数据是真的实时吗？</summary><p>是。行情来自腾讯/东财/新浪等公开实时接口：盘中自动刷新；收盘/休市显示最近一笔真实成交并标注“收盘”；接口失败时宁可显示最近数据并提示，也不显示假价。</p></details>
<details><summary>支持美股港股吗？</summary><p>支持。内置全A股+港股+美股名单，A股/港股/美股行情与K线均可查看与研究。</p></details>
<details><summary>我是新手能用吗？</summary><p>能。看行情、双击看综合诊断、一键出因子体检和交易计划书都不需要编程；进阶的因子与回测功能可按教程逐步学习。</p></details>
</div>

<div class="foot">
⚠️ 本软件为量化研究/教学工具：所有行情均标注来源与实时/收盘状态；回测与信号基于历史数据，不构成投资建议；股市有风险，入市需谨慎。<br>
© A股量化研究工作站 · GitHub 页面更新于 2026-09
</div>
</div></body></html>"""

en = """<!DOCTYPE html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-width">
<title>A-Share Quant Research Workbench</title>
<meta name="description" content="Multi-market quant research workbench: live data (never faked), factor lab, professional backtesting with walk-forward, AI diagnosis and trade-plan generator.">
<meta property="og:image" content="images/dashboard.png">
<style>body{background:#0b1526;color:#e2e8f0;font-family:system-ui,-apple-system,'Segoe UI',sans-serif;max-width:1000px;margin:0 auto;padding:46px 22px;line-height:1.7}
h1{color:#fff;font-size:34px}.bl{color:#7dd3fc}.card{background:#1e293b;border:1px solid #334155;border-radius:14px;padding:18px 20px;margin:10px 0}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:12px;margin:18px 0}
.shots{display:grid;grid-template-columns:repeat(auto-fit,minmax(320px,1fr));gap:14px}
.shot{background:#1e293b;border:1px solid #334155;border-radius:12px;overflow:hidden}
.shot img{width:100%;display:block}.shot div{padding:10px 14px;color:#94a3b8;font-size:13px}
.pill{display:inline-block;background:#17233b;border:1px solid #334155;border-radius:999px;padding:5px 12px;margin:4px;font-size:13px}
.btn{display:inline-block;background:#3b82f6;color:#fff;padding:12px 30px;border-radius:10px;text-decoration:none;font-weight:bold;margin-top:14px}
.foot{color:#64748b;font-size:12px;margin-top:30px;border-top:1px solid #334155;padding-top:14px}</style>
</head><body>
<div class="bl">A-SHARE · HK · US · QUANT RESEARCH</div>
<h1>A-Share Quant Research Workbench<br>From “researching one stock” to “a trade plan”, in one closed loop.</h1>
<p style="color:#94a3b8">Live multi-market data (never faked when offline) → factor lab & auto factor mining → professional backtesting with Walk-Forward → AI diagnosis → strategy vault → market regime & professional trade plan (position sizing / stops / compliance pre-check) → all rendered in in-app visual popups.</p>
<div style="margin:14px 0">
<span class="pill">Real-time + last-close tagging</span><span class="pill">Alpha101/158 factors</span><span class="pill">Auto factor mining</span>
<span class="pill">Walk-Forward backtest</span><span class="pill">NLP strategy generation</span><span class="pill">Portfolio cockpit</span>
<span class="pill">Trade plan generator</span><span class="pill">In-app report popups</span>
</div>
<h2 style="color:#fff">Screenshots</h2>
<div class="shots">
<div class="shot"><img src="images/dashboard.png" alt="Dashboard"><div>Live dashboard with multi-market quotes and market sentiment</div></div>
<div class="shot"><img src="images/kline.png" alt="K-line"><div>Interactive K-line with MAs, volume and technical indicators</div></div>
<div class="shot"><img src="images/research.png" alt="Research lab"><div>Factor lab, backtesting and trade-plan generator</div></div>
</div>
<div class="grid">
<div class="card"><b>Factor Lab</b><p>Alpha101/Alpha158, IC/RankIC review, genetic auto factor mining.</p></div>
<div class="card"><b>Professional Backtest</b><p>Multi-strategy, parameter search, walk-forward OOS, costs/slippage/stops.</p></div>
<div class="card"><b>AI Fusion</b><p>One-sentence strategy generation, LLM stock diagnosis & sentiment with graceful fallback.</p></div>
<div class="card"><b>Portfolio Cockpit</b><p>Multi-benchmark attribution, RBSA style exposure, MCTR/CVaR risk decomposition.</p></div>
<div class="card"><b>Trade Plan</b><p>Regime → technical snapshot → position sizing → compliance pre-check → scenario plan.</p></div>
<div class="card"><b>Honest Data</b><p>Real-time when open; tagged last-close when closed; simulated data never shown by default.</p></div>
</div>
<p>Windows desktop app · local data · 7-day full trial. Research & education tool only — not investment advice.</p>
<a class="btn" href="https://github.com/Lilong123-93790997/astock-quant-site">View repository</a>
<div class="foot">© A-Share Quant Research Workbench · Disclaimer: historical backtests do not guarantee future results.</div>
</body></html>"""
with open("index.html", "w", encoding="utf-8") as f:
    f.write(zh)
with open("index_en.html", "w", encoding="utf-8") as f:
    f.write(en)
print("rewrote index.html / index_en.html")
