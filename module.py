#import requests
#from bs4 import BeautifulSoup
a=int(input("Выберите, по какому документу вам нужно найти задолженность:\n 1)СНИЛС\n 2)ИНН\n 3)СТС\n 4)Номер ИП\n 5)ВУ\n 6)Паспорт\n"))
b=str(input("Введите номер документа в формате нескольких цифр идущих подряд (без пробелов и дефизов):\n "))
url0="https://fssp.online/subscription?"
if a==1:
    url=url0+'snils='+b+'#by-snils'
elif a==2:
    url=url0+'inn='+b+'#by-inn'
elif a==3:
    url=url0+'vehicle='+b+'#by-sts'
elif a==4:
    url=url0+'vehicle='+b+'#by-sts'
elif a==5:
    url=url0+'icense='+b+'#by-vu'
elif a==6:
    url=url0+'passport='+b+'#by-passport'
print(url)
#r=requests.get(url)
#soup=BeautifulSoup(r.text, 'lxml')
#block=soup.find('input', id="search-by-snils")
#print(block)