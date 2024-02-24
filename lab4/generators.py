#ex1
def Generate(n):
    for i in range(1, n + 1):
        yield i**2

num = int(input())
for square in Generate(num):
    print(square, end = " ")

#ex2
def Generate_Even(n):
    for i in range(n + 1):
        if i % 2 == 0:
            yield i

def main():
    even_num = Generate_Even(n)
    print(*even_num, sep = ", ")

n = int(input())
if __name__ == "__main__":
    main()

#ex3
def Generate(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

n = int(input())
for num in Generate(n):
    print(num)

#ex4
def Generate_square(a, b):
    for i in range(a, b + 1):
        yield i**2

a = int(input())
b = int(input())
for num in Generate_square(a, b):
    print(num)

#ex5
def Generate(n):
    while n >= 0:
        yield n
        n -= 1

num = int(input())
for number in Generate(num):
    print(number)