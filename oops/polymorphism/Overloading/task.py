'''
🧮 Mini Project: "Money" Class – Currency Calculator
💡 Objective:
Create a Money class that represents an amount of money and supports operator overloading for common arithmetic 
and comparison operations.

✅ Features to Implement:
1. Attributes:

class Money:
    def __init__(self, rupees, paise=0):
        ...
2. Overload these operators:
Operator	Purpose
+	Add two Money objects
-	Subtract two Money objects
==	Compare two Money objects
<, >	Compare which money is more
str()	Pretty printing like ₹100.50
*	Multiply money by a number
/	Divide money by a number

🔁 Sample Usage:
m1 = Money(100, 50)     # ₹100.50
m2 = Money(50, 75)      # ₹50.75

print(m1 + m2)          # ₹151.25
print(m1 - m2)          # ₹49.75
print(m1 == m2)         # False
print(m1 > m2)          # True

print(m1 * 2)           # ₹201.00
print(m1 / 2)           # ₹50.25
💡 Extra Challenge (Optional):
Handle paise overflow (e.g., ₹5.150 → ₹6.50).

Handle negative values with a friendly message.

🎓 Skills Practiced:
__add__, __sub__, __eq__, __lt__, __gt__, __str__, __mul__, __truediv__

Value normalization (e.g., 100 paise = 1 rupee)

Defensive programming
'''
class Money:
    def __init__(self, rupees, paise=0):
        total_paise = rupees * 100 + paise
        self.rupees = total_paise // 100
        self.paise = total_paise % 100

    def __normalize(self):
        return self.rupees * 100 + self.paise

    def __str__(self):
        return "₹" + str(self.rupees) + "." + str(self.paise).zfill(2)

    def __add__(self, other):
        total = self.__normalize() + other.__normalize()
        return Money(0, total)

    def __sub__(self, other):
        total = self.__normalize() - other.__normalize()
        if total < 0:
            return "Error"
        return Money(0, total)

    def __eq__(self, other):
        return self.__normalize() == other.__normalize()

    def __le__(self, other):
        return self.__normalize() <= other.__normalize()

    def __gt__(self, other):
        return self.__normalize() > other.__normalize()

    def __mul__(self, value):
        if isinstance(value, (int, float)):
            total = int(self.__normalize() * value)
            return Money(0, total)
        return "Error"

    def __truediv__(self, value):
        if value == 0:
            return "Can't divide by 0"
        if isinstance(value, (int, float)):
            total = int(self.__normalize() / value)
            return Money(0, total)
        return "Error"


# 🔸 Object creation
m1 = Money(10, 30)
m2 = Money(50, 75)

# 🔹 Testing
print(m1 + m2)         # ₹61.05
print(m1 - m2)         # Error
print(m2 - m1)         # ₹40.45
print(m1 == m2)        # False
print(m2 <= m1)        # False
print(m1 > m2)         # False
print(m1 * 2)          # ₹20.60
print(m1 / 2)          # ₹5.15
print(m1 / 0)          # Can't divide by 0
