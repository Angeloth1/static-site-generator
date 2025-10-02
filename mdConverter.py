import markdown
import os
import sys
from jinja2 import Environment, FileSystemLoader

def Conv(postName):
    # ------------------------
    # Define paths
    # ------------------------
    md_path = os.path.join("post", postName + ".md")  # Input Markdown file
    
    html_folder = "HTML"
    css_folder  = os.path.join(html_folder, "CSS")
    js_folder   = os.path.join(html_folder, "JS")

    os.makedirs(html_folder, exist_ok=True)
    os.makedirs(css_folder, exist_ok=True)
    os.makedirs(js_folder, exist_ok=True)

    html_path = os.path.join(html_folder, postName + ".html")
    css_path  = os.path.join(css_folder, "style.css")
    js_path   = os.path.join(js_folder, "script.js")

    # ------------------------
    # Read Markdown
    # ------------------------
    if not os.path.exists(md_path):
        print(f"[ERROR] Markdown file not found: {md_path}")
        return

    with open(md_path, "r", encoding="utf-8") as f:
        md_content = f.read()

    html_body = markdown.markdown(md_content)

    # ------------------------
    # Extract title from markdown (# Heading)
    # ------------------------
    title = postName
    for line in md_content.splitlines():
        if line.strip().startswith("# "):
            title = line.lstrip("# ").strip()
            break

    # ------------------------
    # Load Jinja2 Template
    # ------------------------
    env = Environment(loader=FileSystemLoader("template"))
    try:
        template = env.get_template("base.html")
    except Exception as e:
        print(f"[ERROR] Missing template: {e}")
        return

    # ------------------------
    # Render final HTML with fixed refs
    # ------------------------
    html_content = template.render(
        content=html_body,
        title=title,
        css_path="CSS/style.css",
        js_path="JS/script.js"
    )

    # ------------------------
    # Save HTML
    # ------------------------
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"✅ Converted {md_path} → {html_path} (title: {title})")

    # ------------------------
    # Ensure global CSS exists (only if missing)
    # ------------------------
    if not os.path.exists(css_path):
        with open(css_path, "w", encoding="utf-8") as f:
            f.write("/* Default stylesheet */\nbody { font-family: Arial, sans-serif; background-color: #121212; color: #eee; }")
        print(f"🆕 Created global CSS: {css_path}")

    # ------------------------
    # Ensure global JS exists (only if missing)
    # ------------------------
    if not os.path.exists(js_path):
        with open(js_path, "w", encoding="utf-8") as f:
            f.write("// Default JavaScript\nconsole.log('Global script loaded');")
        print(f"🆕 Created global JS: {js_path}")


# ------------------------
# CLI Entry Point
# ------------------------
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python mdConverter.py <post_name>")
        sys.exit(1)
    post_name = sys.argv[1]
    Conv(post_name)
