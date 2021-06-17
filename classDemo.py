'''
設計類
類名:見名知意首字母大寫遵循駝峰原則
屬性:見名知意駝峰原則
行為:方法
'''

'''
創建類
類:一種數據類型,本身並不占內存空間
實例化對象,對象占內存空間
格式
class 類名(父類列表):
    屬性
    行為
'''
#object:基類,超類,所有類的父類
#一般沒有合適的父類就寫object

class Person(object):
    #定義屬性
    name = ""
    age = 0
    height = 0
    weight = 0

    #定義方法(定義函數)
    #注意:方法的參數必須以self當第一個參數
    #self代表類的實例(某個對象)
    def run(self):
        print("run")
    def eat(self, food):
        print("eat" + food)
