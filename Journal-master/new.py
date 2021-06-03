def viewDiaryList(): #일기 보기 함수
    diaryList = tkinter.Tk()
    diaryList.geometry('660x480')
    diaryList.iconbitmap('viewNotes.ico')

    diaryList.title('일기 보기')

    showtitle = tkinter.Label(diaryList, text="목록")
    showtitle.place(x=30, y=60)

    showdiary = tkinter.Label(diaryList, text="일기 내용")
    showdiary.place(x=370, y=80)

    showimage = tkinter.Label(diaryList, text="이미지 파일")
    showimage.place(x=30, y=340)