
from selenium import webdriver
from selenium.webdriver.chrome.options import  Options
from random import expovariate, seed
from random import random
from time import sleep, time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.keys import Keys
import pandas as pd
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager

# Create your views here.




chrome_options = webdriver.ChromeOptions()

chrome_options.add_argument('start-maximized')
# chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")

df = pd.read_excel("Master Index List A.xlsx",  engine ='openpyxl')
# print(df)

list_of_fields = ["fire department","police department",
            "gun range","whole foods near",
            "dollar store near","pawn shop near",
            "homeless shleter near","bike path near","army recruiter near","chinese restaurant near",
            "equestrian path near","golf course near","country club near","starbucks near"]


address_list=[]
name_list=[]
id_list=[]
List_list=[]
zip_list=[]

for i in range (317, len(df["Address"])):
    try:
        address=str(df["Address"][i]+str(df['City'][i])+str(df['State'][i]))
        # address=str(df["Address"][i])+str(df['City'])
        addresss=address
        # print("addresss => ", addresss)
        # id_list.append(i)
        
        
        print(address,"jkvjksfvjfdvfvfvjf")
        # time.sleep(15)
        # driver = webdriver.Chrome(executable_path=r"E:\football\chromedriver_win32\chromedriver.exe")
        # driver=webdriver.Chrome(ChromeDriverManager().install())
        driver=webdriver.Chrome(ChromeDriverManager().install(),chrome_options=chrome_options)

    
        driver.get('https://www.google.co.in/maps/@30.7396608,76.7328256,13z')
        # driver.maximize_window()
        driver.delete_all_cookies()  
        time.sleep(5)          
        WebDriverWait(driver,2).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="searchboxinput"]'))).send_keys(addresss)
        driver.find_element_by_xpath('//*[@id="searchboxinput"]').send_keys(Keys.ENTER)
        time.sleep(5)

        try:
            WebDriverWait(driver,2).until(EC.element_to_be_clickable((By.XPATH,'/html/body/jsl/div[3]/div[10]/div[8]/div/div[1]/div/div/div[4]/div[1]/div/button'))).click()
      
        except Exception as e:
            pass
        try:
            # WebDriverWait(driver,2).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="pane"]/div/div[1]/div/div/div[4]/div[1]/div[1]/div/a'))).click()

            #click on the direction button
            driver.find_element_by_xpath('//*[@id="pane"]/div/div[1]/div/div/div[4]/div[1]/button').click()

            # WebDriverWait(driver,2).until(EC.element_to_be_clickable((By.XPATH,'/html/body/jsl/div[3]/div[9]/div[8]/div/div[1]/div/div/div[4]/div[1]/div/button'))).click()
        except Exception as e:
            pass  
        
        # Button click for the change direction.
        WebDriverWait(driver,2).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="omnibox-directions"]/div/div[3]/div[2]/button/div'))).click()

        list_output=[]
        list_output.append(df['ID'][i])
        list_output.append(addresss)
        # Search keyword 
        for i in list_of_fields:
                                                                    
            # Clear input field for the search next keyword.
            driver.find_element_by_xpath('//*[@id="sb_ifc52"]/input').clear()            

            print(i+" "+addresss)
            WebDriverWait(driver,2).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="sb_ifc52"]/input'))).send_keys(i + " " +  addresss)
            # //*[@id="sb_ifc52"]/input

            driver.find_element_by_xpath('//*[@id="sb_ifc52"]/input').send_keys(Keys.ENTER)
            time.sleep(7)
            # res = driver.page_source
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            try:
                a = driver.find_element_by_xpath('/html/body/jsl/div[3]/div[10]/div[8]/div/div[1]/div/div/div[5]/div[1]/div/div[1]/div[1]/div[2]')
                print("a 1=> ", a.text)
            except Exception as e:
                pass

            try:
                a = driver.find_element_by_xpath('//*[@id="section-directions-trip-0"]/div/div[3]/div[1]/div[2]')
                print("a 2=> ", a.text)
            except Exception as e:
                pass

            try:
                a = driver.find_element_by_xpath('//*[@id="section-directions-trip-0"]/div/div[1]/div[1]/div[2]/div')
            except Exception as e:
                pass            
            if a:
                try:
                    list_output.append(a.text)
                    print(a.text)
                except:
                    
                    list_output.append("NA")
            else:
                list_output.append("NA")

        # print(id_list)
        print(address)
        df1=pd.DataFrame([list_output])
        df1.to_csv('new_master_list_output.csv',header=False , index=False ,mode='a')
        print("List Output => ", list_output, address)
        

        list_output.clear()
        id_list.clear()
        # zip_list.clear()
        # List_list.clear()
        name_list.clear()
        address_list.clear()
        driver.close()

    except Exception as e:
        print("Error :",e)
        pass
        
