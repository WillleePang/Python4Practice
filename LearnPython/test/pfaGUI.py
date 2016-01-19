# -*- encoding: utf-8 -*-
# Filename:

__author__ = 'pangwilllee'


from functools import partial
import Tkinter


root = Tkinter.Tk()
MyButton = partial(Tkinter.Button, root, fg='white', bg='blue')
b1 = MyButton(text='button 1')
b2 = MyButton(text='button 2')
b3 = MyButton(text='button 3')
qb = MyButton(text='quit', bg='red', command=root.quit)
b1.pack()
b2.pack()
b3.pack()
qb.pack(fill=Tkinter.X, expand=True)
root.title('PFAs')
root.mainloop()


