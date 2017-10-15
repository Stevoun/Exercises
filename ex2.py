S=[]
B=[]
Max=[]
l1=[]
l2=[]
l3=[]
l4=[]

for i in range (0,24):
    x=0
    while i>=0:
        print "Dwse arithmo: "
        num=input()
        B.append(num)
        break
for i in range (0,6):
        l1.append(B[i])
for i in range (6,12):
        l2.append(B[i])
for i in range (12,18):
        l3.append(B[i])
for i in range (18,24):
        l4.append(B[i])
l1.sort()
l2.sort()
l3.sort()
l4.sort()
Max.append(l1[5])
Max.append(l2[5])
Max.append(l3[5])
Max.append(l4[5])


s="4:00pm",Max[0]
S.append(s)
s="5:00pm",Max[1]
S.append(s)
s="6:00pm",Max[2]
S.append(s)
s="7:00pm",Max[3]
S.append(s)

print S
