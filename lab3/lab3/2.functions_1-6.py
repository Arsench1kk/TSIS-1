#ex1 
gram = float(input()) 
def ounce(x): 
    return 28.3495231 * x 
print(ounce(gram)) 
 
#ex2 
Fahrenheit = float((input())) 
def temperature(x): 
    return (5/9) * (x - 32)  
print(temperature(Fahrenheit)) 
#ex3 
def prime(n): 
    if n <= 1: 
        return False 
    for i in range(2, int(n ** 0.5) + 1): 
        if n % i == 0: 
            return False 
    return True 
 
def filter_prime(numbers): 
    return [num for num in numbers if prime(num)] 
 
 
numbers = [int(x) for x in input("Введите числа, разделенные пробелами:").split()] 
prime_numbers = filter_prime(numbers) 
print("Prime numbers:", prime_numbers) 
 
#ex4 
def reverse(sentence): 
    words = sentence.split()   
    reversed_words = reversed(words)   
    reversed_sentence = ' '.join(reversed_words)   
    return reversed_sentence 
 
words = input("Введите предложение: ") 
reversed_sentence = reverse(words) 
print("Предложение с перевернутыми словами:", reversed_sentence) 
 
#ex5 
def has_33(nums): 
    for i in range(len(nums) - 1):   
        if nums[i] == 3 and nums[i + 1] == 3:  # проверяем число = 3 или след число 3  
            return True 
    return False   
 
print(has_33([1, 3, 3]))    # Output: True 
print(has_33([1, 3, 1, 3]))  # Output: False 
print(has_33([3, 1, 3]))     # Output: False 
 
#ex6 
def spy_game(nums): 
    zero = 0 
    seven= 0 
     
    for num in nums: 
        if num == 0: # num =0 zero=+1 
            zero += 1 
        elif num == 7:  
            seven += 1 
            # Если мы уже встретили два нуля и одну семерку, возвращаем True 
            if zero >= 2 and seven >= 1: 
                return True 
    return False 
 
print(spy_game([1,2,4,0,0,7,5]))   
print(spy_game([1,0,2,4,0,5,7]))   
print(spy_game([1,7,2,0,4,5,0]))