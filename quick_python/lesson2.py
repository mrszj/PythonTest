#coding=utf8
def collatz(number):
    if number%2 ==0:
        return number//2
    else:
        return 3*number+1
    
while True:
    try:
        num=input("请输入一个非0的整数:\n")
    except Exception:
        print("您输入的值异常!")
        continue
    if num==0:
        continue
    if num<0:
        num=-num
    break

print("现在开始计算:\n")
n=num
t=0
while n != 1:
    n=collatz(n)
    t+=1
    print(n)
print("经过%d次神秘计算,您输入的%d变为1了! Unbelievable!!!") %(t,num)


     

    