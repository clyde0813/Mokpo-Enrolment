from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.alert import Alert
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from tkinter import *
import os

driver = webdriver.Chrome(os.getcwd() + '\\es\chromedriver.exe')


def url_open():
    url = 'http://mnusu.mokpo.ac.kr:7774'
    driver.get(url)

url_open()

def go():
    pass


dp = Tk()
main_frame = Frame(dp)
dp.geometry('300x500')
dp.title("목포대 수강신청 프로그램")
main_frame.pack()

id_label = Label(main_frame, text="아이디")
id_label.grid(row=1, column=0)
id_entry = Entry(main_frame)
id_entry.grid(row=1, column=1)

pw_label = Label(main_frame, text="비밀번호")
pw_label.grid(row=2, column=0)
pw_entry = Entry(main_frame)
pw_entry.grid(row=2, column=1)

start_button = Button(main_frame, text="시작", width=15, height=2)
start_button.grid(row=3, column=1)

empty_label1 = Label(main_frame)
empty_label1.grid(row=4)

major_label1 = Label(main_frame, text="전공1")
major_label1.grid(row=5, column=0)
major_entry1 = Entry(main_frame)
major_entry1.grid(row=5, column=1)
major_button1 = Button(main_frame, text="신청")
major_button1.grid(row=5, column=2)

major_label2 = Label(main_frame, text="전공2")
major_label2.grid(row=6, column=0)
major_entry2 = Entry(main_frame)
major_entry2.grid(row=6, column=1)
major_button2 = Button(main_frame, text="신청")
major_button2.grid(row=6, column=2)

major_label3 = Label(main_frame, text="전공3")
major_label3.grid(row=7, column=0)
major_entry3 = Entry(main_frame)
major_entry3.grid(row=7, column=1)
major_button3 = Button(main_frame, text="신청")
major_button3.grid(row=7, column=2)

major_label4 = Label(main_frame, text="전공4")
major_label4.grid(row=8, column=0)
major_entry4 = Entry(main_frame)
major_entry4.grid(row=8, column=1)
major_button4 = Button(main_frame, text="신청")
major_button4.grid(row=8, column=2)

major_label5 = Label(main_frame, text="전공5")
major_label5.grid(row=9, column=0)
major_entry5 = Entry(main_frame)
major_entry5.grid(row=9, column=1)
major_button5 = Button(main_frame, text="신청")
major_button5.grid(row=9, column=2)

empty_label2 = Label(main_frame)
empty_label2.grid(row=10)

general_label1 = Label(main_frame, text="교양1")
general_label1.grid(row=11, column=0)
general_entry1 = Entry(main_frame)
general_entry1.grid(row=11, column=1)
general_button1 = Button(main_frame, text="신청")
general_button1.grid(row=11, column=2)

general_label2 = Label(main_frame, text="교양2")
general_label2.grid(row=12, column=0)
general_entry2 = Entry(main_frame)
general_entry2.grid(row=12, column=1)
general_button2 = Button(main_frame, text="신청")
general_button2.grid(row=12, column=2)

general_label3 = Label(main_frame, text="교양3")
general_label3.grid(row=13, column=0)
general_entry3 = Entry(main_frame)
general_entry3.grid(row=13, column=1)
general_button3 = Button(main_frame, text="신청")
general_button3.grid(row=13, column=2)

general_label4 = Label(main_frame, text="교양4")
general_label4.grid(row=14, column=0)
general_entry4 = Entry(main_frame)
general_entry4.grid(row=14, column=1)
general_button4 = Button(main_frame, text="신청")
general_button4.grid(row=14, column=2)

general_label5 = Label(main_frame, text="교양5")
general_label5.grid(row=15, column=0)
general_entry5 = Entry(main_frame)
general_entry5.grid(row=15, column=1)
general_button5 = Button(main_frame, text="신청")
general_button5.grid(row=15, column=2)
dp.mainloop()
