# List Comprehensions
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    print(list([[i,i2,i3]for i in range(x+1) for i2 in range(y+1) for i3 in range(z+1) if i+i2+i3!=n]))

# Tuples
if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    t = tuple(integer_list)
    print(hash(t))
# t=(1,2)
# print(hash(t))

#Nested Lists
if __name__ == '__main__':
    list1=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        list1.append([name,score])
    a= sorted(list({k for i,k in list1}))[1]
    list2=[]
    for i,x in list1:
        if x==a:
            list2.append(i)
    list2.sort()
    print(*[i for i in list2],sep="\n")

