B=[]
S=[]
nai="Y"
oxi="N"
for j in range (0,7):
    x=0
    i=0
    while i>=0:
        print " Dwse",i+1,"arithmo sistoixias: "
        num= input()
        x=x+num
        B.append(num)
        i=i+1
        answer= input( "Telos sistoixias? nai/oxi: ")

        if answer==nai :
            break
    S.append(x)
    while S[j-1]<S[j]:
        print "mallon phres",S[j]-S[j-1],"provata apo ton geitona :)"
        print "THA PREPEI NA KSANADWSEIS SISTOIXIA...."
        B.remove(num)
        S.remove(x)
        i=0
        x=0
        while i>=0:
            print " Dwse",i+1,"arithmo sistoixias: "
            num= input()
            x=x+num
            B.append(num)
            i=i+1
            answer= input( "Telos sistoixias? nai/oxi: ")

            if answer==nai :
                break
        S.append(x)

    answer= input ("Telos? nai/oxi: ")
    if answer==nai :
        break
print "Dwse arithmo provatwn: "
count=input()

while count < S[0]:
    print "Adinato na einai mikrotero apo to sinolo twn provatwn p girisan thn prwth mera, ksanadwse:"
    count=input()
print count -S[j]
