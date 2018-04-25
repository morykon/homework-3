
# coding: utf-8

# In[82]:



def my_sort(func, array, reverse):
    
    if type(array) != list:
        print('TypeError')    
    else:
        array.sort() 
        if func: 
            array.sort(key = func)
        if reverse:
            array.reverse()    
        
        print(array)
    
    


# In[83]:


my_sort(None,['Aa', 'cCc', 'bbbbb', 'a'], None)


# In[84]:


my_sort(lambda x: len(x), ['Aa', 'cCc', 'bbbbb', 'a'], None)


# In[87]:


my_sort(lambda x: len(x), 23, None)

