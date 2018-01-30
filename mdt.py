def mdt(fnm):
    f=open(fnm,"r")
    l=f.readline()
    sp=l.split()
    ln=len(sp)
    fout=open("mac_def.txt","w")
    c=0
    lcnt=1
    while(l!=""):
        if(c==1):
            fout.write(str(lcnt)+"\t"+str(l))
        for i in range(ln):
            if(sp[i]=='%macro'):
                c+=1
            if(sp[i]=='%endmacro'):
                c-=1
        l=f.readline()
        sp=l.split()
        ln=len(sp)
        lcnt+=1
mdt("a.asm")
