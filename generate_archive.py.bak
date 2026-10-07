#!/usr/bin/env python3
"""从 data.json 自动生成 archive.html"""
import json, os

DATA = r"D:\WorkBuddy输出\法商知识内参\output\data.json"
OUT = r"D:\WorkBuddy输出\法商知识内参\output\archive.html"
INDEX = r"D:\WorkBuddy输出\法商知识内参\output\index.html"

with open(DATA, encoding="utf-8") as f:
    records = json.load(f)

total = len(records)

entries_html = ""
for r in reversed(records):
    entries_html += f"""            <a class="entry" href="{r['file']}">
                <div class="entry-date">{r['date']}</div>
                <div class="entry-topic">{r['topic']}</div>
                <div class="entry-summary">{r['summary']}</div>
            </a>
"""

html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>法商小知识 · 历史回顾</title>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{ background: #0a0a0a; min-height: 100vh; padding: 20px; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif; color: #fff; }}
        .container {{ max-width: 420px; margin: 0 auto; }}
        .header {{ text-align: center; padding: 32px 0 24px; }}
        .header-title {{ font-size: 28px; font-weight: 700; letter-spacing: 2px; color: #c9a96e; }}
        .header-sub {{ font-size: 11px; color: rgba(255,255,255,0.4); margin-top: 8px; }}
        .stats {{ text-align: center; padding: 12px; background: rgba(255,255,255,0.03); border-radius: 10px; margin-bottom: 24px; font-size: 12px; color: rgba(255,255,255,0.5); }}
        .stats span {{ color: #c9a96e; font-weight: 600; font-size: 18px; }}
        .entry-list {{ display: flex; flex-direction: column; gap: 10px; }}
        .entry {{ background: linear-gradient(135deg, #1a1a1a 0%, #0d0d0d 100%); border-radius: 12px; padding: 16px; text-decoration: none; display: block; border: 1px solid rgba(255,255,255,0.05); }}
        .entry:hover {{ border-color: rgba(201,169,110,0.3); background: linear-gradient(135deg, #222 0%, #111 100%); }}
        .entry-date {{ font-size: 11px; color: #c9a96e; margin-bottom: 6px; letter-spacing: 1px; }}
        .entry-topic {{ font-size: 15px; font-weight: 600; color: #e8e8e8; line-height: 1.5; }}
        .entry-summary {{ font-size: 12px; color: rgba(255,255,255,0.45); margin-top: 8px; line-height: 1.6; }}
        .back-link {{ display: block; text-align: center; padding: 20px; color: rgba(255,255,255,0.4); font-size: 13px; text-decoration: none; }}
        .back-link:hover {{ color: #c9a96e; }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <div class="header-title">法商小知识</div>
            <div class="header-sub">历史回顾</div>
        </div>
        <div class="stats">已推送 <span>{total}</span> 篇法商知识</div>
        <div class="entry-list">
{entries_html}        </div>
        <a href="index.html" class="back-link">← 返回今日推送</a>
    </div>
</body>
</html>"""

with open(OUT, "w", encoding="utf-8") as f:
    f.write(html)

print(f"✅ archive.html 已更新，共 {total} 篇")
