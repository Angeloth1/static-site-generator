import markdown
import os
import sys
from jinja2 import Environment, FileSystemLoader

def Conv(postName):
# ------------------------
# Define paths
# ------------------------
    md_path = os.path.join("post", postName + ".md")  # Input Markdown file
    
    # Folder names
    html_folder = "HTML"
    css_folder  = "CSS"
    js_folder   = "JS"

    # Create folders if missing
    os.makedirs(html_folder, exist_ok=True)
    os.makedirs(css_folder, exist_ok=True)
    os.makedirs(js_folder, exist_ok=True)

    # File paths
    html_path = os.path.join(html_folder, postName + ".html")  # Output HTML file
    css_path  = os.path.join(css_folder, "style.css")          # Global CSS file
    js_path   = os.path.join(js_folder, "script.js")           # Global JS file

    print(f"DEBUG: md_path={md_path}")
    print(f"DEBUG: html_path={html_path}")

# ------------------------
# Read Markdown
# ------------------------
    if not os.path.exists(md_path):
        print(f"[ERROR] Markdown file not found: {md_path}")
        return

    try:
        with open(md_path, "r", encoding="utf-8") as f:
            md_content = f.read()
    except Exception as e:
        print(f"[ERROR] Failed to read {md_path}: {e}")
        return

# ------------------------
# Convert Markdown → HTML
# ------------------------
    try:
        html_body = markdown.markdown(md_content)
    except Exception as e:
        print(f"[ERROR] Failed to convert Markdown to HTML: {e}")
        return

# ------------------------
# Creating the Title
# ------------------------
    title = postName #fallback if no header found
    for line in md_content.splitlines():
        if line.strip().startswith("# "):
            title =line.lstrip("#").strip
            break

# ------------------------
# Load Jinja2 Template
# ------------------------
    env = Environment(loader=FileSystemLoader("template"))  # Look inside /template folder
    try:
        template = env.get_template("base.html")  # Load base template
    except Exception as e:
        print(f"[ERROR] Missing template: {e}")
        return

# Render final HTML (inject converted markdown into template)
    html_content = template.render(content=html_body)

# ------------------------
# Save the final HTML
# ------------------------
    try:
        with open(html_path, "w", encoding="utf-8") as f:
            f.write(html_content)
        print(f"✅ Converted {md_path} → {html_path} (title: {title})")
    except Exception as e:
        print(f"[ERROR] Failed to write HTML file: {e}")

# ------------------------
# Ensure global CSS exists
# ------------------------
    if not os.path.exists(css_path):
        try:
            with open(css_path, "w", encoding="utf-8") as f:
                f.write("/* Global stylesheet */\nbody { font-family: Arial, sans-serif; }")
            print(f"🆕 Created global CSS: {css_path}")
        except Exception as e:
            print(f"[ERROR] Failed to create CSS file: {e}")

# ------------------------
# Ensure global JS exists
# ------------------------
    if not os.path.exists(js_path):
        try:
            with open(js_path, "w", encoding="utf-8") as f:
                f.write("// Global JavaScript\nconsole.log('Global script loaded');")
            print(f"🆕 Created global JS: {js_path}")
        except Exception as e:
            print(f"[ERROR] Failed to create JS file: {e}")


# ------------------------
# CLI Entry Point
# ------------------------
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python mdConverter.py <post_name>")
        sys.exit(1)
    post_name = sys.argv[1]
    Conv(post_name)
