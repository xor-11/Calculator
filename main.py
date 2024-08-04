from kivy.graphics import Canvas
from kivy.uix.screenmanager import Screen
from math import sin,cos,tan,pi,asin,acos,atan
from kivymd.app import MDApp
import kivymd
from kivy.app import App
from kivy.properties import StringProperty, BooleanProperty
from kivy.uix.stacklayout import StackLayout
from kivymd.uix.textfield import MDTextField
from kivy.config import Config

Config.set('graphics', 'resizable', True)

class cv(Canvas):
    pass
class Calculator(StackLayout):
    display = StringProperty("")
    a = BooleanProperty(True)


    def arcsin(self):
        self.display += "asin("
    def arccos(self):
        self.display += "acos("
    def arctan(self):
        self.display += "atan("


    def special(self):
        if self.a == False:
            self.a = True
            print(self.a)

        elif self.a == True :
            self.a = False
            print(self.a)

    def pi(self):
        self.display += "pi"

    def dot(self):
        self.display += "."

    def tan(self):
        self.display += "tan("
    def cos(self):
        self.display+= "cos("
    def sin(self):
        self.display += "sin("

    def rightb(self):
        self.display += ")"




    def exp(self):
        self.display += "**"

    def factors1(self,widget):
        self.display = ""
        def divisors(a):
            l = []
            for i in range(1, int((a ** (1 / 2)) + 1)):
                if a % i == 0:
                    l.append(i)
                    l.append(a // i)
            return sorted(set(l))

        try:
            a = int(widget.text)
            self.display = str(divisors(a))
        except:
            self.display = "ERROR"


    def isprime1(self,widget):
        self.display = ""
        def isprime(a):
            if a == 0 or a == 1:
                return False
            if a == 2 or a == 3:
                return True
            if a % 2 == 0 or a % 3 == 0:
                return False
            for i in range(5, int(a ** (1 / 2) + 1), 2):
                if a % i == 0:
                    return False
            return True
        try:
            a = int(widget.text)
            self.display = str(isprime(a))
        except:
            self.display = "ERROR"

    def lcm1(self,widget):
        self.display = ""

        def gcd(a, b):
            if a % b == 0:
                return (b)
            return gcd(b % a, a)
        try:
            a = eval(widget.text)
            b = int(a[0])
            c = int(a[1])
            k = int(b*c/gcd(b,c))
            self.display = str(k)
        except:
            self.display = "ERROR"

    def gcd1(self,widget):
        self.display = ""




        def gcd(a, b):
            if a % b == 0:
                return (b)
            return gcd(b % a, a)
        try:

            a = eval(widget.text)
            b = int(a[0])
            c = int(a[1])
            self.display = str(gcd(b, c))
        except:
            self.display = "ERROR"

    def clear(self):
        self.display = ""

    def backspace(self):
        self.display = self.display[:len(self.display) - 1]

    def b1(self):

        self.display += str(1)

    def b2(self):

        self.display += str(2)

    def b3(self):

        self.display += str(3)

    def b4(self):
        self.display += "+"

    def b5(self):

        self.display += str(4)

    def b6(self):

        self.display += str(5)

    def b7(self):

        self.display += str(6)

    def b8(self):

        self.display += "-"

    def b9(self):

        self.display += str(7)

    def b10(self):

        self.display += str(8)

    def b11(self):

        self.display += str(9)

    def b12(self):

        self.display += "*"

    def b13(self):

        self.display += "("

    def b14(self):

         self.display += str(0)

    def b15(self):
        try:
            self.display = str(eval(self.display))
        except:
            self.display = "ERROR"

    def b16(self):

        self.display += "/"
class CalculatorApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"


CalculatorApp().run()