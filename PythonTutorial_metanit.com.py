#1 "save as" → utf-8
'''name = input("Введите имя: ")
print ("Привет, ", name)'''

#2  TAB or 4 SPACEs
#   Print != print
#   () is not necessary everywhere, same as ';' 
from asyncio import selector_events
from logging import exception
from operator import index
from telnetlib import X3PAD
from tkinter import TRUE
from xml.sax.handler import property_declaration_handler


if (1 > 2):
    print ("1 is more than 2");

if 1 > 2:
    print ("1 is more than 2")

print ("1 isn`t more than 2")

#3 commentaries
'''
extensive commentary
your advertising could be here'''

#OFFTOP pampering with types in "print (..)"
null=0.0100
first =1
second= "second"
sum = null + first # + second -- EXCEPTION float vs str

print ("null is", null, ", first =", first,", second)", second,"\nsum — ", sum)
# spaces between "print" parameters spelled automatically,no need to add it manually

#4  variables
''' python key words

    False      await      else       import     pass
    None       break      except     in         raise
    True       class      finally    is         return
    and        continue   for        lambda     try
    as         def        from       nonlocal   while
    assert     del        global     not        with
    async      elif       if         or         yield

'''

#   denomination types: camel case AND underscore notation
camelCase = "camelCase"
underscore_notation = "underscore_notation"
#register
Name = "Tom"
name = "tom"

#5 types, basic are bool, int, float, complex, str
#   int
a = 0b1001      # binary
b = 0o12        # octal
c = 0x0B        # hexadecimal
print (a,b,c);  # 9 10 11

#   complex

   
#   explicit initializing
bull : bool = False
a : int = 9
c = 12e-1
print (a,c)
#OFFTOP pampering with types in "print (..)" (2)
d = 8.05300
D = 8e0
_d =8.e0
_D =8.
print ("\nd, D, _d TYPES (different float variables spelling):", type(d), type(D),type(_d))
print ("\nTypeCastIng to float, int, bool, str:", float(d), int(d), bool(d), str(d))


#КОНСОЛЬНЫЙ ВВОД И ВЫВОД

name = 'tom'
NAME = "TOM"
print ("\n\' or \" in str initialization — doesn`t matter: ", name, NAME)

#   different spelling of a text in PRINT
a_letter = ("Lorem ipsum dolor sit amet, "            "consectetur adipiscing elit, "
'sed do eiusmod tempor incididunt '
"ut labore et dolore magna aliqua. "

)
a_poem = '''
The innkeeper began to tell me about
    That the forces of Evil put a curse on them,

Sending a messenger to them with horns and a tail!


'''
print (a_letter, '\n',a_poem)
print ('''\' is not what you thinked \ n\n''')

path = (r'C:\python\name.txt')  # using "r' allows ignoring of control characters like  \n [line feed]
userName = 'Tom'
userAge = 37
user = f'name {userName}, age: {userAge}'

print     (path, "\t", user, end = '\tqwerty')

'''
userName = input("\nВведите ваше имя:_")
userAge = input("Введите ваш возраст:_")
print(f"Ваше имя {userName}, тип значения {type(userName)},"
      f" а возраст -- {userAge}, тип значения {type(userAge)}")
'''

#АРИФМЕТИЧЕСКИЕ ОПЕРАЦИИ С ЧИСЛАМИ

a = 4
b = a/3
print (a +b - b**a) # ** = ВОЗВЕДЕНИЕ В СТЕПЕНЬ

print (7//2) #ЦЕЛОЧИСЛЕННОЕ ДЕЛЕНИЕ (div)
print (7%2) #ОСТАТОК ОТ ДЕЛЕНИЯ (mod)
# += et al работает как на C++


#ОКРУГЛЕНИЕ
print(2.0001 + 0.1) #2.101000000000000000003
print(round(2.0001 + 0.1 , 4)) #2.11

#round без второго параметра округляет до ближайшего (2.51 = 3)
#                                   или до ближайшего четного (2.5 = 2)
print(round(2.555,2))


#ОПЕРАТОРЫ
x = 3
y = 2
b = y and x # если оба true, то возвращается последний операнд

age = 38
weight = 77
result = age > 21 and weight == 77
print(b,type(b),result)

# or -- возвращает первый операнд в случае его True, иначе возвращает второй
#not -- логическое отрицание
# in -- проверка наличия вхождений строки А в строке Б

print (0 or [12389], '\n')


#УСЛОВНАЯ КОНСТРУКЦИЯ
if a>1:
    
        print (c,b,a)
        print (b-a)
        print (c-b-a)
        if b>1:
            print (b)


elif b>1:
    print (c)

else:
        print(b)
print(result if a>b else c)

x = 3
y = 4
z = 5
print(x if (not x)+ y * z else y) #x
print(x if  not x + y * z else y) #y


#ЦИКЛЫ
while x>=0:
    print(f"икс равен {round(x,5)}")
    x-=0.31
else:
    print(f"икс меньше нуля и равен {round(x,5)}. Это последнее предупреждение")

for x in range(1,5):
    print(x,end='\t')
    newVariable=5.5
else:
    print(newVariable)
# BREAK and CONTINUE is mutual to same operators in C++


#ФУНКЦИИ
def first_func():
    print ("\n\tфункция\n")
    def inserted_func():    #видна только внутри first_func
        print("вложенная функция")  
    def alt_inserted_func(): print("альтернативная вложенная функция")
                            #можно писать иначе
    inserted_func()
    alt_inserted_func()

first_func()

def say_hello(name, age = 18):  #параметр по умолчанию, если age == null
    print(f"Hello, {name}")   #необязательные параметры идут всегда после обязательных
say_hello("Bob")    #будет использован параметр возраста по умолчанию
say_hello("Tom", 19)

#   ИМЕНОВАННЫЕ ПАРАМЕТРЫ (передача значений параметрам по имени)
def print_person(name, age):
    print(f"Name: {name}  Age: {age}")
print_person(age = 22, name = "Tom") #польза -- можно менять порядок
                          #параметров и читателю становится понятнее

def print_person(name, *,  age, company):   # '*' относится к age и company -
                                            # - обязательное именование
    print(f"Name: {name}  Age: {age}  Company: {company}")

print_person("Bob", age = 41, company ="Microsoft")

# ПОЗИЦИОННЫЕ ПАРАМЕТРЫ (параметры, которые привязаны не к имени, а к позиции)
def print_person(name, /, age, company="Microsoft"):# '/' относится к name
    print(f"Name: {name}  Age: {age}  Company: {company}")# удобно ориентироваться по положению
print_person("Tom", company="JetBrains", age = 24)
print_person("Bob", 41)

# Неопределенное количество параметров
def sum(*numbers):  #с помощью '*' создаётся итерируемый список
    result = 0
    for n in numbers:   # я же сказал, итерируемый
        result += n
    print(f"sum = {result}")
    
    return result    # тип функции определяется автоматически, как и с переменной, ох уж этот питон
    qwerty=3         # повторение -- мать учения
    йцукен:int =4    # ух ты, можно кириллицей!

sum(1, 2, 3, 4, 5)      # sum = 15
sum(3, 4, 5, 6)         # sum = 18

sum41 = sum(40, 1)
def double(number):
    return number * 2
print("sum 40, 1 = ",double(sum41))

def print_person(*,age=13, name):
    if(age>120) or (age<0):             #красивая обработка исключений
        print(f"{age} ← invalid age")
        return 1                        #по-хорошему потом по коду ошибки надо выводить описание
    print(f"Name:{name}, age:{age}")

print_person(name="Федор", age=24)      #normal
print_person(name="Feudor", age=243)    #   exception

#   ФУНКЦИЯ КАК ПЕРЕМЕННАЯ
def func1(): print("первая функция-переменная")
def func2(): print("вторая функция-переменная")

undefinited_func = func1
undefinited_func();
undefinited_func = func2
undefinited_func();

def func3(function, str):
    print(f'''результат работы функции{undefinited_func()}
          "Введённая строка: {str}''')


def do_operation(a,b,operation):
    print(f"результат операции с функцией в качестве параметра: {operation(a,b)}")
    return operation(a,b)
def exponentiation(a,b):        return a**b

def multiply(a,b):    return a*b
def sum(a,b): return a+b

print(do_operation  (  2,3,exponentiation))
print(do_operation(2,3,multiply))

# возврат функции в качестве результата
def select_operation (choice):
    if   choice == "sum":           return sum
    elif choice == "exponentiation":return exponentiation
    elif choice == "multiply":      return multiply
    else: return 1

print(do_operation(2,3, select_operation("sum"))) # 5


# ЛЯМБДА-мать их-ВЫРАЖЕНИЯ -- анонимные функции, т.е. без def и соотв конструкции
# иными словами, лямбда-выражение, это функция, мимикрирующая под переменную
# де-факто это синтаксический сахар, упрощённая запись функции в-одну-строку как переменной
message1 = lambda: print("hello")
def message2(): print("hello")
#message1 и message2 равнозначны, но при этом
message1()
message2()
print(message1==message2)     # False
print(message1()==message2()) # True

sum = lambda a, b: a + b
print(sum(4,5))

ssum = lambda a,b,c: a+b*c

#Лямбда-функцию можно сразу впихивать параметром
do_operation(2.1,33,lambda b,a:round (a**b ,2))



#   ОБЛАСТЬ ВИДИМОСТИ ПЕРЕМЕНЫХ
# global
age = 0
def some_function_global():
    global age          # используем глобальную переменную
    age = 1
    print(age, end='\t')


def some_function():
    age = -1            # скрываем значение глобальной переменной
    print(age, end='\t')

print(age)
some_function()
print(age)
some_function_global()
print(age)

# local
a = 2
b = 0
def some_function_():
    global a
    if a > 0:
        a = 0       # в IF используется та же переменная
    print(a)

some_function_()
print (a)
print("------------------------")

def some_function__():
    global a
    a=3
    def inner_function():
        message1        # нельзя использовать nonlocal для global ранее
    inner_function()
    print(a)

some_function__() # 3
print (a) # 3

def some_function_local():
    a=2
    def inner_function():
        nonlocal a
        a=-2
    inner_function()
    print (a)

some_function_local()
print (a)

# разобрались с global и nonlocal


# ЗАМЫКАНИЯ (closure) -- функция, всегда запоминающая своё окружение. 
#   Состав:
    # внешняя функция с областью видимости
    # переменные и параметры внешней функции
    # вложенная функция, котрая использует окружение внешней
        # окружение -- это внешние для функции переменные и параметры
def outer():
    n=5
    def inner():
        nonlocal n
        n+=1
        print(n)
    return inner

fn = outer()   # здесь - следите за руками - мы присвоили Результат работы
fn() # 6       # outer, т.е. inner с nonlocal n (не определённым заранее),
fn() # 7       # т.е. fn сохраняет изменённое n.
fn() # 8       # В итоге fn является Замыканием, т.е. объединяет функцию
               # и окружение, в котором функция была создана

# применение параметров окружающей фукнции ко внутренней
def outer(a):
    def inner(b): return a * b
    return inner        # двойной ретурн даёт право и обязанность
                        # использования двойных скобок (см. снизу)

# или при помощи лямбда-выражений, но надо быть аккуратным с параметрами
def outer_alt(a):return lambda a: a*b
                       
par_a=45
par_b=3
fn = outer(par_a)
print(fn(par_b)) # 135
#   или так:
c = outer(par_a-30)(par_b+1)
print(c)         # 15 * 4 = 60


# ДЕКОРАТОРЫ
def decor_square(some_func):
    def lzhedmitry(*params):
        print("-------------")
        print( some_func(*params)**2 )  # круто!
        print("-------------")  # И беды не будет, ибо количество 
    return lzhedmitry           # параметров дублируется в зависимости от функции

@decor_square
def sum_of_two(a,b): return a+b

print(sum_of_two(2,3)) # 25



# КЛАССЫ, ОБЪЕКТЫ
class NullClass:
    pass    # значение по умолчанию, если ничего не придумано
nullObject = NullClass()   # определение объекта класса через конструктор

class MyClass():
    def __init__(self, name): # конструктор определяется через __init__; может быть только один
        self.name = name    #аттрибуты определяются через конструктор автоматически
        self.age = 68       # все аттрибуты должны быть явно определены в нём

    def print_yourself(self):   # функция определяется как метод через def и
        print (f"my name is {self.name}, {self.age} years old") # передачу self (аналог this)

myself = MyClass("Warren")
myself.print_yourself()

myself.dynamicAttr = "bastard"  # динамическое создание аттрибута вне класса
print(myself.dynamicAttr)   # инкапсуляция OFF, читай далее


# ИНКАПСУЛЯЦИЯ, АТРИБУТЫ, СВОЙСТВА. 
# раскидаем понятия:
    # инкапсуляция -- способ работы с атрибутами только через методы
    # атрибут = поле; сделать аттрибут приватным -- добавить ему в начале "__" 
    # методы, вытаскивающие приватные атрибуты из класса -- акцессоры/геттеры

class RightClass(): # а что может быть в скобках помимо void?
    def __init__(self,_name, _age):
        self.__age=_age
        self.__name=_name
        pass
    
    def get_age(self):
        return self.__age   # это называется геттер или аксессор
    # отличие свойства от метода?
    def set_age(self, _age): # метод называется сеттер или mutator
        if 0 < age < 150:
            self.__age = _age
        else:
            print("Недопустимый возраст")

    def set_name(self, _name):
        if _name != '':
            self.__name = _name
        else:
            print("Имя не должно быть пусто")
    def get_name(self):
        return self.__name

    def display_info(self):
        print(f"Имя: {self.__name}, возраст: {self.__age}")

print("\nВключаем инкапсуляцию, пишем правильный класс")
item = RightClass("Victor", 34)
item.display_info()
item.set_age(36)
item.display_info()

# Аннотации свойств (ещё один сахар) 
# через @property созадётся свойство-геттер
# через имя_свойства_геттера.setter создаётся сеттер
class RightClass():
    def __init__(self,_name, _age):
        self.__age=_age
        self.__name=_name
        pass
    
    @property   #геттер
    def age(self):
        return self.__age
    
    @age.setter #сеттер
    def age(self, _age):
        if 0 < age < 150:
            self.__age = _age
        else:
            print("Недопустимый возраст")

    @property
    def name(self):
        return self.__name
    
    @name.setter    #сеттер не может быть написан раньше геттера
    def name(self, _name):
        if _name != '':
            self.__name = _name
        else:
            print("Имя не должно быть пусто")
    
    def display_info(self):
        print(f"Имя: {self.__name}, возраст: {self.__age}")
    
    def do_nothing(self):
        print (f"{self.name} do nothing")
        

print("\nВключаем @property и @[setter_name].setter у правильного класса")
item = RightClass("Victor", 34)
item.display_info()
item.age = 36
print(item.age)
item.display_info()
print()
print("Теперь мы умеем обращаться и к геттеру, и к сеттеру возраста "
      "через item.age")


# НАСЛЕДОВАНИЕ 
# суперкласс называется базовым классом (base class, parent class), 
# подкласс -- производный или дочерний (derived or child class)
class UltraRightClass(RightClass):
    pass
    def work(self):
        print(f"{self.name} works")
      #  print(f"{self.__name} works") # будет ошибка, методы дочернего 
      # элемента не могут обращаться к атрибутам родительского

person = UltraRightClass("Tom", 33)
person.display_info()
person.work()
print()

class UltraLeftClass (RightClass):
    def study(self): print (f"{self.name} studies")
    # множественное наследование
class UltraCenterClass(UltraRightClass, UltraLeftClass):
    pass

person = UltraCenterClass("Viktor", 78)
person.display_info()
person.work()
person.study()
print()


# Переопределение функционала базового класса
class UltraRightClass(RightClass):
    def __init__(self,_name, _age, _company): # взяли конструктор базового класса, 
        super().__init__(_name, _age)         # де-факто вытянули аттрибуты из него
        self.company = _company               # и дополнили их

    def display_info(self):
        super().display_info()  # аналогично поступили тут с методом
        print(f"company: {self.company}")

    def work(self):
        print(f"{self.name} works")
    
person = UltraRightClass("Tom", 35.5, "necroSoft")
person.display_info()
print()


# Проверка типа объекта
a: bool
b: bool
a= type(person) == UltraRightClass
b= isinstance(person, UltraRightClass)
print(a,'\t',b)

def action_alt(_person):
    if type(_person) == UltraRightClass:
        _person.work()
    elif type(_person) == UltraLeftClass:
        _person.study()
    elif type(_person) == RightClass:
        _person.do_nothing()
    print()

def action_right(_person):
    if isinstance(_person, UltraRightClass): # зачем нам insistance, если есть type?
        _person.work()
    elif isinstance(_person, UltraLeftClass):
        _person.study()
    elif isinstance(_person, RightClass):
        _person.do_nothing()
    print()

action_alt(person)
action_right(person)

person1 = RightClass("RC", 30)
person2 = UltraRightClass("URC", 31, "MMA")
person3 = UltraLeftClass("ULC", 32)

action_right(person1)
action_right(person2)
action_right(person3)



# АТРИБУТЫ КЛАССА (не путаем с атрибутами объекта)
class Person:
                        # атрибуты класса определяются непосредственно в нём,
                        # а не в конструкторе, как это было с атрибутами объекта
    type = "Person"     #*type, sum -- имеют свои значения, поэтому светят синим
    description = "Describes a person"
    third_attrib = 3    # нельзя не определять

#   видимость работает так же, как и с атрибутами объекта, через "__"
print(Person.type)
print(Person.description)
Person.type = "Class Person"
print(Person.type)
print()

# пример полезности
class DefaultClass:
    defaultName = "here is no name"
    def __init__(self, _name):
        if _name:           # делаем проверку, не пусто ли имя
            self.name = _name
        else: self.name = DefaultClass.defaultName

class SecondDefaultClass:
    name = "Undefined"
    __type = "SecondDefaultClass"

    @staticmethod       # метод, независимый от объекта; зачем здесь аннотация вообще?
    def print_type():
        print(SecondDefaultClass.__type)

    def print_type_alt(self): # ведь можно написать так и проблем не будет, см ↑↑
        print(SecondDefaultClass.__type) # разве что его нельзя использовать без инициализации объекта


    def print_name(self):
        print(self.name)

person4 = SecondDefaultClass()
person5 = SecondDefaultClass()
person4.print_name()
person5.print_name()
person4.name = "Bob"
person4.print_name()
person5.print_name()
print()

person4.print_type()
person4.print_type_alt() # это вопрос архитектуры и видимости, не более
print()

# Класс object. Строковое представление объекта
# начиная с 3 версии python все классы являются наследниками object
class Person:
    def __str__(self):      # наиболее используемый метод класса object,
        str_:str
        str_ = str(super.__str__(self)) # выводи строковое представление объекта;
        return f"name: {self.name}, age:{self.age}" # надо переопределить

    def __init__(self, _name, _age):
        self.name = _name
        self.age = _age
        pass

    def display_info(self):
        print(f"name: {self.name}, age: {self.age}")
        pass
    pass

tom = Person("tom", 23)
print (tom)
tom.display_info()

print (print(tom) == tom.display_info()) # True
print()



# ОШИБКИ ВЫПОЛНЕНИЯ -- ИСКЛЮЧЕНИЯ
'''
try:
    numeric = int(input ("Введите целое число: "))
    print (f"Введённое число: {numeric}")
except:     #ValueError:      #аналог catch
    print ("Ошибка: введено не число")
finally: # выполняется в любом случае, как правило тут высвобождаются ресурсы
    print("Блок try завершил выполнение")
print ("Завершение работы программы")

def func():
    try:
        print ("hello")
        return      # блок finally выполняется в любом случае
    except:
        print("ошибка ввода hello")
    finally:
        print ("world")
        pass
    pass
func()
print()

# Встроенные типы исключений
try:
    numeric = int(input ("Введите целое число: "))
    print (f"Введённое число: {numeric}")
except ValueError:
    print ("Ошибка: введено не число")
finally:
    print("Блок try завершил выполнение")
print ("Завершение работы программы\n")
'''


# базовые типы исключений Python 
'''
 • BaseException: базовый тип для всех встроенных исключений
 • Exception: базовый тип, который обычно применяется для создания 
       своих типов исключений
 • ArithmeticError: базовый тип для исключений, связанных с 
       арифметическими операциями (OverflowError, ZeroDivisionError, 
       FloatingPointError).
 • BufferError: тип исключения, которое возникает при невозможности 
       выполнить операцию с буффером
 • LookupError: базовый тип для исключений, которое возникают при 
       обращении в коллекциях по некорректному ключу или индексу 
       (например, IndexError, KeyError)

Перечислю только некоторые наиболее часто встречающиеся:
    IndexError: исключение возникает, если индекс при обращении к элементу 
коллекции находится вне допустимого диапазона
    KeyError: возникает, если в словаре отсутствует ключ, по которому 
происходит обращение к элементу словаря.
    OverflowError: возникает, если результат арифметической операции 
не может быть представлен текущим числовым типом (обычно типом float).
    RecursionError: возникает, если превышена допустимая глубина рекурсии.
    TypeError: возникает, если операция или функция применяется к значению 
недопустимого типа.
    ValueError: возникает, если операция или функция получают объект 
корректного типа с некорректным значением.
    ZeroDivisionError: возникает при делении на ноль.
    NotImplementedError: тип исключения для указания, что какие-то 
методы класса не реализованы
    ModuleNotFoundError: возникает при при невозможности найти модуль 
при его импорте директивой import
    OSError: тип исключений, которые генерируются при возникновении 
ошибок системы (например, невозможно найти файл, память диска заполнена 
                и т.д.)
'''

# пример с разными исключениями
'''
try:
    number1 = int(input("Введите первое Целое число: "))
    number2 = int(input("Введите второе Целое число: "))
    print ("результат деления первого числа на второе \n", number1/number2)

except (ValueError,ZeroDivisionError): # а можно и так
    print ("попытка делить на ноль или некорректный ввод")

except ValueError:
    print("ошибка ввода; введено не целое или не число")
except ZeroDivisionError:
    print("нельзя делить на ноль")

except BaseException as e:      # всегда (ли?) нужен, чтобы прога не вылетала
    print("неизвестная ошибка: ", e)

finally: print ("Завершение работы программы\n")
'''

# ГЕНЕРАЦИЯ ИСКЛЮЧЕНИЙ И СОЗДАНИЕ СВОИХ ТИПОВ ИСКЛЮЧЕНИЙ
'''
try:
    number1 = int(input("Введите первое Целое число: "))
    number2 = int(input("Введите второе Целое число: "))
    if number2 == 0:
        raise Exception("Второе число не должно быть равно 0") 
        # выдача внеочередного исключения Exception (BaseException)

    print ("результат деления первого числа на второе \n", number1/number2)

except ValueError:
    print("ошибка ввода; введено не целое или не число")

except BaseException as e:
    print("неизвестная ошибка:\n", e)

finally: print ("Завершение работы программы\n")
'''

class Person:
    def __init__(self, _name, _age):
        self.__name = _name
        minAge_, maxAge_ = 0, 150
        if minAge_ <= _age<= maxAge_:
            self.__age = _age
        else: raise PersonAgeException(_age, minAge_, maxAge_)

    def __str__(self):
        return f"name: {self.__name}, age: {self.__age}"

class PersonAgeException(BaseException): # создаём своё исключение
    def __init__(self, _age, _minAge, _maxAge):
        self.age = _age
        self.minAge = _minAge
        self.maxAge = _maxAge

    def __str__(self):
        return f"Ошибка: введено неккоректное значение возраста: {self.age}\n" \
        f"значение должно быть в диапазоне от {self.minAge} до {self.maxAge}"

try: # если try/except не будет, то python всё равно напишет исключение
     # с traceback-ом (ибо мы вписали наше исключение в __init__),
     # но при этом выкинет из программы
    person1 = Person("Jesus", 33)
    person1 = Person("Judas", -1) # Exc!
except PersonAgeException as e: print (e) # используем своё исключение
print (person1)
print ()



# СПИСКИ, КОРТЕЖИ, СЛОВАРИ
numbers = [1,2,3,4,5,6]
people = ["Tom", "Ford", "Daimler", '', '\t']

numbers1 =  list([1,2,3,4,5,6])
numbers2 = []
people1 = list("Список")
peopleAndNumbers = list(["list", 1, 'f', 554.332])
print(numbers, '\t',numbers1, '\t', numbers2, '\t', \
 people, '\t', people1, '\t', peopleAndNumbers)

#ввод одинаковых значений
numbers2 = [5] *6
people = ["Tom", "Ford", 5.3] *3

# обращение к элементам списка
print(people[4])
print(people[-1]) # получение элемента с конца списка
                  # (у последнего элемента индекс = -1)
people[-3] = "not Tom"
print (people)

try:
    print(people[-0])
    print(people[-9])
  # print(people[9]) -- вылет только тут, ибо -0 = -9 = 0
    print(people[-(-1)]) # ошибок нет, ибо 
                         # сначала происходит вычисление индекса
except:
    print("выход за границы списка")

# Разложение списка
list_, int_, char_, float_ = peopleAndNumbers
print (list_, int_, char_, float_, sep = ', ')
print()

# перечисление списка (перебор элементов)
for person in people:
    print(person)
iter_ = 0
while iter_< len(people):
    print(people[iter_])
    iter_+=1

print (numbers==numbers1) # True, если внутренности совпадают
print()

# Получение части списка
lists = list()
lists.append(people[:3])    # с 0 по 3 элемент
lists.append(people[4:len(people)]) # с 4 по последний элемент
lists.append(people[0:7:3]) # c 0 по 6(!) элемент с шагом 3 (0,3,6 элементы)

print(people)
print()
for item in lists:
    print(item, end='\n')
print()

# обратный порядок заполнения
numbers1 = numbers[-1:-3] # элементов 6: значит будет идти с 5го по 3й; не работает (?)
print(numbers,'\n',numbers1) # ↑ пишет " []"; и почему при использовании '\n'
print()                      # нижняя строка смещается на пробел?

# Методы и функции по работе со списками (читаем на сайте)
# https://metanit.com/python/tutorial/3.1.php

# Проверка наличия элемента
print(people)
while "Ford" in people:
        index_ = people.index("Ford")
        print (f"Ford есть в списке людей под индексом "
       f"{index_}, удаляем")
        people.remove("Ford")
print(people)

del people[2:7:2]
print(people)
print("число вхождений слова \"Tom\": ", people.count("Tom"))
print("число вхождений числа 5.3: ", people.count(5.3))
print()

# остановились на сортировке
