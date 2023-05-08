number = 12  # Manfiy yoki musbat bo'lgan raqam 👉

bool = False  # True yoki False

set = set()  # Bu to'plam bo'lib to'plam elementlarini takrorlarnmas saqlaydi

dict = {"last_name": "Bahodirjon", "first_name": "Ikromiddinov"}  # samarali kalit/qiymat deb ataladi

sequence = 'Bahodirjon'  # Sequence malumotlarni ketma-ket tartiplangan to'plami 👉

# Number turlari

int = 12  # Int bu butun son

float = 12.0  # Float bu qoldiqli son

complex = complex(1, 2)  # Complex biz satr yoki raqamni murakkab ma'lumotlar turiga aylantirish

# Sequence turlari

list = ['Javascript', 'Python', 'Typescript']

tuple = ('HTML', 'CSS', 'SCSS')

string = 'Lesson 1'

# if, elif, else buyruqlari

age = 16

if age >= 12:
    print("Siz 12 yoshdan kichik yoki tengsiz")
elif age >= 16:
    print("Siz 12 yoshdan katta yoki 16 yoshdan kichiksiz yoki kattasiz")
else:
    print("Siz 16 yoshdan kattasiz")

# for sikli

students = ['Bahodirjon', 'Islombek', 'Iqboljon']

for student in students:
    print("Maktab boshlandi " + student)

# while sikli

age = 0

while age <= 100:
    age += 1
    print("Siz " + str(age) + ' yoshga kirdingiz.')


# funksiya chegaralangan bayonotlar ketma-ketligini o'z ichiga oladi

def func(name):
    print("Salom " + name)


func('Bahodirjon')

# """
#     Modul oddiy Python fayli boʻlib, unda funksiyalar va global
#     oʻzgaruvchilar toʻplami mavjud va . py kengaytmali fayl.
#     Bu bajariladigan fayl va barcha modullarni tartibga solish
#     uchun bizda Pythonda Package deb nomlangan tushuncha mavjud
# """



