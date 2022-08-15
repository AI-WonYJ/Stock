from tkinter import *
from tkinter import messagebox
root = Tk()
root.title("blog")
root.geometry("200x100")
root.resizable(0,0)

def your_name():
	yn = txt.get() #텍스트 입력란에서 값을 가져와서 변수 yn에 저장한다.
	lbl2.configure(text="your name: "+yn) #함수가 실행시 라벨2를 yn의 변경 값으로 설정, 사용자의 조작에 따라 라벨과 텍스트의 변경이 필요할 때 지정해서 바꾸거나 입력을 받아서 바꾸 경우에 사용
	messagebox.showinfo("name",yn) #메시지 박스를 띄운다., (팝업 창의 캡션 부분, 실질적으로 나타나는 메시지)

lbl = Label(root, text="name", font="NanumGothic 10")
lbl.grid(row=0, column=0)

txt = Entry(root)
txt.grid(row=0,column=1)

btn = Button(root, text="ok",command=your_name,width=3,height=1)
btn.grid(row=1,column=1)

lbl2 = Label(root,text="your name : ") #새 객체, 라벨2는 이름을 받아 동적으로 변화한다.
lbl2.grid(row=2,column=1) #라벨2가 위치할 곳은 제일 하단이다.

root.mainloop()
