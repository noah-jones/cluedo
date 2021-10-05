#!/usr/bin/env python3

import sys
import random
import string

from optparse import OptionParser

import svgwrite

def get_encrypyted_secret(secret,
                          noise_color='rgb(255, 0, 0)',
                          secret_color='rgb(0, 255, 255)',
                          draw_circle=False,
                          filename=None,
                          ):
    """
    Get an :class:`svgwrite.Drawing` object of the visually encrypted secret.

    Parameters
    ==========
    secret : str
        The secret to encrypt
    noise_color : str, default = 'rgb(255, 0, 0)'
        The color of the foreground noise (an svg-compatible string)
    secret_color : str, default = 'rgb(0, 255, 255)'
        The color of the foreground noise (an svg-compatible string)
    draw_circle : bool, default = False
        Whether to place the secret in a white circle
    filename : str, default = None
        Filename the :class:`svgwrite.Drawing` object should be associated with

    Returns
    =======
    dwg : :class:`svgwrite.Drawing`
        The visually encrypted message
    """
    if filename is None:
        filename = "__dummy__"


    document_height = 800  # px
    dwg = svgwrite.Drawing(filename=filename, size=(f'{document_height}px', f'{document_height}px'))


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
    color = secret_color
    for offset in [0, 20]:
        random_text(offset, color)

    # secret background
    if draw_circle:
        dwg.add(dwg.circle(center=('50%', '50%'),
                           r='40%',
                           fill='rgb(255, 255, 255)'))
    else:
        dwg.add(dwg.rect(insert=(line_height, document_height/2-line_height),
                         size=(document_height-2*line_height, 1.5*line_height),
                         fill='rgb(255, 255, 255)'))


    # add noise
    rmax = 4
    rmin = 2
    N = 4000

    for i in range(N):
        dwg.add(dwg.circle(center=(random.random()*document_height, random.random()*document_height),
                           r=random.random()*(rmax-rmin)+rmin,
                           fill=noise_color,
                           ))

    # secret
    dwg.add(dwg.text(secret,
                     insert=('50%', '50%'),
                     fill=secret_color,
                     style='font-size:32pt; text-anchor:middle;'))



    # foreground text
    color = noise_color
    for offset in [10, 30]:
        random_text(offset, color)

    return dwg

def main():
    """CLI."""
    parser = OptionParser()
    parser.add_option("-o", "--outputfile", dest="filename",
                      help="write SVG to FILE", metavar="FILE")
    parser.add_option("-c", "--circle", action="store_true", dest="put_in_circle",
                      help="let the secret live in a white circle",default=False)


    options, args = parser.parse_args()

    if len(args) != 1:
        raise ValueError('No code provided to encrypt')

    YOUR_SECRET_CODE = args[0]

    if options.filename is not None:
        write_to_stdout = False
        filename = options.filename
    else:
        write_to_stdout = True
        filename = '__dummy__'

    dwg = get_encrypyted_secret(YOUR_SECRET_CODE,draw_circle=options.put_in_circle,filename=filename)
    if write_to_stdout:
        dwg.write(sys.stdout)
    else:
        dwg.save()


if __name__=="__main__":
    main()
