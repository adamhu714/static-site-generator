from generator import copy_static_dir, generate_pages_recursive

def main():
    copy_static_dir()
    generate_pages_recursive("./content/", "./template.html", "./public/")



if __name__=="__main__" :
    main()