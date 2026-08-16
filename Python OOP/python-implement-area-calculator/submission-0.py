import math

class AreaCalc:
    # TODO: Implement calculate method
    def calculate(self, *arg):
        if len(arg) == 1:
            n = math.pi * arg[0] ** 2
            return round(n, 2)
            
        return arg[0] * arg[1]
    

    
# Don't modify the following code
calc = AreaCalc()
print(calc.calculate(5))    
print(calc.calculate(4, 6))
