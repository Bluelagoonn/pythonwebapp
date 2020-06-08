"""
# คำถาม 1 ได้ผลลัพท์เท่าไหร่ทำไมถึงเป็นแบบนั้น

def result(cost, income):
    return income - cost

print(result(4000))
# Error
#ส่ง Argument ไม่ครบตามจำนวน parameter

"""
"""
# คำถาม 2 ได้ผลลัพท์เท่าไหร่ทำไมถึงเป็นแบบนั้น

def result():
    framework = "Flask"
    language = "Python"

print('I love', framework)
# framework is not defind
#frame ถูกกำหนดอยู่นอกฟังก์ชั่น
"""
"""
# คำถาม 3 ได้ผลลัพท์เท่าไหร่ทำไมถึงเป็นแบบนั้น

def result():

print(result())

#ใช้ไม่ได้เนื่องจากปล่อย function Empty และไม่ได้ใส่ pass ในฟังก์ชั่นเพื่อทำการข้ามไม่ใช้งานฟังก์ชั่นที่ว่างเปล่า

"""

# คำถาม 4 ทำให้ข้อมูลที่ได้ถูกรีเทินค่าออกมาเป็น Tuple

def result(cost, income):
    return[income, cost]

print(type())?
#< class 'list'>
