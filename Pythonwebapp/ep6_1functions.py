
#การเขียนโปรแกรมจะมีฟังก์ชั่นที่มีการรับค่าเข้ามา Input  และการแสดงผล Display
#ซึ่งฟังก์ชั่นที่ว่ามานี้มี 2 ตัว คือ input & output

input('Type your name here')  #รับค่าเข้ามาทางคีย์บอร์ด

print('Hello world')   #แสดงผลค่า/ Debug code

#การผระกาศฟังก์ชั่นทำได้ดังนี้

    def student_info():
        print('Hello Student')

# def = defination การนิยาม
# student_info = ชื่อฟังก์ชั่น
#--หลักในการประกาศชื่อฟังก์ชั่นจะเหมือนกับการประกาศชื่อตัวแปร
#--คือจะใช้ตัวพิมพ์เล็ก Lowcase ทั้งหมด และถ้ามีคำสองคำจะคั่นด้วย Underscore

#-----การเรียกใช้งานฟังก์ชั่น---------#
def say_hello():
    print('hello world')

say_hello() #calling function


#------Parameters or Argument-----------#
#parameter
#ค่าตัวแปรที่ถูกกำหนดไว้ในฟังก์ชั่น โดยพารามิเตอร์แต่ละตัวจะถูกแยกด้วยเครื่องหมาย comma ","
    def student_info(name, lastname, age, std_id):
        print('Hello world')

        #name ,lastname, age, std_id ----> parameter


#Arguments คือค่าที่ส่งเข้าไปในฟังก์ชั่น โดยจะมีความสำพันธ์กันกับ Parameters
#โดยค่าที่ส่งเข้าไปในฟังก์ชั่นจะต้องมีค่าเท่ากับพารามิเตอร์ที่ประกาศไว้ในฟังก์ชั่นจะมากกว่าหรือน้อยกว่านี้ไม่ได้

def student_info(name, lastname, age, std_id):
    return name, lastname, age, std_id         # Return ค่าเหล่านั้นออกมา  #function

student_info('Isara', 'Stackpython', 21, 5234340189)  #Correct   #Argument
student_info('Isara', 21, 5234340189)  #Not correct


#---ฟังก์ชั่นไม่จำเป็นต้องใส่ค่าพารามิเตอร์ก็ได้
def student_info
    print('Hello world')

student_info()
#Hello world


#ตัวแปรที่ประกาศในฟังก์ชั่นจะใช้นอกฟังก์ชั่นไม่ได้ Local Variable
#ถ้าประกาศฝให้ใชเ้ภายนอกไดเ้ให้ประกาศ Global Varible

    def student_info():
        name = 'Chatchai'
        age = 18 

    msg = 'I am'
    print(msg, age, 'year old')
    # NameError : name 'age' is not defined


#ฟังก์ชั่นปล่อยเป็นค่าว่างไม่ได้
# ฟังก์ชั่นไม่สามารถปล่อยเป็นค่าว่างได้ คือต้องมีการการกระทำในฟังก์ชั่นนั้น ถ้าหากมีความจำเป็นที่ไม่ต้องกระทำใด ๆ ในฟังก์ชั่นนั้น ให้ใช้คำสั่ง pass

def student_info():
    pass

def student_info():
    #This will raise an error

    #-------Docstring Functions----------------#

    เราสามารถทำ Docstring เพื่อบอกว่าฟังก์ชั่นนี้ใช้ทำอะไร โดยใช้เครื่องหมาย Triple Quotes
    def say_hello():
        """ This function is used to
        display 'Hello World"""
        print('Hello World Freshness')


