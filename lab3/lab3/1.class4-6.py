#ex1 
class ttt: 
    def __init__(self): 
        self.rrr="" 
    def getstring(self1): 
        self1.rrr=(input()) 
    def printstring(self): 
        print(self.rrr.upper()) 
 
new=ttt() 
new.getstring() 
new.printstring()   
 
#ex2 
 
x = int(input("square length = ")) 
x1 = int(input("regtangle length = ")) 
y1 = int(input("regtangle width = ")) 
 
class Shape: 
    def __init__(self): 
        pass 
    def area1(self): 
        return 0 
class Square(Shape):  
    def __init__(self,length):  
        super().__init__() 
        self.length = length 
    def area2(self):  
        return self.length * self.length 
class Rectangle(Shape):  
    def __init__(self, length, width): 
        super().__init__() 
        self.length = length 
        self.width = width 
    def area3(self): 
        return self.length * self.width 
 
 
result1 = Shape() 
print(result1.area1()) 
 
result2 = Square(x) 
print(result2.area2()) 
 
result3 = Rectangle(x1,y1) 
print(result3.area3()) 
 
#ex4 
class Point: 
    def __init__(self):  
        self.x = float(input("Enter x-coordinate: ")) 
        self.y = float(input("Enter y-coordinate: ")) 
     
    def show(self):  
        print("Coordinates: ({}, {})".format(self.x, self.y)) 
     
    def move(self, dx, dy):   
        self.x += dx 
        self.y += dy 
     
    def distance(self, other_point): 
        dx = self.x - other_point.x  
        dy = self.y - other_point.y  
        distance = (dx ** 2 + dy ** 2) ** 0.5 
        return distance 
 
 
print("Enter coordinates for point 1:") 
point1 = Point() 
 
print("Enter coordinates for point 2:") 
point2 = Point() 
 
point1.show() 
point2.show() 
 
print("Distance between the two points:", point1.distance(point2)) 
 
 
dx = float(input("Enter move x-coordinate: ")) 
dy = float(input("Enter move y-coordinate: ")) 
point1.move(dx, dy) 
point1.show() 
 
#ex4 
class BankAccount: 
    def __init__(self, owner, balance=0): 
        self.owner = owner 
        self.balance = balance 
     
    def deposit(self, amount): 
        if amount > 0: 
            self.balance += amount 
            print("Deposited $" + str(amount) + ". New balance: $" + str(self.balance)) 
        else: 
            print("Неверная сумма депозита. Сумма должна быть больше нуля.") 
     
    def withdraw(self, amount): 
        if amount > 0: 
            if amount <= self.balance: 
                self.balance -= amount 
                print("Withdrew $" + str(amount) + ". New balance: $" + str(self.balance)) 
            else: 
                print("Недостаточно средств. Сумма вывода превышает доступный баланс") 
        else: 
            print("Неверная сумма вывода. Сумма должна быть больше нуля.") 
 
 
owner = input("Enter owner's name: ") 
initial_balance = float(input("Enter initial balance: ")) 
 
 
account = BankAccount(owner, initial_balance) 
 
 
while True: 
    print("\nChoose an operation:") 
    print("1. Deposit") 
    print("2. Withdraw") 
    print("3. Exit") 
    choice = input("Enter your choice (1/2/3): ") 
 
    if choice == '1': 
        amount = float(input("Enter deposit amount: ")) 
        account.deposit(amount) 
    elif choice == '2': 
        amount = float(input("Enter withdrawal amount: ")) 
        account.withdraw(amount) 
    elif choice == '3': 
        print("Exiting program.") 
        break 
    else: 
        print("Неверный выбор. Пожалуйста, введите 1, 2 или 3.") 
 
#ex6 
def prime(n): 
    if n <= 1: 
        return False 
    for i in range(2, int(n**0.5) + 1): 
        if n % i == 0: 
            return False 
    return True 
 
numbers = [2, 3, 4,5, 6,7, 8, 9, 11, 13, 17, 19, 23, 29, 31 , 52] 
 
 
prime_numbers = list(filter(lambda x: prime(x), numbers)) 

print("Prime numbers:", prime_numbers)