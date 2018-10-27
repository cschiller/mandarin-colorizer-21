#
# Anki add-on for adding tone colors to Chinese characters
#
# Copyright (c) 2015 Christian Schiller
#

# import the main window object (mw) from ankiqt
from aqt import mw
from aqt.utils import showInfo
from aqt.qt import *

import string

from .mandarin import pinyin
from .mandarin import color

# First some helper functions.

def isHanzi(h):
    if ord(h) < 128:
        return False
    elif u'\uff00' < h and h < u'\uffef':
        return False
    elif u'\u3000' <= h and h < u'\u303f':
        return False
    elif u'\u2026' == h:
        # horizontal ellipsis
        return False
    else:
        return True


def flatten(aList):
    result = []
    for subList in aList:
        for s in subList:
            result.append(s)
    return result


# We're going to add a menu item below. First we want to create a function to
# be called when the menu item is activated.

def colorize():

    nids = mw.col.findNotes('deck:current')
    for nid in nids:
        note = mw.col.getNote(nid)

        if len(note['OrigPinyin'].strip()) == 0:
            note['OrigPinyin'] = note['Pinyin']
            note.flush()

        p = map(str.strip, note['Pinyin'].split(','))
        h = note['Hanzi'].strip()

        i = 0
        j = 0

        allHanzi = ''

        for k in range(len(h)):
            if isHanzi(h[k]):
                allHanzi += h[k]

        newPinyin = ''
        newColor = ''

        firstVariant = True

        for variant in p:

            if not firstVariant:
                newPinyin += ', '

            try:
                np = pinyin.normalize(variant)
            except Exception:
                showInfo('Invalid Pinyin: ' + variant)
                continue

            sandhi = pinyin.sandhify(flatten(np), allHanzi)

            firstWord = True
            for w in np:

                if not firstWord:
                    newPinyin += ' '
                firstWord = False

                syllables = ''
                for syllable in w:
                    syllables += syllable

                    if firstVariant:
                        hc = h[j]
                        while not isHanzi(hc):
                            newColor += hc
                            j += 1
                            hc = h[j]
                        newColor += color.colorize(hc, syllable[-1], sandhi[i])
                        i += 1
                        j += 1

                newPinyin += pinyin.useToneMarkers(syllables)

            if firstVariant:
                # add trailing non-Hanzi characters
                while j < len(h):
                    newColor += h[j]
                    j += 1

            firstVariant = False

        note['Color'] = newColor
        if len(newPinyin.strip()) > 0:
            note['Pinyin'] = newPinyin
        note.flush()

    showInfo("Done coloring Chinese characters.")


def resetPinyin():
    nids = mw.col.findNotes('deck:current')
    for nid in nids:
        note = mw.col.getNote(nid)
        if len(note['OrigPinyin'].strip()) > 0:
            note['Pinyin'] = note['OrigPinyin']
            note.flush()

    showInfo("Done resetting Pinyin.")


# Now add the actions to the tools menu.

colorAction = QAction("Color Chinese", mw)
colorAction.triggered.connect(colorize)
mw.form.menuTools.addAction(colorAction)

resetAction = QAction("Reset Pinyin", mw)
resetAction.triggered.connect(resetPinyin)
mw.form.menuTools.addAction(resetAction)
