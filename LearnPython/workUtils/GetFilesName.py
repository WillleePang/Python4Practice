# coding=utf-8
# Filename:

__author__ = 'pangwilllee'

import os,sys


def get_files_by_url(file_dir):
    f = file('name.txt', 'wb+')
    file_num = 0
    file_list = os.listdir(file_dir)
    for single_file in file_list:
        file_num+1
        f.write(single_file.decode('gbk').encode('utf-8') + '\n')
        print unicode(single_file, "gbk")
    f.close()


if __name__ == '__main__':
    get_files_by_url('C:'+os.sep+'Users'+os.sep+'pangwilllee'+os.sep+'Desktop')