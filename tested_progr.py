

def main(n):
    r = 1
    while n > 0:
        r*=n
        n=n-1
    return r

if __name__ == '__main__':
    print(main(-1))
    print(main(-3))
    print(main(-5))
    print(main(2.2))
    print(main([5,4]))
    print(main("aaaa"))
