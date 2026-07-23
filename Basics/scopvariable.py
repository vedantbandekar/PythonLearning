# varibale scope = where a variable is visible and accessible 
# scope resolution = (LEGB) Local --> Enclosed -> Gloabl -> Built-in

# varibale scope

#normal function cant see inside each other func1 only knows func1 value not the value of func2 
# def func1 ():
#     a = 1
#     print (a)

# def func2 ():
#     b = 2
#     print (b)

# func1 ()
# func2 ()

#this is how it works now

def func1 ():
    x = 1

    def func2 ():
        x = 2   #this is local function
        print (x)  
    func2 ()

func1 ()

def func1 ():
    x = 1   #this is enclosed function so here since local value is not present it will print this value 

    def func2 ():
        print (x)  
    func2 ()

func1 ()


def func1 ():
    print (x)

def func2 ():
    print (x)  

x = 3 #this is a global function since no local or enclosed function present the code will use global function printing 3 twic once for func1 and another for func2

func1 ()
func2 ()

from math import e

def func1():
    print(e) #local e has a value 

e = 3 #but still prints gobal since it is a built in function from math lib

func1()

