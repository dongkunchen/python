import time
import itertools

#mylist = list(itertools.product("0123456789abcd", repeat=10))
passwd = ("".join(x) for x in itertools.product("0123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM",repeat=10))
# print(mylist)
# print(len(mylist))
while True:
    try:

        str = next(passwd)
        time.sleep(0.5)
        print(str)

    except StopIteration as e:
        break
