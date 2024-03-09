def hello_world():
    print("Hello, World")

def foo():
    if(9 < 7):
        print("Denne er innstengt 10hi!")
    else:
        print("Denne er ikke innestengt. Også kalt ei utestengt. HEI MARTIN .... beep boop")
        print("Hei Julie! Kan du følge med???")

    i = 0
    while(True):
        print("Hei VERDEN")
        i += 1
        if(i > 10):
            break

def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print("SHEESH")

def main():
    hello_world()
    print("Hei Julie!")
    print("kan du følge med???")

if __name__ == "__main__":
    main()
