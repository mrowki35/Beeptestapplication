import time

t = 0
level = 1
period = 0

while (level!=23):
    while(t<=63):
        time.sleep(0.01)
        t=t+0.01
        print(t)
    print(level)
    level = level +1 
