from tkinter import *

root = Tk()
root.title("Stock")
root.geometry("200x50")  # 윈도우 창이 띄어질 때의 기본 크기를 설정한다.
root.resizable(0, 0)  # 띄어진 후 변경 가능한 크기를 설정한다.

def your_name():  # 버튼이 눌렸을 때 실행 될 함수 선언
  print("Hello!")

lbl = Label(root, text="Stock", font = "NanumFothic 10")  # (윈도우 창, 표시할 텍스트, 폰트)
# lbl.pack()  # 위젯 배치
lbl.grid(row = 0, column = 0)

txt = Entry(root)  # 입력받기
# txt.pack()
txt.grid(row = 0, column = 1)

btn = Button(root, text = "ok", command = your_name)  # (윈도우 창, 버튼 표시 이름, 실행할 함수)
# btn.pack()
btn.grid(row = 1, column = 1)

root.mainloop()