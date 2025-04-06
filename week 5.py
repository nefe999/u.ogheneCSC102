def printme(str):
    #This is a function
    print(str);
    return;

printme("I'm first call to user defined function!");
printme("Again second call to same function");

def changeme(mylist):
    #This changes a passed list
    mylist.append([1,2,3,4])
    print("Values inside the function: ", mylist)
    return
mylist = [10,20,30]
changeme(mylist)
print("Values outside the function: ", mylist)

def printme(str):
    #This is a string 
    print(str);
    return;
printme(str = "My string");

def printinfo(name, age):
    #Test function
    print("Name: ", name);
    print("Age: ", age);
    return;
printinfo(age= 18, name="nefe");

def printinfo(name, age= 20):
    #Test function 
    print("Name: ", name);
    print("Age: ", age);
    return;
printinfo(age= 50, name= "nefe");
printinfo(name= "nefe");
 
def printinfo(arg1, *vartuple):
    #This is test 
    print("Output is: ")
    print(arg1)
    for var in vartuple:
        print(var)
        return;
printinfo(10);
printinfo(70,60,50);

total = 50; #This is global variable
def sum(arg1, arg2):
    #Add both the parameters
    total= arg1 + arg2;
    print("Inside the function loccal total : ", total)
    return total;
#Now you can call sum function 
sum(10, 20);
print("Outside the function global total : ", total)
 
def swap(x, y):
    global a
    a = "Ufuoma"
    x,y = y,x
    b = "Nefe"
    b = "Oghene"
    c = "Ochuko"
    print(a,b,x,y)
    a = "Peace"
swap("James","John")
print(a)