### List Comprehensions

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    print ([[i, j, k] for i in range (x+1) for j in range (y+1) for k in range (z+1) if i + j + k != n])


### Tuples

if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    
    tup = ()
    for x in integer_list:
        tup += (x,)
    print(hash(tup))


### Nested Lists

list = []
second_lowest_names = []
scores = set ()
 
for x in range (int(input())):
    name = input()
    score = float(input())
    list.append([name, score])
    scores.add(score)

    
second_lowest_names = sorted(scores)[1]

for name, score in list:
    if score == second_lowest_names:
        second_lowest_names.append(name)

for name in sorted(second_lowest_names):
     print(name, end='\n')
