import os
import shutil
from jinja2 import Environment, FileSystemLoader

def build_homepage():
    # Load template
    env = Environment(loader=FileSystemLoader("template"))
    try:
        template = env.get_template("base.html")
    except Exception as e:
        print(f"[ERROR] Missing template: {e}")
        return

    # Collect posts
    posts = []
    posts_dir = "post"
    for filename in os.listdir(posts_dir):
        if filename.endswith(".md"):
            post_name = filename[:-3]  # remove .md
            md_path = os.path.join(posts_dir, filename)
            with open(md_path, "r", encoding="utf-8") as f:
                md_content = f.read()
            # Extract title from first H1
            title = post_name
            for line in md_content.splitlines():
                if line.strip().startswith("# "):
                    title = line.lstrip("# ").strip()
                    break
            # Save post info
            posts.append({
                "title": title,
                "link": f"{post_name}/index.html"
            })

    # Generate homepage content as a list of links
    html_body = "<h1>Welcome!</h1>\n<ul>\n"
    for post in posts:
        html_body += f'<li><a href="{post["link"]}">{post["title"]}</a></li>\n'
    html_body += "</ul>"

    # Paths for homepage
    html_folder = "HTML"
    css_folder = os.path.join(html_folder, "css")
    js_folder = os.path.join(html_folder, "js")
    os.makedirs(css_folder, exist_ok=True)
    os.makedirs(js_folder, exist_ok=True)

    html_path = os.path.join(html_folder, "index.html")
    css_path = os.path.join(css_folder, "style.css")
    js_path = os.path.join(js_folder, "script.js")

    # Render template
    html_content = template.render(
        content=html_body,
        title="Home",
        css_path="css/style.css",
        js_path="js/script.js"
    )

    # Save homepage
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html_content)

    # Copy CSS/JS
    shutil.copy("CSS/style.css", css_path)
    shutil.copy("JS/script.js", js_path)

    print(f"✅ Homepage generated → {html_path}")

if __name__ == "__main__":
    build_homepage()
