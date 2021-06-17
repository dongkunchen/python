import collections
#隊列Queue 先進先出

#進隊
queue = collections.deque()
print(queue)
queue.append("A")
print(queue)
queue.append("B")
print(queue)
queue.append("C")
print(queue)

#出隊(取數據)
res1 = queue.popleft()
print("res1 =", res1)
print(queue)
res2 = queue.popleft()
print("res2 =", res2)
print(queue)
res3 = queue.popleft()
print("res3 =", res3)
print(queue)