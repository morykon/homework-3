
# coding: utf-8

# In[2]:


#1_______________________
from pprint import pprint 
matrix = [[ 1, 4, 5, 6, 7], 
           [ 8, 9, 0, 1, 1], 
           [ 1, 4, 5, 6, 7], 
           [ 8, 9, 1, 0, 4], 
           [ 8, 6, 5, 4, 0.5]] 

matrix_t = list(zip(*matrix)) 
pprint(matrix) 
pprint(matrix_t) 

#2_____________________________
import numpy as np
mat = np.transpose(matrix)
print(mat)

