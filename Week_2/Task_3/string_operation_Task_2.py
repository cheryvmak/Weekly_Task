# Task 2

# Q6.

# enter a string 
word = "I'm enjoying python"
# check if it contain substring 
print("python" in word)

# Q7

# enter a string
a = "Hello"
# reverse a string without using ([::-1])
print(a[-1:-6:-1])

# Q8

# enter a string with extra spaces
name = "    Adeola "
#remove the  leading and trailing lines 
print(name.strip())

# Q9

# enter a sentence using input
clients = input("Enter a sentence: ")

# enter each vowel as variable and count
#vowels = ("aeiouAEIOU")
a = clients.count("a")
e = clients.count("e")
i = clients.count("i")
o = clients.count("o")
u = clients.count("u")
A = clients.count("A")
E = clients.count("E")
I = clients.count("I")
O = clients.count("O")
U = clients.count("U")

# sum all the vowel ina variable 
sum_vowel = a+e+i+o+u+A+E+I+O+U

#print the number of variable in it
print(f"The number of vowel in it: {sum_vowel}")

# Q10

#enter a string
a = "1234"
# type cast to integer
b = (int(a) * 2)
# print the output
print(b)
