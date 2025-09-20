import markdown
import os 
import sys

def Conv(postName):
    #βρίσκει και το αρχείο md και κάνει το path για το html αν δεν υπάρχει

    md_path = os.path.join("post",postName +".md")
    html_folder= "HTML"
    os.makedirs(html_folder, exist_ok=True)
    html_path = os.path.join(html_folder, postName +".html")
    
    #κλείνει αν δεν βρει το md
    if not os.path.exists(md_path):
        print("[bold red]No file found[/bold red]")
        return
    
    #διαβάζει το md
    with open(md_path, "r", encoding="utf-8") as f:
        md_content = f.read()
    
    html_cont = markdown.markdown(md_content)

    #Save as Html 
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html_cont)


if __name__ =="__main__":
    post_name = sys.argv[1]
    Conv(post_name)