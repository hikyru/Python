while True:
    try:
        n = list(input())
        n.reverse()
        n = "".join(n)
        print(int(n))
    except:
        break