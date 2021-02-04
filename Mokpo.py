from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.alert import Alert
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from tkinter import *
import os

driver = webdriver.Chrome(os.getcwd() + '\\es\chromedriver.exe')
wait1 = WebDriverWait(driver, 3)


def url_open():
    url = 'http://mnusu.mokpo.ac.kr:7774'
    driver.get(url)


url_open()


def login():
    driver.find_element_by_id("name").send_keys(id_entry.get())
    driver.find_element_by_id("pwd").send_keys(pw_entry.get())
    driver.find_element_by_class_name("btn_login").click()


def lecture(a, b):
    major = wait1.until(EC.presence_of_all_elements_located((By.XPATH,
                                                             '//*[contains(text(), "' +
                                                             a + '")]/following-sibling::td/a[@class="btn_ok"]')))
    major[int(b) - 1].click()


def all_command():
    major_status = major_var.get()
    general_status = general_var.get()
    if major_status == 1:
        major_start()
    elif general_status == 1:
        general_start()


def major_start():
    driver.get('http://mnusu.mokpo.ac.kr:7774/login/3')
    login()
    try:
        wait1.until(EC.presence_of_element_located((By.ID, "search"))).click()
        lecture(lecture_entry1.get(), lecture_entry12.get())
        lecture(lecture_entry2.get(), lecture_entry22.get())
        lecture(lecture_entry3.get(), lecture_entry32.get())
        lecture(lecture_entry4.get(), lecture_entry42.get())
        lecture(lecture_entry5.get(), lecture_entry52.get())

    except Exception as ec:
        print(ec)


def general_start():
    driver.get('http://mnusu.mokpo.ac.kr:7774/login/2')
    login()
    try:
        wait1.until(EC.presence_of_element_located((By.ID, "search"))).click()
        lecture(lecture_entry1.get(), lecture_entry12.get())
        lecture(lecture_entry2.get(), lecture_entry22.get())
        lecture(lecture_entry3.get(), lecture_entry32.get())
        lecture(lecture_entry4.get(), lecture_entry42.get())
        lecture(lecture_entry5.get(), lecture_entry52.get())

    except Exception as ec:
        print(ec)


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
major_var = IntVar(value=0)
major_checkbox = Checkbutton(main_frame, text="전공", variable=major_var)
major_checkbox.grid(row=1, column=2, sticky=W)
general_var = IntVar(value=0)
general_checkbox = Checkbutton(main_frame, text="교양", variable=general_var)
general_checkbox.grid(row=2, column=2, sticky=W)

start_button = Button(main_frame, text="시작", width=15, height=2, command=all_command)
start_button.grid(row=3, column=1)

code_label = Label(main_frame, text="과목코드")
code_label.grid(row=4, column=1)
class_label = Label(main_frame, text="분반")
class_label.grid(row=4, column=2)

lecture_label1 = Label(main_frame, text="과목 1")
lecture_label1.grid(row=5, column=0)
lecture_entry1 = Entry(main_frame, width=17)
lecture_entry1.grid(row=5, column=1)
lecture_entry12 = Entry(main_frame, width=17)
lecture_entry12.grid(row=5, column=2)
lecture_var1 = IntVar(value=0)
lecture_checkbox1 = Checkbutton(main_frame, variable=lecture_var1)
lecture_checkbox1.grid(row=5, column=3)

lecture_label2 = Label(main_frame, text="과목 2")
lecture_label2.grid(row=6, column=0)
lecture_entry2 = Entry(main_frame, width=17)
lecture_entry2.grid(row=6, column=1)
lecture_entry22 = Entry(main_frame, width=17)
lecture_entry22.grid(row=6, column=2)
lecture_var2 = IntVar(value=0)
lecture_checkbox2 = Checkbutton(main_frame, variable=lecture_var2)
lecture_checkbox2.grid(row=6, column=3)

lecture_label3 = Label(main_frame, text="과목 3")
lecture_label3.grid(row=7, column=0)
lecture_entry3 = Entry(main_frame, width=17)
lecture_entry3.grid(row=7, column=1)
lecture_entry32 = Entry(main_frame, width=17)
lecture_entry32.grid(row=7, column=2)
lecture_var3 = IntVar(value=0)
lecture_checkbox3 = Checkbutton(main_frame, variable=lecture_var3)
lecture_checkbox3.grid(row=7, column=3)

lecture_label4 = Label(main_frame, text="과목 4")
lecture_label4.grid(row=8, column=0)
lecture_entry4 = Entry(main_frame, width=17)
lecture_entry4.grid(row=8, column=1)
lecture_entry42 = Entry(main_frame, width=17)
lecture_entry42.grid(row=8, column=2)
lecture_var4 = IntVar(value=0)
lecture_checkbox4 = Checkbutton(main_frame, variable=lecture_var4)
lecture_checkbox4.grid(row=8, column=3)

lecture_label5 = Label(main_frame, text="과목 5")
lecture_label5.grid(row=9, column=0)
lecture_entry5 = Entry(main_frame, width=17)
lecture_entry5.grid(row=9, column=1)
lecture_entry52 = Entry(main_frame, width=17)
lecture_entry52.grid(row=9, column=2)
lecture_var5 = IntVar(value=0)
lecture_checkbox5 = Checkbutton(main_frame, variable=lecture_var5)
lecture_checkbox5.grid(row=9, column=3)

if __name__ == "__main__":
    id_entry.insert(0, "205113")
    pw_entry.insert(0, "990813")

dp.mainloop()
