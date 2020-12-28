

def main(n):
    r = 1
    while n > 0:
        r*=n
        n=n-1
    return r

if __name__ == '__main__':
    print(main(10))
    print(main(3))
    print(main(5))
