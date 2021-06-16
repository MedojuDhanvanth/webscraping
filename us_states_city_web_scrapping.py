#!/usr/bin/env python
# coding: utf-8

# In[4]:


#pip install selenium
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd


# In[7]:


pip install selenium  


# In[198]:


#driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
#driver = webdriver.Chrome("C:/Program Files/Google/Chrome/Application/chromedriver.exe")
driver = webdriver.Chrome(executable_path=r'C:/Users/Sony/Downloads/chromedriver_win32/chromedriver.exe')


# In[30]:


driver.get('https://community.powerbi.com/t5/Data-Stories-Gallery/bd-p/DataStoriesGallery')
time.sleep(10)


# In[29]:


import time


# In[32]:


print("Printed immediately.")
time.sleep(5.4)
print("Printed after 2.4 seconds.")


# In[99]:


driver.get('https://www.google.com/search?q=newyork+timezone')
#driver.get('https://en.wikipedia.org/wiki/2020_in_film')
#c=driver.find_element_by_id('<h1 id="firstHeading" class="firstHeading">2020 in film</h1>')

c=driver.find_element_by_xpath("//div[2]/div[2]/div/div/div/div/div/div/div")
d=driver.find_element_by_xpath("//div[2]/div/div/div/div/div/div/div[2]")
print(c.text,"        ",d.text)


# In[122]:


r=[]
list = ['newyork timezone','texas timezone','alabama timezone' ]
# Using for loop
for i in list:
    print('https://www.google.com/search?q=',i)
    r.append(i) 
print(r)
#print(k)


# In[130]:


links=['https://www.google.com/search?q=newyork timezone','https://www.google.com/search?q=texas timezone',
       'https://www.google.com/search?q= alabama timezone']
links
for i in links:
    driver.get(i)
#driver.get('https://en.wikipedia.org/wiki/2020_in_film')
#c=driver.find_element_by_id('<h1 id="firstHeading" class="firstHeading">2020 in film</h1>')

    c=driver.find_element_by_xpath("//div[2]/div[2]/div/div/div/div/div/div/div")
    d=driver.find_element_by_xpath("//div[2]/div/div/div/div/div/div/div[2]")
    print(i[-16:],c.text,"        ",d.text)
    #print(i[:32],c.text)
    print(i.split("?q=",1)[1],",",c.text,",")


# In[129]:


links


# In[194]:


links=['https://www.google.com/search?q=Alaska Adak timezone',
'https://www.google.com/search?q=Alaska Akiachak timezone',
'https://www.google.com/search?q=Alaska Akiak timezone',
'https://www.google.com/search?q=Alaska Akutan timezone',
'https://www.google.com/search?q=Alaska Alakanuk timezone',
'https://www.google.com/search?q=Alaska Aleknagik timezone',
'https://www.google.com/search?q=Alaska Allakaket timezone',
'https://www.google.com/search?q=Alaska Ambler timezone',
'https://www.google.com/search?q=Alaska Anaktuvuk Pass timezone',
'https://www.google.com/search?q=Alaska Anchor Point timezone',
'https://www.google.com/search?q=Alaska Anchorage timezone',
'https://www.google.com/search?q=Alaska Anderson timezone',
'https://www.google.com/search?q=Alaska Angoon timezone',
'https://www.google.com/search?q=Alaska Aniak timezone',
'https://www.google.com/search?q=Alaska Anvik timezone',
'https://www.google.com/search?q=Alaska Arctic Village timezone',
'https://www.google.com/search?q=Alaska Atka timezone',
'https://www.google.com/search?q=Alaska Atqasuk timezone',
'https://www.google.com/search?q=Alaska Auke Bay timezone',
'https://www.google.com/search?q=Alaska Barrow timezone',
'https://www.google.com/search?q=Alaska Beaver timezone',
'https://www.google.com/search?q=Alaska Bethel timezone',
'https://www.google.com/search?q=Alaska Bettles Field timezone',
'https://www.google.com/search?q=Alaska Big Lake timezone',
'https://www.google.com/search?q=Alaska Brevig Mission timezone',
'https://www.google.com/search?q=Alaska Buckland timezone',
'https://www.google.com/search?q=Alaska Cantwell timezone',
'https://www.google.com/search?q=Alaska Central timezone',
'https://www.google.com/search?q=Alaska Chalkyitsik timezone',
'https://www.google.com/search?q=Alaska Chefornak timezone',
'https://www.google.com/search?q=Alaska Chevak timezone',
'https://www.google.com/search?q=Alaska Chicken timezone',
'https://www.google.com/search?q=Alaska Chignik timezone',
'https://www.google.com/search?q=Alaska Chignik Lagoon timezone',
'https://www.google.com/search?q=Alaska Chignik Lake timezone',
'https://www.google.com/search?q=Alaska Chitina timezone',
'https://www.google.com/search?q=Alaska Chugiak timezone',
'https://www.google.com/search?q=Alaska Circle timezone',
'https://www.google.com/search?q=Alaska Clam Gulch timezone',
'https://www.google.com/search?q=Alaska Clarks Point timezone',
'https://www.google.com/search?q=Alaska Clear timezone',
'https://www.google.com/search?q=Alaska Coffman Cove timezone',
'https://www.google.com/search?q=Alaska Cold Bay timezone',
'https://www.google.com/search?q=Alaska Cooper Landing timezone',
'https://www.google.com/search?q=Alaska Copper Center timezone',
'https://www.google.com/search?q=Alaska Cordova timezone',
'https://www.google.com/search?q=Alaska Craig timezone',
'https://www.google.com/search?q=Alaska Crooked Creek timezone',
'https://www.google.com/search?q=Alaska Deering timezone',
'https://www.google.com/search?q=Alaska Delta Junction timezone',
'https://www.google.com/search?q=Alaska Denali National Park timezone',
'https://www.google.com/search?q=Alaska Dillingham timezone',
'https://www.google.com/search?q=Alaska Douglas timezone',
'https://www.google.com/search?q=Alaska Dutch Harbor timezone',
'https://www.google.com/search?q=Alaska Eagle timezone',
'https://www.google.com/search?q=Alaska Eagle River timezone',
'https://www.google.com/search?q=Alaska Eek timezone',
'https://www.google.com/search?q=Alaska Egegik timezone',
'https://www.google.com/search?q=Alaska Eielson Afb timezone']
links
for i in links:
    driver.get(i)
#driver.get('https://en.wikipedia.org/wiki/2020_in_film')
#c=driver.find_element_by_id('<h1 id="firstHeading" class="firstHeading">2020 in film</h1>')

    c=driver.find_element_by_xpath("//div[2]/div[2]/div/div/div/div/div/div/div")
    #d=driver.find_element_by_xpath("//div[2]/div/div/div/div/div/div/div[2]")
    #print(i[:32],c.text)
    print(i.split("?q=",1)[1],",",c.text,",")
    
    


# In[187]:


my_string="hello python world i'm a beginner "
print(my_string.split("world",1)[1])


# In[200]:


links=['https://www.google.com/search?q=Alaska Adak timezone',
'https://www.google.com/search?q=Alaska Akiachak timezone',
'https://www.google.com/search?q=Alaska Akiak timezone',
'https://www.google.com/search?q=Alaska Akutan timezone',
'https://www.google.com/search?q=Alaska Alakanuk timezone',
'https://www.google.com/search?q=Alaska Aleknagik timezone',
'https://www.google.com/search?q=Alaska Allakaket timezone',
'https://www.google.com/search?q=Alaska Ambler timezone',
'https://www.google.com/search?q=Alaska Anaktuvuk Pass timezone',
'https://www.google.com/search?q=Alaska Anchor Point timezone',
'https://www.google.com/search?q=Alaska Anchorage timezone',
'https://www.google.com/search?q=Alaska Anderson timezone',
'https://www.google.com/search?q=Alaska Angoon timezone',
'https://www.google.com/search?q=Alaska Aniak timezone',
'https://www.google.com/search?q=Alaska Anvik timezone',
'https://www.google.com/search?q=Alaska Arctic Village timezone',
'https://www.google.com/search?q=Alaska Atka timezone',
'https://www.google.com/search?q=Alaska Atqasuk timezone',
'https://www.google.com/search?q=Alaska Auke Bay timezone',
'https://www.google.com/search?q=Alaska Barrow timezone',
'https://www.google.com/search?q=Alaska Beaver timezone',
'https://www.google.com/search?q=Alaska Bethel timezone',
'https://www.google.com/search?q=Alaska Bettles Field timezone',
'https://www.google.com/search?q=Alaska Big Lake timezone',
'https://www.google.com/search?q=Alaska Brevig Mission timezone',
'https://www.google.com/search?q=Alaska Buckland timezone',
'https://www.google.com/search?q=Alaska Cantwell timezone',
'https://www.google.com/search?q=Alaska Central timezone',
'https://www.google.com/search?q=Alaska Chalkyitsik timezone',
'https://www.google.com/search?q=Alaska Chefornak timezone',
'https://www.google.com/search?q=Alaska Chevak timezone',
'https://www.google.com/search?q=Alaska Chicken timezone',
'https://www.google.com/search?q=Alaska Chignik timezone',
'https://www.google.com/search?q=Alaska Chignik Lagoon timezone',
'https://www.google.com/search?q=Alaska Chignik Lake timezone',
'https://www.google.com/search?q=Alaska Chitina timezone',
'https://www.google.com/search?q=Alaska Chugiak timezone',
'https://www.google.com/search?q=Alaska Circle timezone',
'https://www.google.com/search?q=Alaska Clam Gulch timezone',
'https://www.google.com/search?q=Alaska Clarks Point timezone',
'https://www.google.com/search?q=Alaska Clear timezone',
'https://www.google.com/search?q=Alaska Coffman Cove timezone',
'https://www.google.com/search?q=Alaska Cold Bay timezone',
'https://www.google.com/search?q=Alaska Cooper Landing timezone',
'https://www.google.com/search?q=Alaska Copper Center timezone',
'https://www.google.com/search?q=Alaska Cordova timezone',
'https://www.google.com/search?q=Alaska Craig timezone',
'https://www.google.com/search?q=Alaska Crooked Creek timezone',
'https://www.google.com/search?q=Alaska Deering timezone',
'https://www.google.com/search?q=Alaska Delta Junction timezone',
'https://www.google.com/search?q=Alaska Dillingham timezone',
'https://www.google.com/search?q=Alaska Douglas timezone',
'https://www.google.com/search?q=Alaska Dutch Harbor timezone',
'https://www.google.com/search?q=Alaska Eagle timezone',
'https://www.google.com/search?q=Alaska Eagle River timezone',
'https://www.google.com/search?q=Alaska Eek timezone',
'https://www.google.com/search?q=Alaska Egegik timezone',
'https://www.google.com/search?q=Alaska Eielson Afb timezone']
links
for i in links:
    driver.get(i)
#driver.get('https://en.wikipedia.org/wiki/2020_in_film')
#c=driver.find_element_by_id('<h1 id="firstHeading" class="firstHeading">2020 in film</h1>')

    c=driver.find_element_by_xpath("//div[2]/div[2]/div/div/div/div/div/div/div")
    time.sleep(1)
    #d=driver.find_element_by_xpath("//div[2]/div/div/div/div/div/div/div[2]")
    #print(i[:32],c.text)
    print(i.split("?q=",1)[1],",",c.text,",")
print("completed")


# In[201]:


links=['https://www.google.com/search?q=Alaska Ekwok timezone',
'https://www.google.com/search?q=Alaska Elfin Cove timezone',
'https://www.google.com/search?q=Alaska Elim timezone',
'https://www.google.com/search?q=Alaska Elmendorf Afb timezone',
'https://www.google.com/search?q=Alaska Emmonak timezone',
'https://www.google.com/search?q=Alaska Ester timezone',
'https://www.google.com/search?q=Alaska Fairbanks timezone',
'https://www.google.com/search?q=Alaska False Pass timezone',
'https://www.google.com/search?q=Alaska Fort Greely timezone',
'https://www.google.com/search?q=Alaska Fort Richardson timezone',
'https://www.google.com/search?q=Alaska Fort Wainwright timezone',
'https://www.google.com/search?q=Alaska Fort Yukon timezone',
'https://www.google.com/search?q=Alaska Gakona timezone',
'https://www.google.com/search?q=Alaska Galena timezone',
'https://www.google.com/search?q=Alaska Gambell timezone',
'https://www.google.com/search?q=Alaska Girdwood timezone',
'https://www.google.com/search?q=Alaska Glennallen timezone',
'https://www.google.com/search?q=Alaska Goodnews Bay timezone',
'https://www.google.com/search?q=Alaska Grayling timezone',
'https://www.google.com/search?q=Alaska Gustavus timezone',
'https://www.google.com/search?q=Alaska Haines timezone',
'https://www.google.com/search?q=Alaska Healy timezone',
'https://www.google.com/search?q=Alaska Holy Cross timezone',
'https://www.google.com/search?q=Alaska Homer timezone',
'https://www.google.com/search?q=Alaska Hoonah timezone',
'https://www.google.com/search?q=Alaska Hooper Bay timezone',
'https://www.google.com/search?q=Alaska Hope timezone',
'https://www.google.com/search?q=Alaska Houston timezone',
'https://www.google.com/search?q=Alaska Hughes timezone',
'https://www.google.com/search?q=Alaska Huslia timezone',
'https://www.google.com/search?q=Alaska Hydaburg timezone',
'https://www.google.com/search?q=Alaska Hyder timezone',
'https://www.google.com/search?q=Alaska Iliamna timezone',
'https://www.google.com/search?q=Alaska Indian timezone',
'https://www.google.com/search?q=Alaska Juneau timezone',
'https://www.google.com/search?q=Alaska Kake timezone',
'https://www.google.com/search?q=Alaska Kaktovik timezone',
'https://www.google.com/search?q=Alaska Kalskag timezone',
'https://www.google.com/search?q=Alaska Kaltag timezone',
'https://www.google.com/search?q=Alaska Karluk timezone',
'https://www.google.com/search?q=Alaska Kasigluk timezone',
'https://www.google.com/search?q=Alaska Kasilof timezone',
'https://www.google.com/search?q=Alaska Kenai timezone',
'https://www.google.com/search?q=Alaska Ketchikan timezone',
'https://www.google.com/search?q=Alaska Kiana timezone',
'https://www.google.com/search?q=Alaska King Cove timezone',
'https://www.google.com/search?q=Alaska King Salmon timezone',
'https://www.google.com/search?q=Alaska Kipnuk timezone',
'https://www.google.com/search?q=Alaska Kivalina timezone',
'https://www.google.com/search?q=Alaska Klawock timezone',
'https://www.google.com/search?q=Alaska Kobuk timezone',
'https://www.google.com/search?q=Alaska Kodiak timezone',
'https://www.google.com/search?q=Alaska Kongiganak timezone',
'https://www.google.com/search?q=Alaska Kotlik timezone',
'https://www.google.com/search?q=Alaska Kotzebue timezone',
'https://www.google.com/search?q=Alaska Koyuk timezone',
'https://www.google.com/search?q=Alaska Koyukuk timezone',
'https://www.google.com/search?q=Alaska Kwethluk timezone',
'https://www.google.com/search?q=Alaska Kwigillingok timezone',
'https://www.google.com/search?q=Alaska Lake Minchumina timezone',
'https://www.google.com/search?q=Alaska Larsen Bay timezone',
'https://www.google.com/search?q=Alaska Levelock timezone',
'https://www.google.com/search?q=Alaska Lower Kalskag timezone',
'https://www.google.com/search?q=Alaska Manley Hot Springs timezone',
'https://www.google.com/search?q=Alaska Manokotak timezone',
'https://www.google.com/search?q=Alaska Marshall timezone',
'https://www.google.com/search?q=Alaska Mc Grath timezone',
'https://www.google.com/search?q=Alaska Mekoryuk timezone',
'https://www.google.com/search?q=Alaska Metlakatla timezone',
'https://www.google.com/search?q=Alaska Meyers Chuck timezone',
'https://www.google.com/search?q=Alaska Minto timezone',
'https://www.google.com/search?q=Alaska Moose Pass timezone',
'https://www.google.com/search?q=Alaska Mountain Village timezone',
'https://www.google.com/search?q=Alaska Naknek timezone',
'https://www.google.com/search?q=Alaska Napakiak timezone',
'https://www.google.com/search?q=Alaska Nenana timezone',
'https://www.google.com/search?q=Alaska New Stuyahok timezone',
'https://www.google.com/search?q=Alaska Nightmute timezone',
'https://www.google.com/search?q=Alaska Nikiski timezone',
'https://www.google.com/search?q=Alaska Nikolai timezone',
'https://www.google.com/search?q=Alaska Nikolski timezone',
'https://www.google.com/search?q=Alaska Ninilchik timezone',
'https://www.google.com/search?q=Alaska Noatak timezone',
'https://www.google.com/search?q=Alaska Nome timezone',
'https://www.google.com/search?q=Alaska Nondalton timezone',
'https://www.google.com/search?q=Alaska Noorvik timezone',
'https://www.google.com/search?q=Alaska North Pole timezone',
'https://www.google.com/search?q=Alaska Northway timezone',
'https://www.google.com/search?q=Alaska Nuiqsut timezone',
'https://www.google.com/search?q=Alaska Nulato timezone',
'https://www.google.com/search?q=Alaska Nunam Iqua timezone',
'https://www.google.com/search?q=Alaska Nunapitchuk timezone',
'https://www.google.com/search?q=Alaska Old Harbor timezone',
'https://www.google.com/search?q=Alaska Ouzinkie timezone',
'https://www.google.com/search?q=Alaska Palmer timezone',
'https://www.google.com/search?q=Alaska Pedro Bay timezone',
'https://www.google.com/search?q=Alaska Pelican timezone',
'https://www.google.com/search?q=Alaska Perryville timezone',
'https://www.google.com/search?q=Alaska Petersburg timezone',
'https://www.google.com/search?q=Alaska Pilot Point timezone',
'https://www.google.com/search?q=Alaska Pilot Station timezone',
'https://www.google.com/search?q=Alaska Platinum timezone',
'https://www.google.com/search?q=Alaska Point Baker timezone',
'https://www.google.com/search?q=Alaska Point Hope timezone',
'https://www.google.com/search?q=Alaska Point Lay timezone',
'https://www.google.com/search?q=Alaska Port Alexander timezone',
'https://www.google.com/search?q=Alaska Port Alsworth timezone',
'https://www.google.com/search?q=Alaska Port Heiden timezone',
'https://www.google.com/search?q=Alaska Port Lions timezone',
'https://www.google.com/search?q=Alaska Prudhoe Bay timezone',
'https://www.google.com/search?q=Alaska Quinhagak timezone',
'https://www.google.com/search?q=Alaska Rampart timezone',
'https://www.google.com/search?q=Alaska Red Devil timezone',
'https://www.google.com/search?q=Alaska Ruby timezone',
'https://www.google.com/search?q=Alaska Russian Mission timezone',
'https://www.google.com/search?q=Alaska Saint George Island timezone',
'https://www.google.com/search?q=Alaska Saint Marys timezone',
'https://www.google.com/search?q=Alaska Saint Michael timezone',
'https://www.google.com/search?q=Alaska Saint Paul Island timezone',
'https://www.google.com/search?q=Alaska Salcha timezone',
'https://www.google.com/search?q=Alaska Sand Point timezone',
'https://www.google.com/search?q=Alaska Savoonga timezone',
'https://www.google.com/search?q=Alaska Scammon Bay timezone',
'https://www.google.com/search?q=Alaska Selawik timezone',
'https://www.google.com/search?q=Alaska Seldovia timezone',
'https://www.google.com/search?q=Alaska Seward timezone',
'https://www.google.com/search?q=Alaska Shageluk timezone',
'https://www.google.com/search?q=Alaska Shaktoolik timezone',
'https://www.google.com/search?q=Alaska Shishmaref timezone',
'https://www.google.com/search?q=Alaska Shungnak timezone',
'https://www.google.com/search?q=Alaska Sitka timezone',
'https://www.google.com/search?q=Alaska Skagway timezone',
'https://www.google.com/search?q=Alaska Skwentna timezone',
'https://www.google.com/search?q=Alaska Sleetmute timezone',
'https://www.google.com/search?q=Alaska Soldotna timezone',
'https://www.google.com/search?q=Alaska South Naknek timezone',
'https://www.google.com/search?q=Alaska Stebbins timezone',
'https://www.google.com/search?q=Alaska Sterling timezone',
'https://www.google.com/search?q=Alaska Stevens Village timezone',
'https://www.google.com/search?q=Alaska Sutton timezone',
'https://www.google.com/search?q=Alaska Takotna timezone',
'https://www.google.com/search?q=Alaska Talkeetna timezone',
'https://www.google.com/search?q=Alaska Tanacross timezone',
'https://www.google.com/search?q=Alaska Tanana timezone',
'https://www.google.com/search?q=Alaska Tatitlek timezone',
'https://www.google.com/search?q=Alaska Teller timezone',
'https://www.google.com/search?q=Alaska Tenakee Springs timezone',
'https://www.google.com/search?q=Alaska Thorne Bay timezone',
'https://www.google.com/search?q=Alaska Togiak timezone',
'https://www.google.com/search?q=Alaska Tok timezone',
'https://www.google.com/search?q=Alaska Toksook Bay timezone',
'https://www.google.com/search?q=Alaska Trapper Creek timezone',
'https://www.google.com/search?q=Alaska Tuluksak timezone',
'https://www.google.com/search?q=Alaska Tuntutuliak timezone',
'https://www.google.com/search?q=Alaska Tununak timezone',
'https://www.google.com/search?q=Alaska Two Rivers timezone',
'https://www.google.com/search?q=Alaska Tyonek timezone',
'https://www.google.com/search?q=Alaska Unalakleet timezone',
'https://www.google.com/search?q=Alaska Unalaska timezone',
'https://www.google.com/search?q=Alaska Valdez timezone',
'https://www.google.com/search?q=Alaska Venetie timezone',
'https://www.google.com/search?q=Alaska Wainwright timezone',
'https://www.google.com/search?q=Alaska Wales timezone',
'https://www.google.com/search?q=Alaska Ward Cove timezone',
'https://www.google.com/search?q=Alaska Wasilla timezone',
'https://www.google.com/search?q=Alaska White Mountain timezone',
'https://www.google.com/search?q=Alaska Whittier timezone',
'https://www.google.com/search?q=Alaska Willow timezone',
'https://www.google.com/search?q=Alaska Wrangell timezone',
'https://www.google.com/search?q=Alaska Yakutat timezone',
'https://www.google.com/search?q=Alabama Abbeville timezone',
'https://www.google.com/search?q=Alabama Abernant timezone',
'https://www.google.com/search?q=Alabama Adamsville timezone',
'https://www.google.com/search?q=Alabama Addison timezone',
'https://www.google.com/search?q=Alabama Adger timezone',
'https://www.google.com/search?q=Alabama Akron timezone',
'https://www.google.com/search?q=Alabama Alabaster timezone',
'https://www.google.com/search?q=Alabama Alberta timezone',
'https://www.google.com/search?q=Alabama Albertville timezone',
'https://www.google.com/search?q=Alabama Alexander City timezone',
'https://www.google.com/search?q=Alabama Alexandria timezone',
'https://www.google.com/search?q=Alabama Aliceville timezone',
'https://www.google.com/search?q=Alabama Allgood timezone',
'https://www.google.com/search?q=Alabama Alma timezone',
'https://www.google.com/search?q=Alabama Alpine timezone',
'https://www.google.com/search?q=Alabama Alton timezone',
'https://www.google.com/search?q=Alabama Altoona timezone',
'https://www.google.com/search?q=Alabama Andalusia timezone',
'https://www.google.com/search?q=Alabama Anderson timezone',
'https://www.google.com/search?q=Alabama Annemanie timezone',
'https://www.google.com/search?q=Alabama Anniston timezone',
'https://www.google.com/search?q=Alabama Arab timezone',
'https://www.google.com/search?q=Alabama Ardmore timezone',
'https://www.google.com/search?q=Alabama Ariton timezone',
'https://www.google.com/search?q=Alabama Arley timezone',
'https://www.google.com/search?q=Alabama Arlington timezone',
'https://www.google.com/search?q=Alabama Ashford timezone',
'https://www.google.com/search?q=Alabama Ashland timezone',
'https://www.google.com/search?q=Alabama Ashville timezone',
'https://www.google.com/search?q=Alabama Athens timezone',
'https://www.google.com/search?q=Alabama Atmore timezone',
'https://www.google.com/search?q=Alabama Attalla timezone',
'https://www.google.com/search?q=Alabama Auburn timezone',
'https://www.google.com/search?q=Alabama Auburn University timezone',
'https://www.google.com/search?q=Alabama Autaugaville timezone',
'https://www.google.com/search?q=Alabama Axis timezone',
'https://www.google.com/search?q=Alabama Baileyton timezone',
'https://www.google.com/search?q=Alabama Banks timezone',
'https://www.google.com/search?q=Alabama Bankston timezone',
'https://www.google.com/search?q=Alabama Bay Minette timezone',
'https://www.google.com/search?q=Alabama Bayou La Batre timezone',
'https://www.google.com/search?q=Alabama Bear Creek timezone',
'https://www.google.com/search?q=Alabama Beatrice timezone',
'https://www.google.com/search?q=Alabama Beaverton timezone',
'https://www.google.com/search?q=Alabama Belk timezone',
'https://www.google.com/search?q=Alabama Bellamy timezone',
'https://www.google.com/search?q=Alabama Belle Mina timezone',
'https://www.google.com/search?q=Alabama Bellwood timezone',
'https://www.google.com/search?q=Alabama Berry timezone',
'https://www.google.com/search?q=Alabama Bessemer timezone',
'https://www.google.com/search?q=Alabama Billingsley timezone',
'https://www.google.com/search?q=Alabama Birmingham timezone',
'https://www.google.com/search?q=Alabama Birmingham timezone',
'https://www.google.com/search?q=Alabama Black timezone',
'https://www.google.com/search?q=Alabama Blountsville timezone',
'https://www.google.com/search?q=Alabama Boaz timezone',
'https://www.google.com/search?q=Alabama Boaz timezone',
'https://www.google.com/search?q=Alabama Boligee timezone',
'https://www.google.com/search?q=Alabama Bon Air timezone',
'https://www.google.com/search?q=Alabama Bon Secour timezone',
'https://www.google.com/search?q=Alabama Booth timezone',
'https://www.google.com/search?q=Alabama Boykin timezone',
'https://www.google.com/search?q=Alabama Brantley timezone',
'https://www.google.com/search?q=Alabama Bremen timezone',
'https://www.google.com/search?q=Alabama Brent timezone',
'https://www.google.com/search?q=Alabama Brewton timezone',
'https://www.google.com/search?q=Alabama Bridgeport timezone',
'https://www.google.com/search?q=Alabama Brierfield timezone',
'https://www.google.com/search?q=Alabama Brilliant timezone',
'https://www.google.com/search?q=Alabama Brooklyn timezone',
'https://www.google.com/search?q=Alabama Brookside timezone',
'https://www.google.com/search?q=Alabama Brookwood timezone',
'https://www.google.com/search?q=Alabama Brownsboro timezone',
'https://www.google.com/search?q=Alabama Brundidge timezone',
'https://www.google.com/search?q=Alabama Bryant timezone',
'https://www.google.com/search?q=Alabama Bucks timezone',
'https://www.google.com/search?q=Alabama Buhl timezone',
'https://www.google.com/search?q=Alabama Burnt Corn timezone',
'https://www.google.com/search?q=Alabama Burnwell timezone',
'https://www.google.com/search?q=Alabama Butler timezone',
'https://www.google.com/search?q=Alabama Bynum timezone',
'https://www.google.com/search?q=Alabama Calera timezone',
'https://www.google.com/search?q=Alabama Calvert timezone',
'https://www.google.com/search?q=Alabama Camden timezone',
'https://www.google.com/search?q=Alabama Camp Hill timezone',
'https://www.google.com/search?q=Alabama Campbell timezone',
'https://www.google.com/search?q=Alabama Capshaw timezone',
'https://www.google.com/search?q=Alabama Carbon Hill timezone',
'https://www.google.com/search?q=Alabama Cardiff timezone',
'https://www.google.com/search?q=Alabama Carlton timezone',
'https://www.google.com/search?q=Alabama Carrollton timezone',
'https://www.google.com/search?q=Alabama Castleberry timezone',
'https://www.google.com/search?q=Alabama Catherine timezone',
'https://www.google.com/search?q=Alabama Cecil timezone',
'https://www.google.com/search?q=Alabama Cedar Bluff timezone',
'https://www.google.com/search?q=Alabama Centre timezone',
'https://www.google.com/search?q=Alabama Centreville timezone',
'https://www.google.com/search?q=Alabama Chancellor timezone',
'https://www.google.com/search?q=Alabama Chapman timezone',
'https://www.google.com/search?q=Alabama Chatom timezone',
'https://www.google.com/search?q=Alabama Chelsea timezone',
'https://www.google.com/search?q=Alabama Cherokee timezone',
'https://www.google.com/search?q=Alabama Childersburg timezone',
'https://www.google.com/search?q=Alabama Choccolocco timezone',
'https://www.google.com/search?q=Alabama Chunchula timezone',
'https://www.google.com/search?q=Alabama Citronelle timezone',
'https://www.google.com/search?q=Alabama Clanton timezone',
'https://www.google.com/search?q=Alabama Clay timezone',
'https://www.google.com/search?q=Alabama Clayton timezone',
'https://www.google.com/search?q=Alabama Cleveland timezone',
'https://www.google.com/search?q=Alabama Clinton timezone',
'https://www.google.com/search?q=Alabama Clio timezone',
'https://www.google.com/search?q=Alabama Clopton timezone',
'https://www.google.com/search?q=Alabama Cloverdale timezone',
'https://www.google.com/search?q=Alabama Coaling timezone',
'https://www.google.com/search?q=Alabama Coden timezone',
'https://www.google.com/search?q=Alabama Coffee Springs timezone',
'https://www.google.com/search?q=Alabama Coffeeville timezone',
'https://www.google.com/search?q=Alabama Coker timezone',
'https://www.google.com/search?q=Alabama Collinsville timezone',
'https://www.google.com/search?q=Alabama Columbia timezone',
'https://www.google.com/search?q=Alabama Columbiana timezone',
'https://www.google.com/search?q=Alabama Cook Springs timezone',
'https://www.google.com/search?q=Alabama Coosada timezone',
'https://www.google.com/search?q=Alabama Cordova timezone',
'https://www.google.com/search?q=Alabama Cottondale timezone',
'https://www.google.com/search?q=Alabama Cottonton timezone',
'https://www.google.com/search?q=Alabama Cottonwood timezone',
'https://www.google.com/search?q=Alabama Courtland timezone',
'https://www.google.com/search?q=Alabama Cowarts timezone',
'https://www.google.com/search?q=Alabama Coy timezone',
'https://www.google.com/search?q=Alabama Cragford timezone',
'https://www.google.com/search?q=Alabama Crane Hill timezone',
'https://www.google.com/search?q=Alabama Creola timezone',
'https://www.google.com/search?q=Alabama Cropwell timezone',
'https://www.google.com/search?q=Alabama Crossville timezone',
'https://www.google.com/search?q=Alabama Cuba timezone',
'https://www.google.com/search?q=Alabama Cullman timezone',
'https://www.google.com/search?q=Alabama Cusseta timezone',
'https://www.google.com/search?q=Alabama Dadeville timezone',
'https://www.google.com/search?q=Alabama Daleville timezone',
'https://www.google.com/search?q=Alabama Danville timezone',
'https://www.google.com/search?q=Alabama Daphne timezone',
'https://www.google.com/search?q=Alabama Dauphin Island timezone',
'https://www.google.com/search?q=Alabama Daviston timezone',
'https://www.google.com/search?q=Alabama Dawson timezone',
'https://www.google.com/search?q=Alabama De Armanville timezone',
'https://www.google.com/search?q=Alabama Deatsville timezone',
'https://www.google.com/search?q=Alabama Decatur timezone',
'https://www.google.com/search?q=Alabama Deer Park timezone',
'https://www.google.com/search?q=Alabama Delmar timezone',
'https://www.google.com/search?q=Alabama Delta timezone',
'https://www.google.com/search?q=Alabama Demopolis timezone',
'https://www.google.com/search?q=Alabama Detroit timezone',
'https://www.google.com/search?q=Alabama Dickinson timezone',
'https://www.google.com/search?q=Alabama Dixons Mills timezone',
'https://www.google.com/search?q=Alabama Docena timezone',
'https://www.google.com/search?q=Alabama Dolomite timezone',
'https://www.google.com/search?q=Alabama Dora timezone',
'https://www.google.com/search?q=Alabama Dothan timezone',
'https://www.google.com/search?q=Alabama Double Springs timezone',
'https://www.google.com/search?q=Alabama Douglas timezone',
'https://www.google.com/search?q=Alabama Dozier timezone',
'https://www.google.com/search?q=Alabama Duncanville timezone',
'https://www.google.com/search?q=Alabama Dutton timezone',
'https://www.google.com/search?q=Alabama East Tallassee timezone',
'https://www.google.com/search?q=Alabama Eastaboga timezone',
'https://www.google.com/search?q=Alabama Echola timezone',
'https://www.google.com/search?q=Alabama Eclectic timezone',
'https://www.google.com/search?q=Alabama Edwardsville timezone',
'https://www.google.com/search?q=Alabama Eight Mile timezone',
'https://www.google.com/search?q=Alabama Elba timezone',
'https://www.google.com/search?q=Alabama Elberta timezone',
'https://www.google.com/search?q=Alabama Eldridge timezone',
'https://www.google.com/search?q=Alabama Elkmont timezone',
'https://www.google.com/search?q=Alabama Elmore timezone',
'https://www.google.com/search?q=Alabama Elrod timezone',
'https://www.google.com/search?q=Alabama Emelle timezone',
'https://www.google.com/search?q=Alabama Empire timezone',
'https://www.google.com/search?q=Alabama Enterprise timezone',
'https://www.google.com/search?q=Alabama Epes timezone',
'https://www.google.com/search?q=Alabama Equality timezone',
'https://www.google.com/search?q=Alabama Estillfork timezone',
'https://www.google.com/search?q=Alabama Ethelsville timezone',
'https://www.google.com/search?q=Alabama Eufaula timezone',
'https://www.google.com/search?q=Alabama Eutaw timezone',
'https://www.google.com/search?q=Alabama Eva timezone',
'https://www.google.com/search?q=Alabama Excel timezone',
'https://www.google.com/search?q=Alabama Fackler timezone',
'https://www.google.com/search?q=Alabama Fairfield timezone',
'https://www.google.com/search?q=Alabama Fairhope timezone',
'https://www.google.com/search?q=Alabama Falkville timezone',
'https://www.google.com/search?q=Alabama Faunsdale timezone',
'https://www.google.com/search?q=Alabama Fayette timezone',
'https://www.google.com/search?q=Alabama Fitzpatrick timezone',
'https://www.google.com/search?q=Alabama Five Points timezone',
'https://www.google.com/search?q=Alabama Flat Rock timezone',
'https://www.google.com/search?q=Alabama Flomaton timezone',
'https://www.google.com/search?q=Alabama Florala timezone',
'https://www.google.com/search?q=Alabama Florence timezone',
'https://www.google.com/search?q=Alabama Foley timezone',
'https://www.google.com/search?q=Alabama Forest Home timezone',
'https://www.google.com/search?q=Alabama Forkland timezone',
'https://www.google.com/search?q=Alabama Fort Davis timezone',
'https://www.google.com/search?q=Alabama Fort Deposit timezone',
'https://www.google.com/search?q=Alabama Fort Mitchell timezone',
'https://www.google.com/search?q=Alabama Fort Payne timezone',
'https://www.google.com/search?q=Alabama Fort Rucker timezone',
'https://www.google.com/search?q=Alabama Fosters timezone',
'https://www.google.com/search?q=Alabama Franklin timezone',
'https://www.google.com/search?q=Alabama Frankville timezone',
'https://www.google.com/search?q=Alabama Frisco City timezone',
'https://www.google.com/search?q=Alabama Fruitdale timezone',
'https://www.google.com/search?q=Alabama Fruithurst timezone',
'https://www.google.com/search?q=Alabama Fulton timezone',
'https://www.google.com/search?q=Alabama Fultondale timezone',
'https://www.google.com/search?q=Alabama Furman timezone',
'https://www.google.com/search?q=Alabama Fyffe timezone',
'https://www.google.com/search?q=Alabama Gadsden timezone',
'https://www.google.com/search?q=Alabama Gainestown timezone',
'https://www.google.com/search?q=Alabama Gainesville timezone',
'https://www.google.com/search?q=Alabama Gallant timezone',
'https://www.google.com/search?q=Alabama Gallion timezone',
'https://www.google.com/search?q=Alabama Gantt timezone',
'https://www.google.com/search?q=Alabama Garden City timezone',
'https://www.google.com/search?q=Alabama Gardendale timezone',
'https://www.google.com/search?q=Alabama Gaylesville timezone',
'https://www.google.com/search?q=Alabama Geneva timezone',
'https://www.google.com/search?q=Alabama Georgiana timezone',
'https://www.google.com/search?q=Alabama Geraldine timezone',
'https://www.google.com/search?q=Alabama Gilbertown timezone',
'https://www.google.com/search?q=Alabama Glen Allen timezone',
'https://www.google.com/search?q=Alabama Glenwood timezone',
'https://www.google.com/search?q=Alabama Goodsprings timezone',
'https://www.google.com/search?q=Alabama Goodwater timezone',
'https://www.google.com/search?q=Alabama Goodway timezone',
'https://www.google.com/search?q=Alabama Gordo timezone',
'https://www.google.com/search?q=Alabama Gordon timezone',
'https://www.google.com/search?q=Alabama Goshen timezone',
'https://www.google.com/search?q=Alabama Grady timezone',
'https://www.google.com/search?q=Alabama Graham timezone',
'https://www.google.com/search?q=Alabama Grand Bay timezone',
'https://www.google.com/search?q=Alabama Grant timezone',
'https://www.google.com/search?q=Alabama Graysville timezone',
'https://www.google.com/search?q=Alabama Green Pond timezone',
'https://www.google.com/search?q=Alabama Greensboro timezone',
'https://www.google.com/search?q=Alabama Greenville timezone',
'https://www.google.com/search?q=Alabama Grove Hill timezone',
'https://www.google.com/search?q=Alabama Groveoak timezone',
'https://www.google.com/search?q=Alabama Guin timezone',
'https://www.google.com/search?q=Alabama Gulf Shores timezone',
'https://www.google.com/search?q=Alabama Guntersville timezone',
'https://www.google.com/search?q=Alabama Gurley timezone',
'https://www.google.com/search?q=Alabama Hackleburg timezone',
'https://www.google.com/search?q=Alabama Haleyville timezone',
'https://www.google.com/search?q=Alabama Hamilton timezone',
'https://www.google.com/search?q=Alabama Hanceville timezone',
'https://www.google.com/search?q=Alabama Hardaway timezone',
'https://www.google.com/search?q=Alabama Harpersville timezone',
'https://www.google.com/search?q=Alabama Hartford timezone',
'https://www.google.com/search?q=Alabama Hartselle timezone',
'https://www.google.com/search?q=Alabama Harvest timezone',
'https://www.google.com/search?q=Alabama Hatchechubbee timezone',
'https://www.google.com/search?q=Alabama Hayden timezone',
'https://www.google.com/search?q=Alabama Hayneville timezone',
'https://www.google.com/search?q=Alabama Hazel Green timezone',
'https://www.google.com/search?q=Alabama Headland timezone',
'https://www.google.com/search?q=Alabama Heflin timezone',
'https://www.google.com/search?q=Alabama Helena timezone',
'https://www.google.com/search?q=Alabama Henagar timezone',
'https://www.google.com/search?q=Alabama Higdon timezone',
'https://www.google.com/search?q=Alabama Highland Home timezone',
'https://www.google.com/search?q=Alabama Hillsboro timezone',
'https://www.google.com/search?q=Alabama Hodges timezone',
'https://www.google.com/search?q=Alabama Hollins timezone',
'https://www.google.com/search?q=Alabama Holly Pond timezone',
'https://www.google.com/search?q=Alabama Hollytree timezone',
'https://www.google.com/search?q=Alabama Hollywood timezone',
'https://www.google.com/search?q=Alabama Holy Trinity timezone',
'https://www.google.com/search?q=Alabama Honoraville timezone',
'https://www.google.com/search?q=Alabama Hope Hull timezone',
'https://www.google.com/search?q=Alabama Horton timezone',
'https://www.google.com/search?q=Alabama Houston timezone',
'https://www.google.com/search?q=Alabama Huntsville timezone',
'https://www.google.com/search?q=Alabama Hurtsboro timezone',
'https://www.google.com/search?q=Alabama Huxford timezone',
'https://www.google.com/search?q=Alabama Ider timezone',
'https://www.google.com/search?q=Alabama Irvington timezone',
'https://www.google.com/search?q=Alabama Jachin timezone',
'https://www.google.com/search?q=Alabama Jack timezone',
'https://www.google.com/search?q=Alabama Jackson timezone',
'https://www.google.com/search?q=Alabama Jacksons Gap timezone',
'https://www.google.com/search?q=Alabama Jacksonville timezone',
'https://www.google.com/search?q=Alabama Jasper timezone',
'https://www.google.com/search?q=Alabama Jefferson timezone',
'https://www.google.com/search?q=Alabama Jemison timezone',
'https://www.google.com/search?q=Alabama Jones timezone',
'https://www.google.com/search?q=Alabama Joppa timezone',
'https://www.google.com/search?q=Alabama Kansas timezone',
'https://www.google.com/search?q=Alabama Kellerman timezone',
'https://www.google.com/search?q=Alabama Kellyton timezone',
'https://www.google.com/search?q=Alabama Kennedy timezone',
'https://www.google.com/search?q=Alabama Kent timezone',
'https://www.google.com/search?q=Alabama Killen timezone',
'https://www.google.com/search?q=Alabama Kimberly timezone',
'https://www.google.com/search?q=Alabama Kinston timezone',
'https://www.google.com/search?q=Alabama Knoxville timezone',
'https://www.google.com/search?q=Alabama Laceys Spring timezone',
'https://www.google.com/search?q=Alabama Lafayette timezone',
'https://www.google.com/search?q=Alabama Lanett timezone',
'https://www.google.com/search?q=Alabama Langston timezone',
'https://www.google.com/search?q=Alabama Lapine timezone',
'https://www.google.com/search?q=Alabama Lawley timezone',
'https://www.google.com/search?q=Alabama Leeds timezone',
'https://www.google.com/search?q=Alabama Leesburg timezone',
'https://www.google.com/search?q=Alabama Leighton timezone',
'https://www.google.com/search?q=Alabama Lenox timezone',
'https://www.google.com/search?q=Alabama Leroy timezone',
'https://www.google.com/search?q=Alabama Lester timezone',
'https://www.google.com/search?q=Alabama Letohatchee timezone',
'https://www.google.com/search?q=Alabama Lexington timezone',
'https://www.google.com/search?q=Alabama Lillian timezone',
'https://www.google.com/search?q=Alabama Lincoln timezone',
'https://www.google.com/search?q=Alabama Linden timezone',
'https://www.google.com/search?q=Alabama Lineville timezone',
'https://www.google.com/search?q=Alabama Lisman timezone',
'https://www.google.com/search?q=Alabama Little River timezone',
'https://www.google.com/search?q=Alabama Livingston timezone',
'https://www.google.com/search?q=Alabama Loachapoka timezone',
'https://www.google.com/search?q=Alabama Lockhart timezone',
'https://www.google.com/search?q=Alabama Locust Fork timezone',
'https://www.google.com/search?q=Alabama Logan timezone',
'https://www.google.com/search?q=Alabama Louisville timezone',
'https://www.google.com/search?q=Alabama Lower Peach Tree timezone',
'https://www.google.com/search?q=Alabama Lowndesboro timezone',
'https://www.google.com/search?q=Alabama Loxley timezone',
'https://www.google.com/search?q=Alabama Luverne timezone',
'https://www.google.com/search?q=Alabama Lynn timezone',
'https://www.google.com/search?q=Alabama Madison timezone',
'https://www.google.com/search?q=Alabama Madison timezone',
'https://www.google.com/search?q=Alabama Magnolia timezone',
'https://www.google.com/search?q=Alabama Magnolia Springs timezone',
'https://www.google.com/search?q=Alabama Malcolm timezone',
'https://www.google.com/search?q=Alabama Malvern timezone',
'https://www.google.com/search?q=Alabama Maplesville timezone',
'https://www.google.com/search?q=Alabama Marbury timezone',
'https://www.google.com/search?q=Alabama Margaret timezone',
'https://www.google.com/search?q=Alabama Marion timezone',
'https://www.google.com/search?q=Alabama Marion Junction timezone',
'https://www.google.com/search?q=Alabama Mathews timezone',
'https://www.google.com/search?q=Alabama Maylene timezone',
'https://www.google.com/search?q=Alabama Mc Calla timezone',
'https://www.google.com/search?q=Alabama Mc Intosh timezone',
'https://www.google.com/search?q=Alabama Mc Kenzie timezone',
'https://www.google.com/search?q=Alabama Mc Shan timezone',
'https://www.google.com/search?q=Alabama Mc Williams timezone',
'https://www.google.com/search?q=Alabama Megargel timezone',
'https://www.google.com/search?q=Alabama Melvin timezone',
'https://www.google.com/search?q=Alabama Mentone timezone',
'https://www.google.com/search?q=Alabama Meridianville timezone',
'https://www.google.com/search?q=Alabama Mexia timezone',
'https://www.google.com/search?q=Alabama Midland City timezone',
'https://www.google.com/search?q=Alabama Midway timezone',
'https://www.google.com/search?q=Alabama Millbrook timezone',
'https://www.google.com/search?q=Alabama Millerville timezone',
'https://www.google.com/search?q=Alabama Millport timezone',
'https://www.google.com/search?q=Alabama Millry timezone',
'https://www.google.com/search?q=Alabama Minter timezone',
'https://www.google.com/search?q=Alabama Mobile timezone',
'https://www.google.com/search?q=Alabama Monroeville timezone',
'https://www.google.com/search?q=Alabama Montevallo timezone',
'https://www.google.com/search?q=Alabama Montgomery timezone',
'https://www.google.com/search?q=Alabama Montrose timezone',
'https://www.google.com/search?q=Alabama Moody timezone',
'https://www.google.com/search?q=Alabama Mooresville timezone',
'https://www.google.com/search?q=Alabama Morris timezone',
'https://www.google.com/search?q=Alabama Morvin timezone',
'https://www.google.com/search?q=Alabama Moulton timezone',
'https://www.google.com/search?q=Alabama Moundville timezone',
'https://www.google.com/search?q=Alabama Mount Hope timezone',
'https://www.google.com/search?q=Alabama Mount Meigs timezone',
'https://www.google.com/search?q=Alabama Mount Olive timezone',
'https://www.google.com/search?q=Alabama Mount Vernon timezone',
'https://www.google.com/search?q=Alabama Mulga timezone',
'https://www.google.com/search?q=Alabama Munford timezone',
'https://www.google.com/search?q=Alabama Muscadine timezone',
'https://www.google.com/search?q=Alabama Muscle Shoals timezone',
'https://www.google.com/search?q=Alabama Myrtlewood timezone',
'https://www.google.com/search?q=Alabama Nanafalia timezone',
'https://www.google.com/search?q=Alabama Natural Bridge timezone',
'https://www.google.com/search?q=Alabama Nauvoo timezone',
'https://www.google.com/search?q=Alabama Needham timezone',
'https://www.google.com/search?q=Alabama New Brockton timezone',
'https://www.google.com/search?q=Alabama New Castle timezone',
'https://www.google.com/search?q=Alabama New Hope timezone',
'https://www.google.com/search?q=Alabama New Market timezone',
'https://www.google.com/search?q=Alabama Newbern timezone',
'https://www.google.com/search?q=Alabama Newton timezone',
'https://www.google.com/search?q=Alabama Newville timezone',
'https://www.google.com/search?q=Alabama Normal timezone',
'https://www.google.com/search?q=Alabama Northport timezone',
'https://www.google.com/search?q=Alabama Notasulga timezone',
'https://www.google.com/search?q=Alabama Oak Hill timezone',
'https://www.google.com/search?q=Alabama Oakman timezone',
'https://www.google.com/search?q=Alabama Odenville timezone',
'https://www.google.com/search?q=Alabama Ohatchee timezone',
'https://www.google.com/search?q=Alabama Oneonta timezone',
'https://www.google.com/search?q=Alabama Opelika timezone',
'https://www.google.com/search?q=Alabama Opp timezone',
'https://www.google.com/search?q=Alabama Orange Beach timezone',
'https://www.google.com/search?q=Alabama Orrville timezone',
'https://www.google.com/search?q=Alabama Owens Cross Roads timezone',
'https://www.google.com/search?q=Alabama Oxford timezone',
'https://www.google.com/search?q=Alabama Ozark timezone',
'https://www.google.com/search?q=Alabama Paint Rock timezone',
'https://www.google.com/search?q=Alabama Palmerdale timezone',
'https://www.google.com/search?q=Alabama Panola timezone',
'https://www.google.com/search?q=Alabama Pansey timezone',
'https://www.google.com/search?q=Alabama Parrish timezone',
'https://www.google.com/search?q=Alabama Pelham timezone',
'https://www.google.com/search?q=Alabama Pell City timezone',
'https://www.google.com/search?q=Alabama Pennington timezone',
'https://www.google.com/search?q=Alabama Perdido timezone',
'https://www.google.com/search?q=Alabama Perdue Hill timezone',
'https://www.google.com/search?q=Alabama Perote timezone',
'https://www.google.com/search?q=Alabama Peterman timezone',
'https://www.google.com/search?q=Alabama Peterson timezone',
'https://www.google.com/search?q=Alabama Petrey timezone',
'https://www.google.com/search?q=Alabama Phenix City timezone',
'https://www.google.com/search?q=Alabama Phenix City timezone',
'https://www.google.com/search?q=Alabama Phil Campbell timezone',
'https://www.google.com/search?q=Alabama Piedmont timezone',
'https://www.google.com/search?q=Alabama Pike Road timezone',
'https://www.google.com/search?q=Alabama Pinckard timezone',
'https://www.google.com/search?q=Alabama Pine Apple timezone',
'https://www.google.com/search?q=Alabama Pine Hill timezone',
'https://www.google.com/search?q=Alabama Pine Level timezone',
'https://www.google.com/search?q=Alabama Pinson timezone',
'https://www.google.com/search?q=Alabama Pisgah timezone',
'https://www.google.com/search?q=Alabama Pittsview timezone',
'https://www.google.com/search?q=Alabama Plantersville timezone',
'https://www.google.com/search?q=Alabama Pleasant Grove timezone',
'https://www.google.com/search?q=Alabama Point Clear timezone',
'https://www.google.com/search?q=Alabama Prattville timezone',
'https://www.google.com/search?q=Alabama Princeton timezone',
'https://www.google.com/search?q=Alabama Quinton timezone',
'https://www.google.com/search?q=Alabama Ragland timezone',
'https://www.google.com/search?q=Alabama Rainsville timezone',
'https://www.google.com/search?q=Alabama Ralph timezone',
'https://www.google.com/search?q=Alabama Ramer timezone',
'https://www.google.com/search?q=Alabama Ranburne timezone',
'https://www.google.com/search?q=Alabama Randolph timezone',
'https://www.google.com/search?q=Alabama Range timezone',
'https://www.google.com/search?q=Alabama Red Bay timezone',
'https://www.google.com/search?q=Alabama Red Level timezone',
'https://www.google.com/search?q=Alabama Reform timezone',
'https://www.google.com/search?q=Alabama Remlap timezone',
'https://www.google.com/search?q=Alabama Repton timezone',
'https://www.google.com/search?q=Alabama River Falls timezone',
'https://www.google.com/search?q=Alabama Riverside timezone',
'https://www.google.com/search?q=Alabama Roanoke timezone',
'https://www.google.com/search?q=Alabama Robertsdale timezone',
'https://www.google.com/search?q=Alabama Rockford timezone',
'https://www.google.com/search?q=Alabama Rogersville timezone',
'https://www.google.com/search?q=Alabama Russellville timezone',
'https://www.google.com/search?q=Alabama Rutledge timezone',
'https://www.google.com/search?q=Alabama Ryland timezone',
'https://www.google.com/search?q=Alabama Safford timezone',
'https://www.google.com/search?q=Alabama Saginaw timezone',
'https://www.google.com/search?q=Alabama Saint Elmo timezone',
'https://www.google.com/search?q=Alabama Saint Stephens timezone',
'https://www.google.com/search?q=Alabama Salem timezone',
'https://www.google.com/search?q=Alabama Samantha timezone',
'https://www.google.com/search?q=Alabama Samson timezone',
'https://www.google.com/search?q=Alabama Saraland timezone',
'https://www.google.com/search?q=Alabama Sardis timezone',
'https://www.google.com/search?q=Alabama Satsuma timezone',
'https://www.google.com/search?q=Alabama Sawyerville timezone',
'https://www.google.com/search?q=Alabama Sayre timezone',
'https://www.google.com/search?q=Alabama Scottsboro timezone',
'https://www.google.com/search?q=Alabama Seale timezone',
'https://www.google.com/search?q=Alabama Section timezone',
'https://www.google.com/search?q=Alabama Selma timezone',
'https://www.google.com/search?q=Alabama Seminole timezone',
'https://www.google.com/search?q=Alabama Semmes timezone',
'https://www.google.com/search?q=Alabama Shannon timezone',
'https://www.google.com/search?q=Alabama Sheffield timezone',
'https://www.google.com/search?q=Alabama Shelby timezone',
'https://www.google.com/search?q=Alabama Shorter timezone',
'https://www.google.com/search?q=Alabama Shorterville timezone',
'https://www.google.com/search?q=Alabama Silas timezone',
'https://www.google.com/search?q=Alabama Siluria timezone',
'https://www.google.com/search?q=Alabama Silverhill timezone',
'https://www.google.com/search?q=Alabama Sipsey timezone',
'https://www.google.com/search?q=Alabama Skipperville timezone',
'https://www.google.com/search?q=Alabama Slocomb timezone',
'https://www.google.com/search?q=Alabama Smiths Station timezone',
'https://www.google.com/search?q=Alabama Somerville timezone',
'https://www.google.com/search?q=Alabama Spanish Fort timezone',
'https://www.google.com/search?q=Alabama Spring Garden timezone',
'https://www.google.com/search?q=Alabama Springville timezone',
'https://www.google.com/search?q=Alabama Spruce Pine timezone',
'https://www.google.com/search?q=Alabama Stanton timezone',
'https://www.google.com/search?q=Alabama Stapleton timezone',
'https://www.google.com/search?q=Alabama Steele timezone',
'https://www.google.com/search?q=Alabama Sterrett timezone',
'https://www.google.com/search?q=Alabama Stevenson timezone',
'https://www.google.com/search?q=Alabama Stockton timezone',
'https://www.google.com/search?q=Alabama Sulligent timezone',
'https://www.google.com/search?q=Alabama Sumiton timezone',
'https://www.google.com/search?q=Alabama Summerdale timezone',
'https://www.google.com/search?q=Alabama Sunflower timezone',
'https://www.google.com/search?q=Alabama Sweet Water timezone',
'https://www.google.com/search?q=Alabama Sycamore timezone',
'https://www.google.com/search?q=Alabama Sylacauga timezone',
'https://www.google.com/search?q=Alabama Sylvania timezone',
'https://www.google.com/search?q=Alabama Talladega timezone',
'https://www.google.com/search?q=Alabama Tallassee timezone',
'https://www.google.com/search?q=Alabama Tanner timezone',
'https://www.google.com/search?q=Alabama Theodore timezone',
'https://www.google.com/search?q=Alabama Thomaston timezone',
'https://www.google.com/search?q=Alabama Thomasville timezone',
'https://www.google.com/search?q=Alabama Thorsby timezone',
'https://www.google.com/search?q=Alabama Tibbie timezone',
'https://www.google.com/search?q=Alabama Titus timezone',
'https://www.google.com/search?q=Alabama Toney timezone',
'https://www.google.com/search?q=Alabama Town Creek timezone',
'https://www.google.com/search?q=Alabama Townley timezone',
'https://www.google.com/search?q=Alabama Toxey timezone',
'https://www.google.com/search?q=Alabama Trafford timezone',
'https://www.google.com/search?q=Alabama Trenton timezone',
'https://www.google.com/search?q=Alabama Trinity timezone',
'https://www.google.com/search?q=Alabama Troy timezone',
'https://www.google.com/search?q=Alabama Trussville timezone',
'https://www.google.com/search?q=Alabama Tuscaloosa timezone',
'https://www.google.com/search?q=Alabama Tuscumbia timezone',
'https://www.google.com/search?q=Alabama Tuskegee timezone',
'https://www.google.com/search?q=Alabama Tuskegee Institute timezone',
'https://www.google.com/search?q=Alabama Tyler timezone',
'https://www.google.com/search?q=Alabama Union Grove timezone',
'https://www.google.com/search?q=Alabama Union Springs timezone',
'https://www.google.com/search?q=Alabama Uniontown timezone',
'https://www.google.com/search?q=Alabama Uriah timezone',
'https://www.google.com/search?q=Alabama Valhermoso Springs timezone',
'https://www.google.com/search?q=Alabama Valley timezone',
'https://www.google.com/search?q=Alabama Valley timezone',
'https://www.google.com/search?q=Alabama Valley Head timezone',
'https://www.google.com/search?q=Alabama Vance timezone',
'https://www.google.com/search?q=Alabama Vandiver timezone',
'https://www.google.com/search?q=Alabama Verbena timezone',
'https://www.google.com/search?q=Alabama Vernon timezone',
'https://www.google.com/search?q=Alabama Vina timezone',
'https://www.google.com/search?q=Alabama Vincent timezone',
'https://www.google.com/search?q=Alabama Vinegar Bend timezone',
'https://www.google.com/search?q=Alabama Vinemont timezone',
'https://www.google.com/search?q=Alabama Vredenburgh timezone',
'https://www.google.com/search?q=Alabama Wadley timezone',
'https://www.google.com/search?q=Alabama Wagarville timezone',
'https://www.google.com/search?q=Alabama Walnut Grove timezone',
'https://www.google.com/search?q=Alabama Ward timezone',
'https://www.google.com/search?q=Alabama Warrior timezone',
'https://www.google.com/search?q=Alabama Waterloo timezone',
'https://www.google.com/search?q=Alabama Watson timezone',
'https://www.google.com/search?q=Alabama Wattsville timezone',
'https://www.google.com/search?q=Alabama Waverly timezone',
'https://www.google.com/search?q=Alabama Weaver timezone',
'https://www.google.com/search?q=Alabama Webb timezone',
'https://www.google.com/search?q=Alabama Wedowee timezone',
'https://www.google.com/search?q=Alabama Wellington timezone',
'https://www.google.com/search?q=Alabama Weogufka timezone',
'https://www.google.com/search?q=Alabama West Blocton timezone',
'https://www.google.com/search?q=Alabama West Greene timezone',
'https://www.google.com/search?q=Alabama Westover timezone',
'https://www.google.com/search?q=Alabama Wetumpka timezone',
'https://www.google.com/search?q=Alabama Whatley timezone',
'https://www.google.com/search?q=Alabama Wilmer timezone',
'https://www.google.com/search?q=Alabama Wilsonville timezone',
'https://www.google.com/search?q=Alabama Wilton timezone',
'https://www.google.com/search?q=Alabama Winfield timezone',
'https://www.google.com/search?q=Alabama Wing timezone',
'https://www.google.com/search?q=Alabama Woodland timezone',
'https://www.google.com/search?q=Alabama Woodstock timezone',
'https://www.google.com/search?q=Alabama Woodville timezone',
'https://www.google.com/search?q=Alabama York timezone'
]
links
for i in links:
    driver.get(i)
#driver.get('https://en.wikipedia.org/wiki/2020_in_film')
#c=driver.find_element_by_id('<h1 id="firstHeading" class="firstHeading">2020 in film</h1>')

    c=driver.find_element_by_xpath("//div[2]/div[2]/div/div/div/div/div/div/div")
    time.sleep(1)
    #d=driver.find_element_by_xpath("//div[2]/div/div/div/div/div/div/div[2]")
    #print(i[:32],c.text)
    print(i.split("?q=",1)[1],",",c.text,",")
print("completed")


# In[193]:


import re
  
# initializing string
data = "https://www.google.com/search?q=Alaska Adak timezone"
  
# printing original string  
print("The original string is : " + data) 
  
# Using re.split() 
# Splitting characters in String 
res = re.split('https://www.google.com/search?q=', data)
  
# printing result  
print("after:" + str(res)) 


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[136]:


import pandas as pd
# import csv module
import csv
  
with open("C:/Users/Sony/Downloads/US-Cities-Database-main/US-Cities-Database-main/csv/us_cities.csv") as csv_file:
    # read the csv file
    csv_reader = csv.reader(csv_file)
  
    # now we can use this csv files into the pandas
    df = pd.DataFrame([csv_reader], index = None)
  
# iterating values of first column 
for val in df[1]:
    print(val)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[70]:


# importing the module
import requests
import bs4

# URL
URL = "https://en.wikipedia.org/wiki/India"

# sending the request
response = requests.get(URL)

# parsing the response
soup = bs4.BeautifulSoup(response.text, 'html')

# Now, we have paresed HTML with us. I want to get the _motto_ from the wikipedia page.
# Elements structure
# table - class="infobox"
# 3rd tr to get motto

# getting infobox
infobox = soup.find('table', {'class': 'infobox'})

# getting 3rd row element tr
third_tr = infobox.find_all('tr')[2]

# from third_tr we have to find first 'a' element and 'div' element to get required data
first_a = third_tr.div.find('a')
div = third_tr.div.div

# motto
motto = f"{first_a.text} {div.text[:len(div.text) - 3]}"

# printing the motto
print(motto)


# In[ ]:




