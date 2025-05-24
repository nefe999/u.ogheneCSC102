1

def find_quadratic_roots(a, b, c):
       # Implement or use np.roots([a, b, c])
       pass

def find_cubic_roots(a, b, c, d):
       # Implement or use np.roots([a, b, c, d])
       pass

def find_quartic_roots(a, b, c, d, e):
       # Implement or use np.roots([a, b, c, d, e])
       pass

def main():
       print("Select the type of equation:")
       print("1. Quadratic")
       print("2. Cubic")
       print("3. Quartic")
       choice = input("Enter your choice (1/2/3): ")

       if choice == '1':
           # Prompt user for a, b, c and call find_quadratic_roots
           pass
       elif choice == '2':
           # Prompt user for a, b, c, d and call find_cubic_roots
           pass
       elif choice == '3':
           # Prompt user for a, b, c, d, e and call find_quartic_roots
           pass
       else:
           print("Invalid choice")


x = 3
y = x - 2 
z = y * x 
y = z - x
x = x * 2 
print(x,y,z)
n = 5
if n> 10:
      if n%2==0:
            result="Even and greater than 10"
      else:
            result="Odd and greater than 10"
else:
      result="5 or below"
if n> 5:
      result="Between 6 and 10"


print(result)


count= 1
for i in range(2,10,2):
      count += i 

def modify_list(my_list):
      my_list.append(4)
      my_list=[7,8,9]
      my_list.append(10)
      return my_list

original=[1,2,3]
modified=modify_list(original)
print(original)
print(modified)

x = 3
y = x - 2 
z = y * x
y = z - x
x = x * 2
print(x)
print(y)
print(z)                                                                                         


age = 25
temperature = -10
zero = 0

print(type(age)) 

pi = 3.14159
height = 1.75
negative_float = -0.5

# Scientific notation
large_number = 1.6e3  # 1600.0
tiny_number = 1.6e-3  # 0.0016

print(type(pi))

quotient = 9.5 / 2.0
print(quotient)

a = round(3.14159, 3)
print(a)
import math
x = math.floor(4.7)  # 4 (rounds down)
y = math.ceil(4.3)  # 5 (rounds up)
z = math.trunc(4.7)  # 4 (truncates decimal part)
print(x,y,z)

w = 0.1 + 0.2
print(w)

# Creating complex numbers
z1 = 2 + 3j  # Direct creation
z2 = complex(2, 3)  # Using complex() function

print(type(z1))  # <class 'complex'>