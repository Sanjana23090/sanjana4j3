def outf():         #2nd
    var=10         #3
    def innf():     #5
        var=20    #6
        print("inner var ",var) #7
    innf()           #4
    print("Outer var ",var)    #8
outf() #executes frst
