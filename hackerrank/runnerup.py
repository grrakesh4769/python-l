if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    sarr = sorted(list(set(arr)), None, None, True)
    print sarr[1]
