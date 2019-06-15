import re 
from time import sleep

class function():
    def __init__(self, a, power, b, c):
        self.a = int(a)
        self.b = int(b)
        self.c = int(c)
        self.power = int(power)
    def calc(self, x):
        return self.a*x**self.power + self.b*x + self.c
    def derivative(self, x):
        return self.power*self.a*x**(self.power-1) + self.b

raw_function = input("Enter the function rearranged so it equals 0    ")

#pull out every thing before the power symbol and before the x
a = raw_function.split("^")[0].split("x")[0]
#pull out everythhing after the power symbol and before the next +/-
power = re.split(r"(\+|-)",raw_function.split("^")[1])[0]
#pull out the the first +/- and everything after the first +/- but before the next x
b = re.split(r"(\+|-)", raw_function)[1]+re.split(r"(\+|-)", raw_function)[2].split("x")[0]
#pull out the the second +/- and everything after the second +/-
c = re.split(r"(\+|-)", raw_function)[3]+re.split(r"(\+|-)", raw_function)[4]

#creates a function with the numbers we just pulled out
func = function(a, power, b, c)

x = float(input("Enter the starting value for x    "))
while True:
    adjustment = (func.calc(x)/func.derivative(x))
    if adjustment == 0:
        break
    else:
        x -= adjustment
        print(x)
    sleep(0.1)
