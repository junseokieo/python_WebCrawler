import requests
from bs4 import BeautifulSoup

#특정 URL에 접속하는 요청 객체를 생성한다.
request = requests.get("http://www.dowellcomputer.com/main.jsp")

#접속한 이후의 웹사이트 소스코드를 추출한다.
html = request.text

# html 소스코드를 파이썬 객체로 변환한다.
soup = BeautifulSoup(html, 'html.parser')

# <a> 태그를 포함하는 요소를 추출한다.
links = soup.select('td > a')


#모든 링크에 하나씩 접근한다
for link in links:
    # 링크가 href 속성을 가지고 있다면
    if link.has_attr('href'):
        # href 속성의 값으로 notice 라는 문자열이 포함되어 있다면
        # find 함수는 포함이 안되면 -1을 반환한다.
        if link.get('href').find('notice') != -1:
            print(link.text)

#print(html)
