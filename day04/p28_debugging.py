# file: p28_debugging.py
# desc: 디버깅 학습, 예외처리 추가

class newCalc:
    def add(self,a, b):
        res = (a + b)
        return res
    
    def minus(self,a, b):
        res = (a - b)
        return res
    
    def mult(self,a, b):
        res = (a * b)
        return res
    
    def div(self,a, b):
        res = (a / b)
        return res

while True:
    select = int(input('메뉴 1.더하기, 2.빼기, 3.곱하기, 4.나누기, 5.종료 > '))

    if select ==1:
        x, y = map(int, input('두 수 입력(정수) > ').split())
        calc = newCalc()
        print(f'더하기 결과 : {x} + {y} = {calc.add(x, y)}')
    elif select ==2:
        x, y = map(int, input('두 수 입력(정수) > ').split())
        calc = newCalc()
        print(f'빼기 결과 : {x} - {y} = {calc.minus(x, y)}')  
    elif select ==3:
        x, y = map(int, input('두 수 입력(정수) > ').split())
        calc = newCalc()
        print(f'곱하기 결과 : {x} * {y} = {calc.mult(x, y)}') 
    elif select ==4:
        x, y = map(int, input('두 수 입력(정수) > ').split())
        calc = newCalc()
        if y == 0:
            print('제수에 0을 입력하지 마세요')
            input()
            continue

        print(f'나누기 결과 : {x} ÷ {y} = {calc.div(x, y)}')        
    elif select == 5:
        print('프로그램을 종료합니다.')
        input() #임시로 멈춤
        break
    else: # 1~5 외의 입력이 들어오면
        continue
