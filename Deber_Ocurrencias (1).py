#!/usr/bin/env python
# coding: utf-8

# In[123]:


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
    


# In[124]:


#Inicializar
frecuencia = {}
leertxt()
#======================================


# In[125]:


#Obtener datos
def agregar_list(list):
    for n in list:
        if n in frecuencia:
            frecuencia[n] += 1
        else:
            frecuencia[n] = 1


# In[126]:


print('Contenido actual del diccionario: ', frecuencia)


# In[ ]:




