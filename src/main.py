from generator import copy_static_dir, generate_page

def main():
    copy_static_dir()
    generate_page("./content/index.md", "./template.html", "./public/index.html")



if __name__=="__main__" :
    main()