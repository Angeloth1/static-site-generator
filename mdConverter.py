import markdown
import os
import sys

def Conv(postName):
    md_path = os.path.join("post", postName + ".md") 
    html_folder = "HTML"
    os.makedirs(html_folder, exist_ok=True)
    html_path = os.path.join(html_folder, postName + ".html")

    print(f"DEBUG: md_path={md_path}")
    print(f"DEBUG: html_path={html_path}")

    if not os.path.exists(md_path):
        print(f"[ERROR] Markdown file not found: {md_path}")
        return

    try:
        with open(md_path, "r", encoding="utf-8") as f:
            md_content = f.read()
    except Exception as e:
        print(f"[ERROR] Failed to read {md_path}: {e}")
        return

    try:
        html_cont = markdown.markdown(md_content)
    except Exception as e:
        print(f"[ERROR] Failed to convert Markdown to HTML: {e}")
        return

    try:
        with open(html_path, "w", encoding="utf-8") as f:
            f.write(html_cont)
        print(f"✅ Converted {md_path} → {html_path}")
    except Exception as e:
        print(f"[ERROR] Failed to write HTML file: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python mdConverter.py <post_name>")
        sys.exit(1)
    post_name = sys.argv[1]
    Conv(post_name)
