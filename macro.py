def mac(fnm):
    lcnt=0
    mcnt=0
    maccnt=[]
    macnm=[]
    macprm=[]
    macstr=[]
    macend=[]
    fout=open("macro.txt","w")
    fout.write("No"+"\t"+"macname"+"\t"+"   parameters"+"\t"+"start"+"\t"+"end"+"\n")
    fin=open(fnm,"r")
    l=fin.readline()
    for l in fin:
        lcnt+=1
        s=l.split()
        print(s)
        for i in range(len(s)):
            if(s[i]=="%macro"):
                mcnt+=1
                maccnt.append(mcnt)
                macstr.append(lcnt)
                macnm.append(s[i+1])
                macprm.append(s[i+2])
            if(s[i]=="%endmacro"):
               macend.append(lcnt)

    for i in range(len(macnm)):
        fout.write(str(maccnt[i])+"\t"+str(macnm[i])+"\t\t"+str(macprm[i])+"\t"+str(macstr[i])+"\t"+str(macend[i])+"\n")

mac("a.asm")
