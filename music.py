#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install music


# In[2]:


from music import music_rec


# In[ ]:


def lazy_import(module_name):
    import sys
    module = sys.modules.get(module_name)
    if module is None:
        module = _import_(module_name)
        sys.modules[module_name] = module
    return module


# In[ ]:


from mymodule import MyClass


# In[ ]:


MyClass = lazy_import('mymodule').MyClass

