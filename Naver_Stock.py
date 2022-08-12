#네이버 금융 삼성전자 데이터 수집
import requests
from bs4 import BeautifulSoup
#함수형태 변환
def get_bs_obj(com_code):
    url = "https://finance.naver.com/item/main.nhn?code=" + com_code
    result = requests.get(url)
    bs_obj = BeautifulSoup(result.content, "html.parser") #html.parser 로 파이썬에서 쓸 수 있는 형태로 변환
    return bs_obj

def get_price(com_name, com_code):
  bs_obj = get_bs_obj(com_code)
  no_today = bs_obj.find("p", {"class":"no_today"})
  blind_now = no_today.find("span", {"class":"blind"})
  print("{0} 현재가\n {1}\n".format(com_name, blind_now.text))
  return blind_now.text

from datetime import datetime
import time

while True:
  now = datetime.now()
  print("             \n", now.time())
  # 삼성전자 005930
  get_price("삼성전자", "005930")

  # LG전자 066570
  get_price("LG전자", "066570")

  # 카카오 035720
  get_price("카카오", "035720")
  print("\n============================================")
