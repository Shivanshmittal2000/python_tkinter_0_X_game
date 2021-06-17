def checkwin(a,i,j):
    p=a[i][j]
    m=0
    for k in range(3):
        if a[i][k]==p:
            m+=1
    if m==3:
        return True
    m=0
    for k in range(3):
        if a[k][j]==p:
            m+=1
    if m==3:
        return True
    m=0
    for k in range(3):
        if a[k][k]==p:
            m+=1
    if m==3:
        return True
    c=2
    m=0
    for k in range(3):
        if a[c][k]==p:
            m+=1
            c-=1
    if m==3:
        return True
    return False
def isitwin(a,i,j):
    if checkwin(a,i,j):
        return True
    else :
        return False
def userA(a,i,j,d,name1,name2):
#     print(a)
    a[i][j]=0
    for h in a:
        for t in h:
            print(t,end=" ")
        print()
    output=isitwin(a,i,j)
    if output==True:
        print(" User",name1,"wins")
        return 
    else :
        h=1
        while h==1:
            if d>=9:
                print("Game draw")
                return 
            location=int(input())
            if location<0 or location>9 or visited[location]==True:
                print("Please enter a valid choice")
            elif visited[location]==False:
                visited[location]=True
                i=(location-1)//3
                j=(location-1)%3
                d+=1
                return userB(a,i,j,d,name1,name2)
def userB(a,i,j,d,name1,name2):
    a[i][j]="X"
#     print(a)
    for h in a:
        for l in h:
            print(l,end=" ")
        print()
    isitwin(a,i,j)
    output=isitwin(a,i,j)
    if output==True:
        print(" User",name2,"wins")
        return 
    else :
        if d>=9:
            print("game draw")
            return 
        location=int(input())
        h=1
        while h==1:
            if location<0 or location>9 or visited[location]==True:
                print("Please enter a valid location")
            elif visited[location]==False:
                visited[location]=True
                i=(location-1)//3
                j=(location-1)%3
                d+=1
#                 print(d)
                return userA(a,i,j,d,name1,name2)
def makecross(a):
    h=1
    d=0
    print("Enter Your Name")
    name1=input()
    print("Enter the second player name")
    name2=input()
#     print(a)
    while h==1:
        location=int(input())
        if location<0 or location>9 or visited[location]==True:
            print("Please enter a valid choice")
        elif visited[location]==False:
            visited[location]=True
            i=(location-1)//3
            j=(location-1)%3
            d+=1
#             print(a)
#             print(d)
            for m in a:
                for n in m:
                    print(n,end=" ")
                print()
            return userA(a,i,j,d,name1,name2)
visited={}
for i in range(1,10):
    visited[i]=False
a=[[" " for i in range(3)] for j in range(3)]
print("Welcome to 0, X game")
print(" You can give the location from the following option where you want to fill your value ")
for i in range(1,10):
    print(i,end=" ")
    if i%3==0:
        print()
makecross(a)