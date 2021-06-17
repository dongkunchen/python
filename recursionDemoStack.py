#模擬棧結構 棧stack 先進後出
stack = []

#壓棧(向棧里存數據)
stack.append("A")
print(stack)
stack.append("B")
print(stack)
stack.append("C")
print(stack)
stack.append("D")
print(stack)

#出棧(在棧里取數據)
res1 = stack.pop()
print("res1 =", res1)
res2 = stack.pop()
print("res1 =", res2)
res3 = stack.pop()
print("res1 =", res3)
res4 = stack.pop()
print("res1 =", res4)