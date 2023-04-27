import tkinter
import tkinter.font
import random #랜덤함수사용하겠다는 선언

lotto_num = range(1, 46) #1~45까지의 랜덤정수생성

def buttonClick(): #버튼클릭함수생성
    label=tkinter.Label(window, text=str(random.sample(lotto_num, 6))) #6개의 랜덤정수를 리스트형식으로 window창 안에 생성
    label.pack() #보여주기
    #print(random.sample(lotto_num, 6)) #6개의 랜덤정수 생성

window=tkinter.Tk() #윈도우(창)생성
window.title("lotto") #창 이름은 lotto
window.geometry("400x200") #창 크기는 가로400 세로200
window.resizable(False, False) #크기조절여부(불가능)

button = tkinter.Button(window, overrelief="solid",text="번호확인", width=15, command=buttonClick, repeatdelay=1000, repeatinterval=100)
#버튼창 생성, 버튼의 이름은 "번호확인", 두께는 15, 명령은 마우스클릭, 반복딜레이는1000, 반복간격은100
button.pack()#보여주기

window.mainloop() #계속 움직이게 만드는 mainloop생성.