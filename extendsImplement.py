from child import Child

def main():
    c = Child(300, 100)
    print(c.money, c.faceValue)
    c.play()
    c.eat()
    #注意:父類中方法名相同,默認調用在括號中排前面的父類方法class Child(Father, Mother):
    #(Father, Mother):所以調用Father優先調用,順序交換則反之
    c.func()

if __name__ == "__main__":
    main()