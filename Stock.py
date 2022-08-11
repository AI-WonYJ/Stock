#네이버 금융 삼성전자 데이터 수집
import requests
from bs4 import BeautifulSoup
#함수형태 변환
def get_bs_obj(com_code):
    url = "https://finance.naver.com/item/main.nhn?code=" + com_code
    result = requests.get(url)
    bs_obj = BeautifulSoup(result.content, "html.parser") #html.parser 로 파이썬에서 쓸 수 있는 형태로 변환
    return bs_obj

def get_price(com_code):
  bs_obj = get_bs_obj(com_code)
  no_today = bs_obj.find("p", {"class":"no_today"})
  blind_now = no_today.find("span", {"class":"blind"})
  return blind_now.text

from datetime import datetime
import time

while True:
  삼성전자 = get_price("005930")
  LG전자 = get_price("066570")

  now = datetime.now()
  print("             ", now.time())
  # 삼성전자 005930
  print("\n삼성전자 현재가")
  print(삼성전자)

  # LG전자 066570
  print("\nLG전자 현재가")
  print(LG전자)
  print("\n============================================")
