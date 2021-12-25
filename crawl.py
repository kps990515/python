import requests # 파이썬 에서 requests 모듈을 불러옵니다
                # requests 는 기본 모듈이 아니기때문에 설치를 해줘야합니다
                # 파이썬 환경변수를 등록후(기본 등록되어있음)
                # cmd 창에서 > pip install requests < 를 쳐줍니다
import json     # json 형식으로 쪼개주는 모듈입니다 
from bs4 import BeautifulSoup # html 코드를 이쁘게 정렬해주는 모듈입니다
                              # requests 와 마찬가지로 외부 모듈입니다
                              # pip install BeautifulSoup 로 설치를 해주시면 됩니다

def updateLp():
    lpList = []
    count = 0
    
    for n in range(1,15):
        url = "https://api-cypress.scope.klaytn.com/v1/tokens?key=KSLP&page=" + str(n)
        req = requests.get(url).content
        data = json.loads(req)
        result = data['result'] #Result json 불러오기
        
        for item in result: # result에 있는 LP하나씩
            with open("klayswapLP.txt", "r", encoding="utf8") as f:
                old_lps = f.read().split("\n")  #기존 파일 열어서 하나씩 읽어오기

            new_lps = []
            
            if item['tokenName'] not in old_lps:
                new_lps.append(item['tokenName'])
                lpList.append(item['tokenName'])
            else:
                pass
                
            for new in new_lps: 
                with open("klayswapLP.txt", "a", encoding="utf8") as f:
                    f.write(new + "\n")
            
    return lpList

