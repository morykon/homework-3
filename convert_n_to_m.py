
# coding: utf-8

# In[22]:


def convert_n_to_m(x, n, m):
    if not(type(x)==int or type(x)==str):
        return False
    if x<0:
        return False
    if m == 1:
        to_ten = to_tens_sm(x, n)
        result = to_ten * '0'
        return result
    
    x = str(x)
    x = x.upper()
    alhabet_of_num = {"A" : 10, "B" : 11, "C" : 12, "D" : 13, "E" : 14, "F" : 15, "G" : 16,
    "H" : 17, "I" : 18, "J" : 19,"K" : 20, "L" : 21, "M" : 22, "N" : 23, "O" : 24,"P" : 25, "Q" : 26,
    "R" : 27, "S" : 28, "T" : 29,"U" : 30,"V" : 31, "W" : 32, "X" : 33, "Y" : 34, "Z" : 35}
    max_in_1 = max(x)
    default = '-1'
    max_in_2 = alhabet_of_num.get(max_in_1, default)
    if max_in_2 == '-1':
        max_in_2 = max_in_1 
    if max(x) == '0' and n ==10 :
        return 0
    elif n == 10 :
        result = to_any_sm_from_10(x, m)
        return result
    
    
    elif int(max_in_2) >= n:
        return False
    
    
    elif n<10 and n>10:
        to_ten = to_tens_sm(x, n)
        if to_ten == 0 :
            return 0
        else:
            result = to_any_sm_from_10(to_ten, m)
            return result

# функція  to_any_sm_from_10 переводить з десяткової в систему m
def to_tens_sm(in_any_sm, sm):
    in_any_sm = str(in_any_sm)
    in_any_sm = in_any_sm.upper()
    default = '-1'
    tens_sm = 0
    counter_of_power = 0
    in_any_sm = in_any_sm[::-1]
    
    alhabet_of_num = {"A" : 10, "B" : 11, "C" : 12, "D" : 13, "E" : 14, "F" : 15, "G" : 16,
    "H" : 17, "I" : 18, "J" : 19,"K" : 20, "L" : 21, "M" : 22, "N" : 23, "O" : 24,"P" : 25, "Q" : 26,
    "R" : 27, "S" : 28, "T" : 29,"U" : 30,"V" : 31, "W" : 32, "X" : 33, "Y" : 34, "Z" : 35}
    
    for char in in_any_sm :
        char_in_numb = alhabet_of_num.get(char, default)
        if char_in_numb == '-1':
            char_in_numb = int(char)
        tens_sm = tens_sm + char_in_numb*(sm**counter_of_power)
        counter_of_power = counter_of_power  + 1
        
    return tens_sm


#Функція  to_any_sm_from_10 переводить х в десяткову с-му.
def to_any_sm_from_10(tens_system, any_sm):
    num_of_alhabet = {}
    alhabet_of_num = {"A" : 10, "B" : 11, "C" : 12, "D" : 13, "E" : 14, "F" : 15, "G" : 16,
    "H" : 17, "I" : 18, "J" : 19,"K" : 20, "L" : 21, "M" : 22, "N" : 23, "O" : 24,"P" : 25, "Q" : 26,
    "R" : 27, "S" : 28, "T" : 29,"U" : 30,"V" : 31, "W" : 32, "X" : 33, "Y" : 34, "Z" : 35}
    for key, value in alhabet_of_num.items():
        num_of_alhabet[value] = key
    
    tens_system = int(tens_system)
    m_system = ''
    default = '-1'
    while tens_system != 0:
        ost = tens_system  % any_sm
        ost_for_str = num_of_alhabet.get(ost, default)
        if ost_for_str == '-1' :
            ost_for_str = str(ost)    
        m_system = ost_for_str + m_system
        tens_system = tens_system /any_sm
    return m_system


# In[24]:


convert_n_to_m(123, 4, 1)


# In[25]:


convert_n_to_m("A1Z", 36, 16)


# In[26]:


convert_n_to_m(-123.0, 11, 16)


# In[27]:


convert_n_to_m([123], 4, 3)


# In[28]:


convert_n_to_m("0123", 5, 6)

