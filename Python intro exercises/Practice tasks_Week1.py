#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Calculate the price of bus ticket using distance
def ticket():
    c=int(input("Please enter the distance of the bus ride",))
    print("For each kilometre 10Rs. will be charged")
    t=c*10
    print("Your ticket is Rs.",t)
    


# In[2]:


ticket()


# In[8]:


#Code for calculating speed, distance,time
print("Please enter ? for what you wish to caluclate")
s=str(input("Please enter speed",))
d=str(input("Please enter distance",))
t=str(input("Please enter time",))
if s=="?":
    speed= int(d)/int(t)
    print("Speed is ",speed)
elif d=="?":
    distance= int(t)*int(s)
    print("Distance is ",distance)
elif t=="?":
    time= int(d)/int(s)
else: print("Enter a valid number")


# In[13]:


#Suggesting AC temperature
i=int(input("Please enter the outside temperature ",))
d= i-22
if d>0:
    print("Please reduce the temperature by ",d, "degrees Celcius")
else: print("Please increase the temperature by ",-d, "degrees Celcius")


# In[ ]:




