#1 "save as" → utf-8
'''name = input("Введите имя: ")
print ("Привет, ", name)'''

#2  TAB or 4 SPACEs
#   Print != print
#   () is not necessary everywhere, same as ';' 
from telnetlib import X3PAD


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
_sum = null + first # + second -- EXCEPTION float vs str

print ("null is", null, ", first =", first,", second)", second,"\nsum — ", _sum)
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

#5 types, basic are bool, int, float, complex (?), str
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
_name = "TOM"
print ("\n\' or \" in str initialization — doesn`t matter: ", name, _name)

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

userName = input("\nВведите ваше имя:_")
userAge = input("Введите ваш возраст:_")
print(f"Ваше имя {userName}, тип значения {type(userName)},"
      f" а возраст -- {userAge}, тип значения {type(userAge)}")


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

def print_person(name, *,  age, company):   # '*,' относится к age и company -
                                            # - обязательное именование
    print(f"Name: {name}  Age: {age}  Company: {company}")
print_person("Bob", age = 41, company ="Microsoft")    # Name: Bob  Age: 41  company: Microsoft

