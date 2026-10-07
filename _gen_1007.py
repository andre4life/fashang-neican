# -*- coding: utf-8 -*-
import json, re, shutil, os

TODAY = "2026-10-07"
FS = f"fs_{TODAY}.html"

html = open(FS, encoding="utf-8").read()

# 抽取 topic / 3个 section-content / summary-content
topic = re.search(r'<div class="topic">(.*?)</div>', html, re.S).group(1).strip()
sections = re.findall(r'<div class="section-content">(.*?)</div>', html, re.S)
summary = re.search(r'<div class="summary-content">(.*?)</div>', html, re.S).group(1).strip()
assert len(sections) == 3, f"section 数不对: {len(sections)}"
law_points, practice_scene, risk_alert = [s.strip() for s in sections]

# ---------- 1. data.json ----------
data = json.load(open("data.json", encoding="utf-8"))
new_rec = {
    "date": TODAY,
    "topic": topic,
    "summary": summary,
    "file": FS,
}
# 替换同日记录（远端 Actions 生成的重复话题版）
before = len(data)
data = [r for r in data if r["date"] != TODAY]
data.append(new_rec)
data.sort(key=lambda r: r["date"])
# 校验：无 ASCII 双引号、日期唯一
assert '"' not in json.dumps(new_rec, ensure_ascii=False).replace('"', '', 0) or True
dates = [r["date"] for r in data]
assert len(dates) == len(set(dates)), "日期有重复！"
for r in data:
    assert '"' not in r["summary"], f"{r['date']} summary 含 ASCII 双引号"
    assert '"' not in r["topic"], f"{r['date']} topic 含 ASCII 双引号"
json.dump(data, open("data.json", "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print(f"data.json: {before} -> {len(data)} 条, 末条 {data[-1]['date']} | {data[-1]['topic'][:30]}")

# ---------- 2. content_bank.json ----------
cb = json.load(open("content_bank.json", encoding="utf-8"))
cb = [x for x in cb if x.get("topic") != topic]
cb.append({
    "topic": topic,
    "law_points": law_points,
    "practice_scene": practice_scene,
    "risk_alert": risk_alert,
    "summary": summary,
})
json.dump(cb, open("content_bank.json", "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print(f"content_bank.json: -> {len(cb)} 条")

# ---------- 3. index.html = 当日 fs 逐字节复制 ----------
shutil.copyfile(FS, "index.html")
print("index.html <-", FS, "| identical:", open("index.html",encoding='utf-8').read()==html)
