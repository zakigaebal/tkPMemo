import imp
from tkinter import *
from tkinter.filedialog import *

# 각 메뉴가 클릭됐을 때 실행될 함수 정의
def new_file():
    # 텍스트 영역 지우기
    text_area.delete(1.0,END)

def save_file():
    # 파일 저장 물어보기
    f = asksaveasfile(mode='w', defaultextension='txt',filetypes=[('Text files','txt')])
    # 텍스트영역에 있는 것들을 문자화 시켜서 저장하기
    text_save = str(text_area.get(1.0, END))
    f.write(text_save)
    f.close()

def maker():
    # 새 창 만들고 내용 적기
    help_view = Toplevel(window)
    help_view.geometry('300x50+850+400')
    help_view.title('만든 이')
    lb = Label(help_view, text='\nby 최대열')
    lb.pack()

# 윈도우 생성
window = Tk()
window.title('메모장')
window.geometry('400x400+800+300')
window.resizable(0,0)

# 메뉴 생성
menu = Menu(window)
#첫번째 메뉴 생성
menu_1 = Menu(menu, tearoff=0)
#첫번째 메뉴의 세부 메뉴 추가, 함수 연결
menu_1.add_command(label='새 파일', command=new_file)
menu_1.add_command(label='저장',command=save_file)
# 줄 추가
menu_1.add_separator()
menu_1.add_command(label='종료',command=window.destroy)
# 메뉴바에 추가
menu.add_cascade(label='파일',menu=menu_1)

#두번째 매뉴 생성
menu_2 = Menu(menu, tearoff=0)
#세부메뉴추가, 함수 연결
menu_2.add_command(label='만든 이',command=maker)
# 메뉴바에 추가
menu.add_cascade(label='정보',menu=menu_2)

# 텍스트 창 추가하기
text_area = Text(window)
# 공백설정
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)
#화면배치, 동서남북으로 모두 붙인다
text_area.grid(sticky=N+E+S+W)

# 메뉴 구성
window.config(menu=menu)
window.mainloop()