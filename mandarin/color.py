#
# Colorize Chinese characters according to their tone.
#
# First tone : red
# Second tone: orange
# Third tone : green
# Fourth tone: blue
#
# Tone sandhi are shown using a lighter color.
#
# Copyright (c) 2015 Christian Schiller
#

def getColor(tone, sandhify=False):

    colors = [
        '#ff0000',
        '#ff7f7f',
        '#ffaa00',
        '#ffd47f',
        '#00aa00',
        '#66cc66',
        '#0000ff',
        '#7f7fff',
        '#545454',
        '#656565',
    ]

    if not sandhify:
        return colors[2 * (int(tone) - 1)]
    else:
        return colors[2 * (int(tone) - 1) + 1]

def _spanStart(color):
    return '<span style="color:' + color +'">'

def _spanEnd():
    return '</span>'

def colorize(hanzi, tone, sandhify=True):
    color = getColor(tone, sandhify=sandhify)
    return _spanStart(color) + hanzi + _spanEnd()
