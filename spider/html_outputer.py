#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class HtmlOutputer(object):
    def __init__(self):
        self.datas = []

    def collect_data(self,data):
        if data is None:
            return
        else:
            self.datas.append(data)
    def output_html(self):
        fout = open('./output.html','w')
        fout.write('<html>')
        fout.write('<head><meta charset="utf-8"><link rel="stylesheet" type="text/css" href="./style.css"></head>')
        fout.write('<body>')
        fout.write('<table id ="table-1">')
        fout.write('<thead><tr><th>序号</th><th>标题</th><th>简介</th></tr></thead>')
        for index,data in enumerate(self.datas):
            num = index+1
            fout.write('<tr>')
            fout.write('<td>%s</td>' % num)
            fout.write('<td>')
            fout.write('<a href="%s">%s</a>' % (data['url'], data['title']))
            fout.write('</td>')
            fout.write('<td>%s</td>' % data['description'])
            fout.write('</tr>')
        fout.write('</table>')

        fout.write('</body>')

        fout.write('</html>')

        fout.close()