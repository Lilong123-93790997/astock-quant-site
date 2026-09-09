# 把官网部署到 GitHub Pages（浏览器版，约 2 分钟）

前提：已登录 github.com（你说已登录 ✅）。

## 第 1 步：新建仓库
1. 打开 https://github.com/new
2. Repository name 填：`astock-quant-site`（或任意英文名，如 `quant-research-workbench`）
3. 选 **Public**（公开，GitHub Pages 免费）
4. 不要勾选 “Add a README”（避免冲突），点 **Create repository**

## 第 2 步：上传文件（用网页拖拽）
1. 进入刚建的仓库
2. 点 **uploading an existing file**（或 Add file → Upload files）
3. 把本目录（`推广资料\site`）里的 **index.html**（可再带上 index_en.html、README.md）**拖进去**
4. 点 **Commit changes**

## 第 3 步：开启 Pages
1. 仓库页 → **Settings**
2. 左侧找 **Pages**
3. Source 选 **Deploy from a branch**，Branch 选 **main**，目录选 **/ (root)** → **Save**
4. 等 1–2 分钟，出现网址：`https://<你的用户名>.github.io/astock-quant-site/`

## 第 4 步：验证并开始用
- 打开上面的网址，手机也能看 → 这就是你的“官网落地页”
- 把网址放进：短视频主页简介、知乎签名、公众号菜单、微信群公告、落地页按钮

## 可选
- 把 `index_en.html` 设为英文版链接分享给海外用户
- 之后想改内容：在仓库直接点 `index.html` → 铅笔图标编辑 → Commit，网页会自动更新
- 想用自己域名（如 www.xxx.com）：仓库 Settings→Pages→Custom domain 填域名，再到域名服务商加 CNAME 记录指向 `<用户名>.github.io`
