liste = []
secondnames = []
scores = set()

for _ in range(int(input())):
    name = input()
    score = float(input())
    liste.append([name, score])
    scores.add(score)
        
secondlowest = sorted(scores)[1]

for name, score in liste:
    if score == secondlowest:
        secondnames.append(name)

for name in sorted(secondnames):
    print(name, end='\n')