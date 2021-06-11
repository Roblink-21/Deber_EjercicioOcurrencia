#!/usr/bin/env python
# coding: utf-8

# In[127]:


#leer archivos
def leertxt():
    list = []
    archi=open('texto.txt','r')
    linea=archi.read()
    while linea!="":
        list = linea.split()
        linea=archi.readline()
    archi.close()
    agregar_list(list)
    


# In[128]:


#Inicializar
frecuencia = {}
leertxt()
#======================================


# In[129]:


#Obtener datos
def agregar_list(list):
    for n in list:
        if n in frecuencia:
            frecuencia[n] += 1
        else:
            frecuencia[n] = 1


# In[141]:


print('----------------------------Contenido actual del diccionario--------------------------------')
print('--------------------------------------------------------------------------------------------')
for p in frecuencia:
    print("(", p, ",", frecuencia[p], ")")
print('--------------------------------------------------------------------------------------------')
print('--------------------------------------------------------------------------------------------')


# In[ ]:




