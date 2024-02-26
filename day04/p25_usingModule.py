# file: p25_usingModule.py
# desc: 모듈 사용

import calc as c # 나는 calc.py를 사용할래
from calc import mul as mult # mul() 함수명만 쓰면 됨

import Math


if __name__ == '__main__': ## java void main()과 동일 
    result = mult(10, 7)
    print(result)

    print(__name__) # __main__ = 나는 메인엔트리야

    myMath = Math, Math()
    print(myMath.solv(10))

    