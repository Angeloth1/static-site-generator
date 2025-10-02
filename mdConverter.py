import markdown
import os
import sys
from jinja2 import Environment, FileSystemLoader
import shutil

def Conv(postName):
    # Paths
    md_path = os.path.join("post", postName + ".md")
    html_folder = os.path.join("HTML", postName)
    css_folder = os.path.join(html_folder, "css")
    js_folder = os.path.join(html_folder, "js")

    os.makedirs(html_folder, exist_ok=True)
    os.makedirs(css_folder, exist_ok=True)
    os.makedirs(js_folder, exist_ok=True)

    html_path = os.path.join(html_folder, "index.html")
    css_source = os.path.join("CSS", "style.css")
    js_source = os.path.join("JS", "script.js")
    css_path = os.path.join(css_folder, "style.css")
    js_path = os.path.join(js_folder, "script.js")

    # Read Markdown
    if not os.path.exists(md_path):
        print(f"[ERROR] Markdown file not found: {md_path}")
        return

    with open(md_path, "r", encoding="utf-8") as f:
        md_content = f.read()

    html_body = markdown.markdown(md_content)

    # Extract title
    title = postName
    for line in md_content.splitlines():
        if line.strip().startswith("# "):
            title = line.lstrip("# ").strip()
            break

    # Load template
    env = Environment(loader=FileSystemLoader("template"))
    try:
        template = env.get_template("base.html")
    except Exception as e:
        print(f"[ERROR] Missing template: {e}")
        return

    html_content = template.render(
        content=html_body,
        title=title,
        css_path="css/style.css",
        js_path="js/script.js"
    )

    # Save HTML
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html_content)

    print(f"✅ Converted {md_path} → {html_path} (title: {title})")

    # Copy CSS
    if os.path.exists(css_source):
        shutil.copy(css_source, css_path)
    else:
        with open(css_path, "w", encoding="utf-8") as f:
            f.write("body { font-family: Arial, sans-serif; background-color: #121212; color: #eee; }")
        print(f"🆕 Created default CSS: {css_path}")

    # Copy JS
    if os.path.exists(js_source):
        shutil.copy(js_source, js_path)
    else:
        with open(js_path, "w", encoding="utf-8") as f:
            f.write("console.log('Global script loaded');")
        print(f"🆕 Created default JS: {js_path}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python mdConverter.py <post_name>")
        sys.exit(1)
    post_name = sys.argv[1]
    Conv(post_name)
