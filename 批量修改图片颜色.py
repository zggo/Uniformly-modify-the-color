# -*- coding: utf-8 -*-
"""
Created on Thu May 19 18:47:54 2022
批量修改图片颜色

"""

import PIL.Image as Image
import os

all = os.walk(r'C:\code\image processing\changecolor') 

#============1.打开图片============
for path, dir, filelist in all:
    for i in filelist:
        img = Image.open('changecolor/'+i)
        img_array = img.load()
        #遍历每一个像素块，并处理颜色
        width, height = img.size#获取宽度和高度
        for x in range(0,width):
            for y in range(0,height):
                rgb = img_array[x,y]#获取一个像素块的rgb
                r = rgb[0]
                g = rgb[1]
                b = rgb[2]
                if r>0 and g>0 and b>0 :#背景颜色
                    img_array[x, y] = (0, 0, 0)
                elif r>0 and g<255 and b<255 :
                    img_array[x, y] = (4, 4, 4)#建筑颜色
                else :
                    img_array[x, y] = (2, 2, 2)#道路颜色
        img.save('changecolor/'+i)
        print('任务完成') 