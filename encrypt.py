#!/usr/bin/env python3

import random
import string

import svgwrite


YOUR_SECRET_CODE = 'your secret code here'

document_height = 800  # px
dwg = svgwrite.Drawing(filename='result.svg', size=(f'{document_height}px', f'{document_height}px'))


# background
dwg.add(dwg.rect(insert=(0, 0), size=('100%', '100%'), rx=None, ry=None, fill='rgb(255,255,255)'))


line_height = 40

def random_text(offset, color):

    for i in range(document_height // line_height + 1):

        text = ''.join([random.choice(string.ascii_letters) for _ in range(100)])

        dwg.add(dwg.text(text,
                         insert=(0-offset, i*line_height+20-offset),
                         fill=color,
                         style='font-size:32pt'
                         ))
# background text
color = 'rgb(64, 156, 245)'
for offset in [0, 20]:
    random_text(offset, color)

# secret background
dwg.add(dwg.circle(center=('50%', '50%'),
                   r='40%',
                   fill='rgb(255, 255, 255)'))


# foreground text
color = 'rgb(217, 28, 136)'
for offset in [10, 30]:
    random_text(offset, color)

# secret
color = 'rgb(64, 156, 245)'
dwg.add(dwg.text(YOUR_SECRET_CODE,
                 insert=('50%', '50%'),
                 fill=color,
                 style='font-size:32pt; text-anchor:middle'))


dwg.save()
