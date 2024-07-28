from tkinter import *
import tkinter.ttk

def progress(progressbar):
    if progressbar['value'] < progressbar['maximum']:
        progressbar['value'] += 1
        root.after(10, progress, progressbar)
    else:
        create_third_window()

def create_third_window():
    new_window2 = Toplevel(root)
    new_window2.title('查询许超萍身份证')
    new_window2.geometry('300x300')
    lab_new2 = Label(new_window2, text='许超萍身份证为：330724198005207628')
    lab_new2.pack()
    

def window():
    new_window = Toplevel(root)
    new_window.title('查询许超萍身份证')
    new_window.geometry('300x300')

    lab_new = Label(new_window, text='正在查询许超萍身份证')
    lab_new.pack()

    progressbarOne = tkinter.ttk.Progressbar(new_window, length=250, mode='determinate')
    progressbarOne.pack()
    progressbarOne['maximum'] = 100
    progressbarOne['value'] = 0
    progress(progressbarOne)

root = Tk()
root.title('查询许超萍身份证')
root.geometry('500x500')

lab = Label(root, text='查询许超萍身份证')
lab2 = Label(root, text='本软件仅供学习使用，请勿用于非法用途！')
lab.pack()
lab2.pack()

bt = Button(root, text='查询', command=window)
bt.pack()

root.mainloop()

