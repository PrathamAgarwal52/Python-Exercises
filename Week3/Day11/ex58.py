if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
mylist=[[i,j,k] for i in range(0,x+1) for j in range(0,y+1) for k in range(0,z+1)]
mynewlist = [[i,j,k] for [i,j,k] in mylist if i+j+k != n ]
print(mynewlist)
