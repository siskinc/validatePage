#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by susecjh on 2017/10/28 0028

import random
from PIL import Image, ImageFont, ImageDraw

__validateLen = 10

# 大写字母，小写字母，数字
txt_list = [48, 49, 50, 51, 52, 53, 54, 55, 56, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81,
            82, 83, 84, 85, 86, 87, 88, 89, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111,
            112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122]


def rndtxt():
    return chr(txt_list[random.randint(0,len(txt_list)-1)])

def rnd_font_color():
    return (random.randint(32,127),random.randint(32,127),random.randint(32,127));

def code():
    weight = 240
    hight = 60
    image = Image.new('RGB',(weight,hight),(255,255,255))
    font = ImageFont.truetype('msyh.ttc',36)
    draw = ImageDraw.Draw(image)
    
    #填充背景
    for x in range(weight):
        for y in range(hight):
            draw.point((x,y),fill=(255,255,255))
    
    #生成随机验证码
    for t in range(__validateLen):
        draw.text(((weight//__validateLen)*t+10,10), rndtxt(),font=font,fill = rnd_font_color())
    
    
    

