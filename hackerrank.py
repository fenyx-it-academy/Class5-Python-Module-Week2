#list comprehension
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
print(list([[i,j,k] for i in range(x + 1) for j in range(y+1) for k in range (z+1)    if i+ j+ k!= n]) )

#tuples
if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    t = tuple(integer_list)
    print(hash(t))

#nested list
if __name__ == '__main__':
    list_1=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        list_1.append([name,score])
    a= sorted(list({k for i,k in list_1}))[1]
    list_2=[]
    for i,x in list_1:
        if x==a:
            list_2.append(i)
    list_2.sort()
    print(*[i for i in list_2],sep="\n")