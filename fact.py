
n = int(input("enter a number: "))

b = n-1

def main():
    global n
    global b
    if b > 0:
        n *= b
        b -= 1
        main()

main()
print(n,"is the factorial")
