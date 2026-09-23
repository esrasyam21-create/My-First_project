
#  Python Revision Exercises

name="noor"
hyppy="coding"

print(name.upper())
print(name.lower())

print(name.isalnum())
print(name.isalpha())

print(name.title())

iccuil=(12.3424, 34.64)
print(iccuil)
print(type(iccuil))

iccuil=[12.3424, 34.64]
print(iccuil)
print(type(iccuil))

dic={"name":"sara", "age":"25," , "happy":"sw"}
print(dic)
print(dic["name"])
print(dic["age"])
print(dic["happy"])
print(type(dic))
print("********************************************")

name="Israa"
last_Name="Seyam"
print(f"My name is {name} and last name is {last_Name}")
print("My name is {} and last name is {}".format(name,last_Name))
print(name.split())
print(name.strip())
print(name.swapcase())
print(name.startswith("N"))
print(name.isalnum())
print(name.isascii())
print(name.isalpha())
print(name.lower())
print(name.lstrip())
print(name.upper())
print(name.endswith("r"))
print(type(name))

# string  ثابت

#  tuple  () ثابت
location=(12.433, 156.66)
print(type(location))
print(location)
print(location[0])
print(location[1])
 #    خطا   location[1]=10 


# list [] مرتبين // مرنة //  
location=[12.433, 156.66]
print(type(location))
print(location)
print(location[0])
print(location[1])
location[1]=10
print(location)

# dictionry  []    
dic={"name":"sara","age":25 , "hoppy":"swwiming"}
for i in dic.keys() :
    print(i)

for i in dic.values() :
    print(i)

for i in dic.items() :
    print(i)


# /////  sit لا تسمح بالتكرار 

#################################################################

#functions

#parameter  تستخدم  لكتابة اسم الفاريبل عند تعريف الدالة الفا,نكشن
#Argument تستخدم لكتابة اسم الفاريبل عند الاستدعاء  للدالة الفاونكشن

# Declaration using 'def' 
def make_coffee(beans_type):  # 'beans_type' is the Parameter 
    return f"A hot cup of {beans_type} coffee"

# Calling the function 
order = make_coffee("Espresso") # "Espresso" is the Argument 
print(order) 

print("********************************************************")

# Function with a Side Effect (Print) سايد افيكت يعني الدالة بتطبع انه معها قيمة كذا وليس فيها قيمة مخزنة بس طباعة بدون تخزين
def add_side_effect(a, b): 
    print(a + b)  
# Function with a Result (Return) return يعني بس بيخزن قيمة الدالة  للاستعمال اللاحق
def add_result(a, b): 
    return a + b 
# see the difference: 
val1 = add_side_effect(5, 5) # This shows 10 on the screen 
val2 = add_result(5, 5)      
# This shows nothing on the screen yet 
print(f"Val1 is: {val1}") # Output: Val1 is: None (Because nothing was returned!) 
print(f"Val2 is: {val2}") # Output: Val2 is: 10 (Because it gave back a result) 
final_step = val2 * 2 
print(f"The doubled result is: {final_step}") # Output: 20




















"""
# task 1

""" 

def countdown(n):
# ننشئ قائمة تبدأ من n وتنتهي بـ 0 (نكتب -1 لكي يشمل الصفر، وخطوة -1 للنزول) 
    return list(range(n, -1, -1))
# مثال للتجربة:
print(countdown(5))# النتيجة ستكون: [5, 4, 3, 2, 1, 0] 

#___________ Another Solution __________

def countdown(n):
    output=[]
    for i in range(n, -1, -1):
        output.append(i)
    return output      
print(countdown(5))


"""
# task 2
"""

def print_and_return(num):
    print(num[0])
    return num[len(num)-1]
print_and_return([1, 2])

print(print_and_return([1, 2]))


"""""
# task 3
"""
def first_plus_length(lst):
    # lst[0] هو العنصر الأول، و len(lst) تعطينا طول القائمة
    return lst[0] + len(lst)

print(first_plus_length([1, 2, 3, 4, 5]))  #  6  ---->   (لأن 1 + 5 = 6)


"""
# task 4
"""
def values_greater_than_second(lst):
    # اول ايشي بنتحقق اذا كانت القائمة أقل من عنصرين، لا يمكن المقارنة
    if len(lst) < 2:
        return []
    
    second_value = lst[1] # نحفظ العنصر الثاني
    newList = []
    
    for x in lst:
        if x > second_value:
            newList.append(x)
            
    return newList

print(values_greater_than_second([5, 2, 3, 2, 1, 4])) 
# العنصر الثاني هو 2، الأكبر منه هي [5, 3, 4]

 
"""
# task 5
"""
def length_and_value(size, value):
    # نكرر القيمة (value) بعدد مرات (size) داخل قائمة
    return [value] * size

length_and_value(4, 7) #  النتيجة: [7, 7, 7, 7]
"""
# task 6
"""

def biggie_size(lst):
    for i in range(len(lst)):
        if lst[i] > 0:
            lst[i] = "big"  # تعديل العنصر مباشرة إذا كان موجباً
    return lst

print(biggie_size([-1, 3, 5, -5]))  # : [-1, 'big', 'big', -5]


"""
# task 7
"""
def count_positives(lst):
    count = 0
 
# حساب عدد الأرقام الموجبة
    for num in lst:
        if num > 0:
            count += 1
            
    # استبدال العنصر الأخير بالعدد النهائي للأرقام الموجبة
    lst[-1] = count
    return lst

print(count_positives([1, 6, -4, -2, -7, -2]))  #: [1, 6, -4, -2, -7, 2]



"""
#task 8
"""
def sum_total(lst):
    # استخدام الدالة الجاهزة sum لحساب المجموع مباشرة
    return sum(lst)

print(sum_total([1, 2, 3, 4]))  # 10



"""
#task 9
"""
def average(lst):
    # المتوسط يساوي المجموع مقسوماً على العدد
    return sum(lst) / len(lst)

print(average([1, 2, 3, 4]))  #  2.5




"""
#task 10
"""

def minimum(lst):
    # اول ايشي بنتحقق  مما إذا كانت القائمة فارغة
    if len(lst) == 0:
        return False
    
    # بنستخدم الدالة الجاهزة min عشان نجيب القيمة الصغرى
    return min(lst)

print(minimum([5, 2, 8, 1]))  #  1
print(minimum([]))           # False


