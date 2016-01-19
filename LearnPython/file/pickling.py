# -*- encoding: utf-8 -*-
# Filename: pickling.py

__author__ = 'pangwilllee'

import cPickle as p
# import pickle as p

shop_list_file = r'D:\files\shoplist.data'
# the name of the file where we store the object

shop_list = ['apple', 'mango', 'corret']

# Write to the file
f = file(shop_list_file, 'w')
p.dump(shop_list, f)
f.close()

del shop_list  # remove the shop_list

# Read back from the storage
f = file(shop_list_file)
stored_list = p.load(f)
print stored_list




