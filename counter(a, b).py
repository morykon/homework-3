
# coding: utf-8

# In[111]:



def counter(a, b):
    
    na = []
    nb = []
    c = list(map(int, str(a)))
    v = list(map(int, str(b)))
   
    from itertools import groupby
    
    na = [s for s, _ in groupby(c)]
    #print(na)
    nb = [s for s, _ in groupby(v)]
    #print(nb)
        
    result=list(set(na) & set(nb))
    ln = len(result)
    
    if result:
        print(ln)       
    else:
        print('0')


# In[112]:


counter(12345, 567)


# In[113]:


counter(123, 45)


# In[114]:


counter(1233211, 12128)

