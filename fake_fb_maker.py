from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import random
import pyperclip
import getpass

first_name = ["Lashonda","Nickie","Robbi","Young","Mignon","Hellen","Shelley","Earlean","Kathern","Ceola","Tamar","Carolyne","Randy","Filiberto","Antione","Leatrice","Keisha","Josie","Daren","Angel","Rachelle","Newton","Misha","Elba","Tessa","Landon","Alton","Angelena","Marget","Sherly","Kasi","Gregorio","Brendan","Viki","Alphonso","Tanesha","Mable","Sharda","Beau","Mafalda","Yen","Dorcas","Shera","Treasa","Jacques","Celina","Cristi","Harley","Zona","Justin","Hannah","Galina","Avery","Alverta","Laree","Alda","Velia","Mozella","Murray","Florencio","Demetrice","Anjelica","Tameika","Lan","Lynn","Rodrick","Dong","Halina","Aurora","Issac","Diego","Cris","Jaquelyn","Marianna","Marion","Elane","Maud","Mui","Margo","Caleb","Willy","Cruz","Rufus","Shizue","Sherice","Devorah","Phil","Elvin","Leoma","Obdulia","Hien","Isabell","Emerita","Michal","Prince","Blanca","Melodi"]

last_name = ["Stark","Hendricks","Calhoun","Heath","Kennedy","Zamora","Mckinney","Conley","Atkinson","Holmes","Costa","Blackburn","Clayton","Cochran","Hicks","Larson","Brewer","Tapia","Meadows","Reyes","Santana","Decker","Tran","Choi","Chandler","Gill","Chapman","Krause","Joseph","Pollard","Bolton","Wells","Gregory","Joyce","Schneider","Kramer","Bray","Huber","Hanson","Howe","Villa","Santos","Gilbert","Nichols","Mata","Patterson","Mays","Hull","Vincent","Kaufman","Case","Kline","Huffman","Wolf","Zimmerman","Walker","Riley","Stephenson","Koch","Ponce","Cooper","Mora","Hickman","Mckay","Olson","Mendez","Daniels","Buck","Raymond","Chan","Schaefer","Wise","Simpson","Chang","Hartman","Browning","Rubio","Kelly","Campbell","Tanner","Fields","Hood","Cardenas","Gomez","Cantrell","Bailey","Herring","Frazier","Bowers","Garza","Price","Oliver","Hammond","Figueroa","Wheeler","Nolan","Vance","Mathews","Kelley","Bernard"]

date = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
month = [1,2,3,4,5,6,7,8,9,10,11,12]
year = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,
37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116]
gender = ["u_0_9","u_0_a"]

fn = random.choice(first_name)
ln = random.choice(last_name)
dt = random.choice(date)
mt = random.choice(month)
yr = random.choice(year)
gd = random.choice(gender)
usr = getpass.getuser()
concat = r'C:\Users\\' + usr + r'\Desktop\\fake_fb_account.txt'

driver =  webdriver.Chrome()
driver.maximize_window()
driver.get("https://tempail.com/en/")
driver.find_element(By.CLASS_NAME,"adres-input").click()
driver.get("https://www.facebook.com")
driver.find_element(By.NAME,"firstname").send_keys(fn)
driver.find_element(By.NAME,"lastname").send_keys(ln)
driver.find_element(By.ID,"u_0_o").send_keys(Keys.CONTROL + "v")
driver.find_element(By.ID,"u_0_r").send_keys(Keys.CONTROL + "v")
driver.find_element(By.NAME,"reg_passwd__").send_keys(fn+ln+"@123")
obj1 = Select(driver.find_element(By.ID,"day"))
obj1.select_by_index(dt)
obj2 = Select(driver.find_element(By.ID,"month"))
obj2.select_by_index(mt)
obj3 = Select(driver.find_element(By.ID,"year"))
obj3.select_by_index(yr)
driver.find_element(By.ID,gd).click()
driver.find_element(By.NAME,"websubmit").click()
driver.execute_script("window.open('https://tempail.com/en')")
f = open(concat,"a")
f.write("Username : ")
f.close()
f = open(concat,"a")
f.write(pyperclip.paste())
f.close()
f = open(concat,"a")
f.write("\nPassword : ")
f.close()
f = open(concat,"a")
f.write(fn)
f.close()
f = open(concat,"a")
f.write(ln)
f.close()
f = open(concat,"a")
f.write("@123")
f.close()
