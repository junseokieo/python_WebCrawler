import requests
from bs4 import BeautifulSoup

# 한 건의 대화에 대한 정보를 담는 클래스
class Conversation:
    # 질문(question), 응답(respond) 두 변수로 구성된다
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer
    def __str__(self):
        return ("질문 : "+ self.question+ "\n답변"+ self.answer+ "\n")

# 모든 영어 대화 주제를 출력하는 함수
def get_subjects():
    subjects = []
    
    # 전체 주제 목록을 보여주는 페이지로의 요청 객체를 생성한다.
    req = requests.get('https://basicenglishspeaking.com/daily-english-conversation-topics/')
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    
    divs = soup.findAll('div', {"class": "thrv_wrapper thrv-columns"})
    for div in divs:
        # 내부에 존재하는 <a> 태그들을 추출합니다.
        links = div.findAll('a')
        
        # <a> 태그 내부의 텍스트를 리스트에 삽입합니다.
        for link in links:
            subject = link.text
            subjects.append(subject)
            
    return subjects
    
subjects = get_subjects()
print("총", len(subjects), "개의 주제\n")
print(subjects)
