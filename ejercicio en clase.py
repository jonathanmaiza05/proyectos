Python 3.5.0 (v3.5.0:374f501f4567, Sep 13 2015, 02:27:37) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> from tkinder import *
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    from tkinder import *
ImportError: No module named 'tkinder'
>>> from tkinter import *
>>> tk=Tk()
>>> btn=Button(tk, text ='Click aqui')
>>> btn.pack()
>>> 
