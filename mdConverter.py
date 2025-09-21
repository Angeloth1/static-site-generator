import markdown
import os
import sys

def Conv(postName):
    # Build paths
    md_path = os.path.join("Post", postName + ".md")  # note uppercase Post
    html_folder = "HTML"
    os.makedirs(html_folder, exist_ok=True)
    html_path = os.path.join(html_folder, postName + ".html")
    
    # Exit if Markdown file doesn't exist
    if not os.path.exists(md_path):
        print(f"[bold red]No file found:[/bold red] {md_path}")
        return
    
    # Read Markdown
    with open(md_path, "r", encoding="utf-8") as f:
        md_content = f.read()
    
    # Convert to HTML
    html_cont = markdown.markdown(md_content)

    # Save HTML
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html_cont)
    print(f"✅ Converted {md_path} → {html_path}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python mdConverter.py <post_name>")
        sys.exit(1)
    post_name = sys.argv[1]
    Conv(post_name)
