from pdf2image import convert_from_path

pages = convert_from_path("./static/images/exp1-1.pdf", dpi=300)  # 默认是 200

for i, page in enumerate(pages):
    page.save(f"./static/images/exp1.png", "PNG")


