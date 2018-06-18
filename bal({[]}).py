
# coding: utf-8

# In[40]:


def bal(e):
    opening = tuple('({[')
    closing = tuple(')}]')
    mapping = dict(zip(opening, closing))
    queue = []

    for l in e:
        if l in opening:
            queue.append(mapping[l])
        elif l in closing:
            if not queue or l != queue.pop():
                return False
    return not queue

if __name__ == '__main__':
    import doctest
    doctest.testmod()


# In[41]:


is_matched('(a-2)*(sqrt(4x)-6)**2')


# In[42]:


is_matched(')(())(')

