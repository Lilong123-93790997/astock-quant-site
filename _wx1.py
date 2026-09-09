# -*- coding: utf-8 -*-
import io
zh = io.open("index.html", encoding="utf-8").read()

# 1) CTA 改为加微信
old_cta = '<a class="btn" href="mailto:astockquant@example.com">私信领取试用码</a>'
new_cta = '<a class="btn" href="#wechat">加微信领试用码（7天）</a>'
assert old_cta in zh
zh = zh.replace(old_cta, new_cta, 1)

# 2) 在 FAQ 之前插入“联系/加微信”区
faq_marker = '<h2>常见问题</h2>'
wechat_section = '''<h2 id="wechat">📲 加微信领 7 天免费试用</h2>
<div class="card" style="max-width:640px;margin:0 auto;text-align:center">
  <p style="color:#94a3b8">扫码或复制微信号，添加后发送 <b style="color:#60a5fa">“试用”</b>，即可领取 7 天全功能授权码。</p>
  <img id="wxqr" src="images/wechat-qr.png" alt="微信二维码" style="width:200px;border-radius:12px;border:1px solid #334155;margin:10px auto;display:block"
       onerror="document.getElementById('wxqr').style.display='none';document.getElementById('wxqrfake').style.display='block'">
  <div id="wxqrfake" style="display:none;border:1px dashed #334155;border-radius:12px;padding:26px;margin:10px auto;color:#64748b">微信二维码占位（请作者上传 images/wechat-qr.png）</div>
  <p style="font-size:18px;font-weight:bold;color:#fff">微信号：<span id="wxid">AStockQuant01</span>
     <button onclick="copyWx()" style="background:#3b82f6;color:#fff;border:0;border-radius:8px;padding:8px 18px;margin-left:8px;cursor:pointer;font-weight:bold">一键复制微信号</button></p>
  <p style="color:#64748b;font-size:12px">（演示占位，正式微信号上线前请作者替换 index.html 里的 AStockQuant01 与 wechat-qr.png）</p>
</div>
<script>
function copyWx(){ var t=document.getElementById('wxid').innerText;
  (navigator.clipboard? navigator.clipboard.writeText(t) : (function(){var i=document.createElement('textarea');i.value=t;document.body.appendChild(i);i.select();document.execCommand('copy');document.body.removeChild(i);})())
  .then?undefined:undefined; alert('微信号已复制：'+t); }
</script>

'''
assert faq_marker in zh
zh = zh.replace(faq_marker, wechat_section + faq_marker, 1)
io.open("index.html","w",encoding="utf-8").write(zh)
print("index.html updated with WeChat CTA")
