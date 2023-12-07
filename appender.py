def appendtofile(filename,toappend):
    flist = []
    with open(filename,"a+") as f:
        for i in f:
            flist.append(str(i) + "\n")
        fvar = "".join(flist)
        f.write(fvar + (toappend) + "\n")
