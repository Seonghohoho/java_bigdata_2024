# file: p34_addrBook.py
# desc: 콘솔 주소록  프로그램

import os

class Contact:
    def __init__(self, name, phoneNumber, eMail, addr) -> None:
        self.__name = name
        self.__phoneNumber = phoneNumber
        self.__eMail = eMail
        self.__addr = addr

    def __str__(self) -> str:
        res = (f'이  름 : {self.__name}\n' 
               f'핸드폰 : {self.__phoneNumber}\n'
               f'이메일 : {self.__eMail}\n'
               f'주  소 : {self.__addr}')
        return res
    
def setContact():
    (name, phoneNumber, eMail, addr) = input('주소록 입력(이름, 핸드폰, 이메일, 주소[구분자 /]) > ').split('/')
    name = name.strip()
    phoneNumber = phoneNumber.strip()
    eMail = eMail.strip()
    addr = addr.strip()
    contact = Contact(name, phoneNumber, eMail, addr)
    return contact

def clearConsole():
    cmd = 'clear'
    if os.name in ('nt', 'dos'):
        cmd = 'cls'
    os.system(cmd)

def displayMenu():
    menu = ('주소록 프로그램\n'
            '1. 연락처 추가\n'
            '2. 연락처 출력\n'
            '3. 연락처 삭제\n'
            '4. 종료\n')
    print(menu)
    sel = int(input('메뉴입력 : '))
    return sel

def getContact(lstContact):
    for contact in lstContact:
        print(contact)

def run():
    lstContact = []

    clearConsole()
    while True:
        selMenu = displayMenu()

        if selMenu == 1:
            clearConsole()
            contact = setContact()
            lstContact.append(contact)
            input()
            clearConsole() 
        elif selMenu == 2:
            clearConsole()
            getContact(lstContact)
            input()
            clearConsole()
        elif selMenu == 4:
            break
        else:
            clearConsole()

if __name__ == '__main__':
    print('프로그램 시작')
    run()
    print('프로그램 종료')
