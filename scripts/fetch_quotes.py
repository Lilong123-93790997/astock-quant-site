# -*- coding: utf-8 -*-
"""GitHub Actions 定时抓取行情 -> data/quotes.json（官网实时面板数据源）"""
import json, os, datetime, urllib.request

CODES = ["sh000001", "sz399001", "sz399006", "sh000300",
         "sh600519", "sz000001", "sz300750", "sh601318", "sh600036", "sz000858"]

def fetch(batch):
    url = "https://qt.gtimg.cn/q=" + ",".join(batch)
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=15) as r:
        return r.read().decode("gbk", "ignore")

def parse(text):
    items = []
    for line in text.split(";"):
        if "~" not in line:
            continue
        p = line.split("~")
        if len(p) < 35:
            continue
        try:
            items.append({
                "code": p[2], "name": p[1], "price": float(p[3] or 0),
                "pct": float(p[32] or 0), "prev": float(p[4] or 0),
                "time": p[30] if len(p) > 30 else "",
            })
        except Exception:
            continue
    return items

def main():
    items = []
    for i in range(0, len(CODES), 20):
        try:
            items += parse(fetch(CODES[i:i+20]))
        except Exception as e:
            print("fetch error:", e)
    data = {
        "updated": datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC"),
        "updated_cst": (datetime.datetime.utcnow() + datetime.timedelta(hours=8)).strftime("%Y-%m-%d %H:%M:%S"),
        "items": items,
    }
    os.makedirs("data", exist_ok=True)
    with open(os.path.join("data", "quotes.json"), "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print("saved", len(items), "quotes")

if __name__ == "__main__":
    main()
