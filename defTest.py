'''
def 函數名(參數列表):
    功能
    return
'''
#定義無參無返回值函數
def myPrint():
    print("good man!")
    print("nice man!")
    print("handsome man!")

'''
函數調用
格式:函數名(參數列表)
沒參數也不能省略括號
'''

myPrint()
myPrint()
myPrint()
myPrint()


#有參數函數
#形參(形式參數):定義函數時小括號中的變量
#參數必須按順序傳遞,數目要對應///def myPrint(str,age,hoby):報錯
def myPrint(str,age):
    print(str, age)

myPrint("good man",18)

#編寫函數實現功能給函數兩個數返回兩個數的和

def mySum(num1, num2):
    #將結果返回給函數的調用者
    return num1 + num2
    #執行完return語句後不執行
    print("-***********")

res = mySum(1,2)
print(res)

'''
值傳遞:傳遞的不可變類型
string tuple number是不可變的
'''
def func1(num):
    num = 10
temp = 20
func1(temp)
print(temp)
'''
引用傳遞:傳遞的可變類型
'''
def func2(lis):
    lis[0] = 100

li = [1,2,3,4,5]
func2(li)
print(li)
