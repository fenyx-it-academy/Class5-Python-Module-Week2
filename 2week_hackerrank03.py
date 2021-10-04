if __name__ == '__main__':
    records = []
    puan = []
    siralama = []
    for i in range(int(input())):
        name = input()
        score = float(input())
        records.append([name,score])
        puan.append(score)
    puan2e = sorted(set(puan))[1]
    for x in range(len(puan)):
        if records[x][1] == puan2e:
            siralama.append(records[x][0])
    for sira in sorted(siralama):
        print(sira)