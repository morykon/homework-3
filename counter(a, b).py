
# coding: utf-8

# In[111]:


# 1)
def counter(a, b):
   
    c = list(map(int, str(a)))
    v = list(map(int, str(b)))
        
    res=list(set(c) & set(v))
    ln = len(res)
    
    if res:
        print(ln)       
    else:
        print('0')
        
# 2)



# In[112]:


counter(12345, 567)


# In[113]:


counter(123, 45)


# In[114]:


counter(1233211, 12128)

