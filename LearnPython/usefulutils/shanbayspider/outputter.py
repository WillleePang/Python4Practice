#! /usr/bin/env python
# encoding: utf-8


class Outputter(object):
    def __init__(self):
        self.datas = []

    # shanbay收集数据
    def shanbay_collect_data(self, cont_arr):
        self.datas.extend(cont_arr)

    # shanbay内容输出函数
    def shanbay_output_html(self, file_name):
        fout = open('./shanbay/'+file_name, 'w')
        fout.write("<html>")
        fout.write("<body>")
        fout.write("<table>")
        for data in self.datas:
            fout.write("<tr>")
            fout.write("<td>%s</td>" % data['title'])
            fout.write("<td><a target='_Blank' href='http://www.shanbay.com%s'>%s</a></td>" % (data['url'], data['url']))
            fout.write("</tr>")
        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")
        fout.close()
