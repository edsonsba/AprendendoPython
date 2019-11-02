#!/usr/bin/env python
# coding: utf-8

# In[2]:


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

facebook = webdriver.Chrome(r"C:/Program Files (x86)/Google/Chrome/Application/chromedriver.exe")
facebook.get('https://www.facebook.com')


# In[3]:


facebook.find_element_by_id("email").send_keys("edysonsba@hotmail.com")


# In[4]:


facebook.find_element_by_id("pass").send_keys("FoxEdson2018")


# In[35]:


facebook.find_element_by_id("u_0_b").click()


# In[36]:


menu = facebook.find_element_by_id("u_0_a")


# In[37]:


facebook.find_element_by_xpath('//*[@id="u_0_a"]/div[1]/div[1]/div/a').click()


# In[38]:


facebook.find_element_by_name("q").send_keys("Caronas Mococa  ↔ São Paulo")
facebook.find_element_by_name("q").send_keys(Keys.ENTER)


# In[41]:


facebook.find_element_by_xpath('//*[@id="xt_uniq_2"]/div/a"]').click()


# In[28]:


facebook.find_element_by_id('rc.u_fetchstream_39_u').click()
facebook.find_element_by_name('_1mf _1mj').send_keys("[Ofereço Carona]")


# In[ ]:




