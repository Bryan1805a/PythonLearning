def fizzBuzz(n):
    res = []

    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            res.append("FizzBuzz")
        elif i % 3 == 0:
            res.append("Fizz")
        elif i % 5 == 0:
            res.append("Buzz")
        else:
            res.append(str(i))
    
    return res

if __name__ == "__main__":
    a = int(input())
    print(" ".join(fizzBuzz(a)))