if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    tup_list = tuple(integer_list)
    print(hash(tup_list))