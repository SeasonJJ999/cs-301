msg = "hello"

def greeting():
    global msg#!!!!
    print(msg)
    msg = "howdy"

print("before:", msg)
greeting()
print("after:", msg)
