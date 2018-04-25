
# coding: utf-8

# In[64]:



def my_sort(func, array, reverse):
        
    array.sort() 

    if func: 
        array.sort(key = func)
        
    if reverse:
        array.reverse()
        
    print(array)
    
    


# In[65]:


my_sort(None,['Aa', 'cCc', 'bbbbb', 'a'], None)


# In[66]:


my_sort(lambda x: len(x), ['Aa', 'cCc', 'bbbbb', 'a'], None)

