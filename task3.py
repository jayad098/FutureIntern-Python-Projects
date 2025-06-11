import random
import string

print("Welcome to the password generator !")
random_letter=set()
random_symbol=set()
random_digit=set()


letter_no =int(input("How many letters would you want in your password ?\n"))
for i in range(letter_no):
    random_letter.add(random.choice(string.ascii_letters) )

symbol_no =int(input("How many symbol would you want?\n"))
for i in range(symbol_no): 
    random_symbol.add(random.choice(string.punctuation))

digit_no =int(input("How many digit would you want?\n"))
for i in range(digit_no): 
    random_digit.add(random.randint(0,9))    

union_result = random_letter.union(random_symbol,random_digit)
result = "".join(map(str, union_result))
print("Your password is: ", result)