import markdown
import os
import sys

def Conv(input_path, output_path):
    # check if input file exists
    if not os.path.exists(input_path):
        print(f"[bold red]No file found: {input_path}[/bold red]")
        return
    
    # read markdown
    with open(input_path, "r", encoding="utf-8") as f:
        md_content = f.read()
    
    html_cont = markdown.markdown(md_content)

    # ensure output folder exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # write html
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html_cont)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python converter.py <input.md> <output.html>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]
    Conv(input_file, output_file)
