class Calculator:
    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b

def multiply(self, a, b):
        return a * b
    
    def divide(self, a, b):
        if b == 0:
            return "Помилка: ділення на нуль!"
        return a / b
def power(self, a, b):
        return a  b
    
    def square_root(self, a):
        if a < 0:
            return "Помилка: від'ємне число!"
        return a  0.5

# Тестовий код
if name == "main":
    calc = Calculator()
    print("Додавання:", calc.add(5, 3))
    print("Віднімання:", calc.subtract(5, 3))
    print("Множення:", calc.multiply(5, 3))
    print("Ділення:", calc.divide(6, 2))
    print("Степінь:", calc.power(2, 3))
    print("Корінь:", calc.square_root(9))

