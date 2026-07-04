import mlx_whisper
import docx
from docx.shared import Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
import json, datetime, os, time

AUDIO  = "/Users/lk/Documents/Claude Code/寿险万能营销/访谈录音/福田网点_20260427.wav"
OUT_DIR = "/Users/lk/Documents/Claude Code/寿险万能营销/访谈录音"

print(f"[{datetime.datetime.now():%H:%M:%S}] 开始转写，模型：large-v3，语言：zh")
print("（首次运行需下载模型，约 1.5 GB，请耐心等待）\n")

t0 = time.time()
result = mlx_whisper.transcribe(
    AUDIO,
    path_or_hf_repo="mlx-community/whisper-large-v3-mlx",
    language="zh",
    word_timestamps=False,
    verbose=True,
)
elapsed = time.time() - t0
print(f"\n[{datetime.datetime.now():%H:%M:%S}] 转写完成，耗时 {elapsed/60:.1f} 分钟")

# 保存原始 JSON（备份）
json_path = os.path.join(OUT_DIR, "福田网点_20260427_raw.json")
with open(json_path, "w", encoding="utf-8") as f:
    json.dump(result, f, ensure_ascii=False, indent=2)
print(f"原始数据已保存：{json_path}")

# ── 生成 Word 文档 ──
doc = docx.Document()

# 页面边距
for section in doc.sections:
    section.top_margin    = docx.shared.Cm(2.54)
    section.bottom_margin = docx.shared.Cm(2.54)
    section.left_margin   = docx.shared.Cm(3.17)
    section.right_margin  = docx.shared.Cm(3.17)

# 标题
title = doc.add_heading("访谈录音转写", level=0)
title.alignment = WD_ALIGN_PARAGRAPH.CENTER
title.runs[0].font.size = Pt(18)
title.runs[0].font.color.rgb = RGBColor(0x1a, 0x1a, 0x2e)

# 元信息
meta = doc.add_paragraph()
meta.alignment = WD_ALIGN_PARAGRAPH.CENTER
run = meta.add_run(f"文件：福田网点_20260427.wav　　转写日期：{datetime.date.today()}　　模型：Whisper large-v3")
run.font.size = Pt(10)
run.font.color.rgb = RGBColor(0x64, 0x74, 0x8b)

doc.add_paragraph()  # 空行

# 正文：按 segment 逐段写入，带时间戳
segments = result.get("segments", [])
if segments:
    for seg in segments:
        start = seg.get("start", 0)
        mm, ss = divmod(int(start), 60)
        hh, mm = divmod(mm, 60)
        ts = f"[{hh:02d}:{mm:02d}:{ss:02d}]" if hh else f"[{mm:02d}:{ss:02d}]"

        p = doc.add_paragraph()
        # 时间戳 run（灰色）
        ts_run = p.add_run(ts + "  ")
        ts_run.font.size = Pt(10)
        ts_run.font.color.rgb = RGBColor(0x94, 0xa3, 0xb8)
        # 正文 run
        txt_run = p.add_run(seg.get("text", "").strip())
        txt_run.font.size = Pt(12)
        p.paragraph_format.space_after = Pt(4)
else:
    # fallback: 整段文字
    doc.add_paragraph(result.get("text", "（无转写结果）"))

# 保存
docx_path = os.path.join(OUT_DIR, "福田网点_20260427_转写.docx")
doc.save(docx_path)
print(f"Word 文档已保存：{docx_path}")
print("完成！")
