#네이버 금융 삼성전자 데이터 수집
import requests
from bs4 import BeautifulSoup

# Treeview 메서드는 tkinter의 ttk 모듈 내부에 존재한다. tkinter.ttk 모듈로 호출한다.
import tkinter
import tkinter.ttk

from datetime import datetime
import time


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

# ﻿GUI창을 생성하고 라벨을 설정한다.
root=tkinter.Tk()
root.title("Stock")
root.geometry("540x300+100+100")
root.resizable(False, False)

lbl = tkinter.Label(root, text="My Stock")
lbl.pack()

# ﻿표 생성하기. colums는 컬럼 이름, displaycolums는 실행될 때 보여지는 순서다.
treeview=tkinter.ttk.Treeview(root, columns=["one", "two","three", "four"], displaycolumns=["one","two","three", "four"])
treeview.pack()

# 각 컬럼 설정. 컬럼 이름, 컬럼 넓이, 정렬 등
treeview.column("#0", width=50,)
treeview.heading("#0", text="index")

treeview.column("#1", width=100, anchor="center")
treeview.heading("one", text="종목명", anchor="center")

treeview.column("#2", width=70, anchor="center")
treeview.heading("two", text="보유수량", anchor="center")

treeview.column("#3", width=100, anchor="center")
treeview.heading("three", text="현재가", anchor="center")

treeview.column("#4", width=100, anchor="center")
treeview.heading("four", text="평가손익", anchor="center")


while True:
  time.sleep(1)
  삼성전자 = int(get_price("005930").replace(",",""))
  LG전자 = int(get_price("066570").replace(",",""))
  now = datetime.now()
  
  # 표에 삽입될 데이터
  treelist=[("삼성전자", 7, 삼성전자, ((삼성전자*7) - 412800)), ("LG전자", 6, LG전자, ((LG전자*6) - 560600))]
  
  # 표에 데이터 삽입
  for i in range(len(treelist)):
      treeview.insert('', 'end', text=i, values=treelist[i], iid=str(i)+"번")

  # 슴겨진 항목 (추후 관심 주 추가 항목으로 변경)
  # top=treeview.insert('', 'end', text="hidden index", iid="5번")
  # top_mid1=treeview.insert(top, 'end', text="5", values=["Timy", 0, 8], iid="5번-1")
  # top_mid2=treeview.insert(top, 0, text="6", values=["Ann", 35, 7], iid="5번-0")
  # top_mid3=treeview.insert(top, 'end', text="7", values=["Sany", 60, 6], iid="5번-2")

  # GUI 실행
  root.mainloop()
