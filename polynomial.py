
# coding: utf-8

# In[24]:


def polin(n):
    b = ' '
    for i in b:
        n = n.replace(i, '')
    
    n = n.upper()
    
    m = ''
    for a in n:
        m = a+m
    
    if m == n:
        print('YES')
    else:
        print('NO')


# In[25]:


polin('puppy')


# In[26]:


polin('0')


# In[27]:


polin('mystring1Gni rts ym')

