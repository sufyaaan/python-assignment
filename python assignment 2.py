#!/usr/bin/env python
# coding: utf-8

# In[1]:


physics = int ( input ("Enter physics marks"))
chemistry = int ( input("Enter chemistry marks"))
maths = int ( input ("Enter maths marks"))
urdu = int ( input ("Enter urdu marks"))
english = int ( input ("Enter english marks"))
percentage = ((physics + chemistry + maths + urdu + english)/500) * 100
if percentage<100 and percentage>=80:
    print ("A-one garde")
elif percentage<80 and percentage>=70:
    print ("A grade")
elif percentage<70 and percentage>=60:
    print ("B grade")
elif percentage<60 and percentage>=50:
    print ("C grade")
elif percentage<50 and percentage>=40:
    print ("D grade")
elif percentage<40 and percentage>=0:
    print ("F grade")
else:
    print("Wrong marks added")


# In[10]:


number = int(input("Enter the number : "))
check = number%2
if check==0 :
    print("Number is even")
else:
    print("Number is odd") 


# In[12]:


cities = ["KHI" , "LHR" , "ISB" , "FSB" , "HYD" , "BHP" , "ABT" , "SKR" , "MUR"]
len(cities)


# In[17]:


list = [1 , 2 ,5 , 6 , 4 , 5 , 9 ]
sum(list)


# In[18]:


list = [1 , 2 ,5 , 6 , 4 , 5 , 9 ]
print (max(list))


# In[20]:


a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for b in a:
    if b < 5:
        print (b)


# In[ ]:




