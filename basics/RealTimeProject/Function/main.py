from function import add , ready ,done

def coffee(coffee,c1 ,c2):
    c1(coffee)
    print(f"Im drinking my {coffee}")
    c2(coffee)

if __name__ == "__main__":
    print(add(1,3))
    coffee("Latte",ready,done)
