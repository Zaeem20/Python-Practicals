while True:
    print("""1.Create a directory\n2.remove a directory\n3.rename a file\n4.delete a file\n5.display the present working directory\n6.create a file and store contents in it\n7.display the content of the file\n8.exit the program""")
    
    n=int(input("select an option: "))
    import os
    if n==1:
        mdir=str(input("Enter the name of directory"))
        os.mkdir(mdir)
    elif n==2:
        rdir=str(input("Enter directory name to remove"))
        os.rmdir(rdir)
    elif n==3:
        redir=str(input("Enter previous file name"))
        rendir=str(input("Enter the new file name"))
        os.rename(redir,rendir)
    elif n==4:
        remove=str(input("Enter file name to delete"))
        os.remove(remove)
    elif n==5:
        print(os.getcwd())
    elif n==6:
        fname=str(input("Enter the file name with extension:::"))
        f=open(fname,"w")
        f_write=str(input("Enter the content into the file::"))
        f.write(f_write)
        f.close()
    elif n==7:
        f_name=str(input("Enter the file name  "))
        f=open(f_name,"r")
        a=f.read()
        print(a)
        f.close()
    else:
        break
