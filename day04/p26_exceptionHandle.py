# file: p26_exceptionHandle.py
# desc: 예외처리
# 오류(Error) : 코드상 빨간색(노란색) 밑줄이 그어지는 것
# 예외(Exception) : 프로그램 실행 중에 생기는 오류(비정상적 종료)

# 파일읽어서
try:
    f = open('./samnle.txt', mode='r', encoding='utf-8')
    # # blah blah blah
    res = f.readline()
    print(res)
except:
    print('파일오픈 예외발생!!')
finally:
    try:
        f.close()
    except NameError as e:
        print('파일 오픈실패')

# 2. 계산결과
try:
    print(5 / 0)

except ZeroDivisionError as e:
    print('나누기 예외발생!!')

# print( 5 / 0 )

# a, b = 5, 3

# if a == b:
# print(True)