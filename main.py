import random
# user input 
how_many_letters = int(input("how many letters?\n>>>   "))
how_many_numbers = int(input("how many numbers?\n>>>   "))
how_many_symbols = int(input("how many symbols?\n>>>   "))


# choose letters
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

password_list = []

for char in range(1, how_many_letters + 1):
  password_list += random.choice(letters)
# print(password_list)


# choose numbers
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

for num in range(1, how_many_numbers + 1):
  password_list += random.choice(numbers)
# print(password_list)


# choose symbols
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

for x in range(1, how_many_symbols + 1):
  password_list += random.choice(symbols) 
# print(password_list)

random.shuffle(password_list)
# print(password_list)

password = ""
for char in password_list:
  password += char
print(f"Your password is...\n\n   {password}\n\n\n")