import random 

print("Hello Andre!!!")
print("Hello Alex")
print("Hello Phurin")

list = random.choice([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])

x = input("Do you wish to play y/n\n: ")
if x.lower() == "y":
    while True:
        print("How old am i")
        svar=int(input())
        if svar < list:
            print("Too young")
            continue
        elif svar > list:
            print("Too old")
            continue
        elif svar == list:
            print(f"Hurray, you got it right, i am {list} computer years old!")
            break
else:
    print("ok no play then")
        