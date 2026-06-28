if __name__ == '__main__':
    n = int(input("enter the value:"))
    arr = map(int, input("enter the scores:").split())
    unique_scores = sorted(list(set(arr)))
    print(unique_scores[-2])
