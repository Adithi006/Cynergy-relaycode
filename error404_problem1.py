#adithi.p
l=[[1,1,1,1,0],[1,1,0,1,0],[1,1,0,0,1],[1,0,1,1,0]]
a=[[1,1,1,0,1],[0,1,1,1,0],[1,0,0,1,0],[1,0,1,1,1]]
n=[[1,0,1,1,0],[0,0,1,1,0],[1,1,0,1,1],[0,0,1,1,0]]
d=[[1,1,1,0,1],[1,1,0,0,1],[1,1,1,0,0],[1,1,0,0,1]]
print('the grid is: \n',l,"\n",a,"\n",n,"\n",d)

if l[0][0]==1 & a[0][0]==1 & n[0][0]==1 & d[0][0]==1:
    print('output:',1)
elif l[0][1]==1 & a[0][1]==1 & n[0][1] & d[0][1]==1:
    print('output:',1)
elif l[0][2]==1 & a[0][2]==1 & n[0][2]==1 & d[0][2]==1:
    print('output:',1)
elif l[0][3]==1 & a[0][3]==1 & n[0][3]==1 & d[0][3]==1:
    print('output:',1)
elif l[0][4]==1 & a[0][4]==1 & n[0][4]==1 & d[0][4]==1:
    print('output:',1)

elif l[1][0]==1 & a[1][0]==1 & n[1][0]==1 & d[1][0]==1:
    print('output:',1)
elif l[1][1]==1 & a[1][1]==1 & n[1][1]==1 & d[1][1]==1:
    print('output:',1)
elif l[1][2]==1 & a[1][2]==1 & n[1][2]==1 & d[1][2]==1:
    print('output:',1)
elif l[1][3]==1 & a[1][3]==1 & n[1][3]==1 & d[1][3]==1:
    print('output:',1)
elif l[1][4]==1 & a[1][4]==1 & n[1][4]==1 & d[1][4]==1:
    print('output:',1)

else: 
    print('output: ',0)


