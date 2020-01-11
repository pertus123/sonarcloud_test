def sum(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
def rem(a,b):
    return a%b
 
while True:
    menu = int(input("원하는 계산기 기능을 입력하세요.  "))
    if(menu <= 5):
        numberA = int(input("첫번째 숫자를 입력하세요.  "))
        numberB = int(input("두번째 숫자를 입력하세요.  "))
        if(menu == 1):
            result = sum(numberA, numberB)
            print("결과는 %d 입니다."%result)
        elif(menu == 2):
            result = sub(numberA, numberB)
            print("결과는 %d 입니다."%result)
        elif(menu == 3):
            result = mul(numberA, numberB)
            print("결과는 %d 입니다."%result)
        elif(menu == 4):
            result = div(numberA, numberB)
            print("결과는 %d 입니다."%result)
        elif(menu == 5):
            result = rem(numberA, numberB)
            print("결과는 %d 입니다."%result)
    elif(menu == 6):
        break
    else:
        print("잘못입력하셨습니다. 다시 입력해 주세요.")
