#
# Module for handling Hanyu Pinyin
#
# Copyright (c) 2015 Christian Schiller
#

# Note that 'v' is not included in this set.
CONSONANTS = set(['b', 'B',
                  'c', 'C',
                  'd', 'D',
                  'f', 'F',
                  'g', 'G',
                  'h', 'H',
                  'j', 'J',
                  'k', 'K',
                  'l', 'L',
                  'm', 'M',
                  'n', 'N',
                  'p', 'P',
                  'q', 'Q',
                  'r', 'R',
                  's', 'S',
                  't', 'T',
                  'w', 'W',
                  'x', 'X',
                  'y', 'Y',
                  'z', 'Z'])

VOWELS = set(['a', 'A',
              'e', 'E',
              'i', 'I',
              'o', 'O',
              'u', 'U',
              '\u00fc', '\u00dc',
              'v', 'V'])

ZERO_WIDTH_SPACE = '\u200b'

MACRON = '\u0304'
ACUTE = '\u0301'
CARON = '\u030c'
GRAVE = '\u0300'

COMBINING_CHARACTERS = set([MACRON, ACUTE, CARON, GRAVE])


PINYIN_SYLLABLES = set([
    'a',
    'ai',
    'an',
    'ang',
    'ao',
    'ba',
    'bai',
    'ban',
    'bang',
    'bao',
    'bei',
    'ben',
    'beng',
    'bi',
    'bian',
    'biao',
    'bie',
    'bin',
    'bing',
    'bo',
    'bu',
    'ca',
    'cai',
    'can',
    'cang',
    'cao',
    'ce',
    'cen',
    'ceng',
    'cha',
    'chai',
    'chan',
    'chang',
    'chao',
    'che',
    'chen',
    'cheng',
    'chi',
    'chong',
    'chou',
    'chu',
    'chua',
    'chuai',
    'chuan',
    'chuang',
    'chui',
    'chun',
    'chuo',
    'ci',
    'cong',
    'cou',
    'cu',
    'cuan',
    'cui',
    'cun',
    'cuo',
    'da',
    'dai',
    'dan',
    'dang',
    'dao',
    'de',
    'dei',
    'deng',
    'di',
    'dia',
    'dian',
    'diao',
    'die',
    'ding',
    'diu',
    'dong',
    'dou',
    'du',
    'duan',
    'dui',
    'dun',
    'duo',
    'e',
    'ei',
    'en',
    'er',
    'fa',
    'fan',
    'fang',
    'fei',
    'fen',
    'feng',
    'fo',
    'fou',
    'fu',
    'ga',
    'gai',
    'gan',
    'gang',
    'gao',
    'ge',
    'gei',
    'gen',
    'geng',
    'gong',
    'gou',
    'gu',
    'gua',
    'guai',
    'guan',
    'guang',
    'gui',
    'gun',
    'guo',
    'ha',
    'hai',
    'han',
    'hang',
    'hao',
    'he',
    'hei',
    'hen',
    'heng',
    'hong',
    'hou',
    'hu',
    'hua',
    'huai',
    'huan',
    'huang',
    'hui',
    'hun',
    'huo',
    'ji',
    'jia',
    'jian',
    'jiang',
    'jiao',
    'jie',
    'jin',
    'jing',
    'jiong',
    'jiu',
    'ju',
    'juan',
    'jue',
    'jun',
    'ka',
    'kai',
    'kan',
    'kang',
    'kao',
    'ke',
    'kei',
    'ken',
    'keng',
    'kong',
    'kou',
    'ku',
    'kua',
    'kuai',
    'kuan',
    'kuang',
    'kui',
    'kun',
    'kuo',
    'la',
    'lai',
    'lan',
    'lang',
    'lao',
    'le',
    'lei',
    'leng',
    'li',
    'lia',
    'lian',
    'liang',
    'liao',
    'lie',
    'lin',
    'ling',
    'liu',
    'lo',
    'long',
    'lou',
    'lu',
    'luan',
    'lun',
    'luo',
    'lv',
    'lve',
    'ma',
    'mai',
    'man',
    'mang',
    'mao',
    'me',
    'mei',
    'men',
    'meng',
    'mi',
    'mian',
    'miao',
    'mie',
    'min',
    'ming',
    'miu',
    'mo',
    'mou',
    'mu',
    'na',
    'nai',
    'nan',
    'nang',
    'nao',
    'ne',
    'nei',
    'nen',
    'neng',
    'ni',
    'nian',
    'niang',
    'niao',
    'nie',
    'nin',
    'ning',
    'niu',
    'nong',
    'nou',
    'nu',
    'nuan',
    'nun',
    'nuo',
    'nv',
    'nve',
    'o',
    'ou',
    'pa',
    'pai',
    'pan',
    'pang',
    'pao',
    'pei',
    'pen',
    'peng',
    'pi',
    'pian',
    'piao',
    'pie',
    'pin',
    'ping',
    'po',
    'pou',
    'pu',
    'qi',
    'qia',
    'qian',
    'qiang',
    'qiao',
    'qie',
    'qin',
    'qing',
    'qiong',
    'qiu',
    'qu',
    'quan',
    'que',
    'qun',
    'r',
    'ran',
    'rang',
    'rao',
    're',
    'ren',
    'reng',
    'ri',
    'rong',
    'rou',
    'ru',
    'rua',
    'ruan',
    'rui',
    'run',
    'ruo',
    'sa',
    'sai',
    'san',
    'sang',
    'sao',
    'se',
    'sen',
    'seng',
    'sha',
    'shai',
    'shan',
    'shang',
    'shao',
    'she',
    'shei',
    'shen',
    'sheng',
    'shi',
    'shou',
    'shu',
    'shua',
    'shuai',
    'shuan',
    'shuang',
    'shui',
    'shun',
    'shuo',
    'si',
    'song',
    'sou',
    'su',
    'suan',
    'sui',
    'sun',
    'suo',
    'ta',
    'tai',
    'tan',
    'tang',
    'tao',
    'te',
    'teng',
    'ti',
    'tian',
    'tiao',
    'tie',
    'ting',
    'tong',
    'tou',
    'tu',
    'tuan',
    'tui',
    'tun',
    'tuo',
    'wa',
    'wai',
    'wan',
    'wang',
    'wei',
    'wen',
    'weng',
    'wo',
    'wu',
    'xi',
    'xia',
    'xian',
    'xiang',
    'xiao',
    'xie',
    'xin',
    'xing',
    'xiong',
    'xiu',
    'xu',
    'xuan',
    'xue',
    'xun',
    'ya',
    'yan',
    'yang',
    'yao',
    'ye',
    'yi',
    'yin',
    'ying',
    'yo',
    'yong',
    'you',
    'yu',
    'yuan',
    'yue',
    'yun',
    'za',
    'zai',
    'zan',
    'zang',
    'zao',
    'ze',
    'zei',
    'zen',
    'zeng',
    'zha',
    'zhai',
    'zhan',
    'zhang',
    'zhao',
    'zhe',
    'zhen',
    'zhei',
    'zhen',
    'zheng',
    'zhi',
    'zhong',
    'zhou',
    'zhu',
    'zhua',
    'zhuai',
    'zhuan',
    'zhuang',
    'zhui',
    'zhun',
    'zhuo',
    'zi',
    'zong',
    'zou',
    'zu',
    'zuan',
    'zui',
    'zun',
    'zuo'
])

DIACRITICS = {

              # First tone

              '\u0100' : ('A', 1),
              '\u0101' : ('a', 1),
              '\u0112' : ('E', 1),
              '\u0113' : ('e', 1),
              '\u012a' : ('I', 1),
              '\u012b' : ('i', 1),
              '\u014c' : ('O', 1),
              '\u014d' : ('o', 1),
              '\u016a' : ('U', 1),
              '\u016b' : ('u', 1),
              '\u01d5' : ('V', 1),
              '\u01d6' : ('v', 1),

              # Second tone

              '\u00c1' : ('A', 2),
              '\u00e1' : ('a', 2),
              '\u00c9' : ('E', 2),
              '\u00e9' : ('e', 2),
              '\u00cd' : ('I', 2),
              '\u00ed' : ('i', 2),
              '\u00d3' : ('O', 2),
              '\u00f3' : ('o', 2),
              '\u00da' : ('U', 2),
              '\u00fa' : ('u', 2),
              '\u01d7' : ('V', 2),
              '\u01d8' : ('v', 2),

              # Third tone

              '\u01cd' : ('A', 3),
              '\u01ce' : ('a', 3),
              '\u011a' : ('E', 3),
              '\u011b' : ('e', 3),
              '\u01cf' : ('I', 3),
              '\u01d0' : ('i', 3),
              '\u01d1' : ('O', 3),
              '\u01d2' : ('o', 3),
              '\u01d3' : ('U', 3),
              '\u01d4' : ('u', 3),
              '\u01d9' : ('V', 3),
              '\u01da' : ('v', 3),

              # Fourth tone

              '\u00c0' : ('A', 4),
              '\u00e0' : ('a', 4),
              '\u00c8' : ('E', 4),
              '\u00e8' : ('e', 4),
              '\u00cc' : ('I', 4),
              '\u00ec' : ('i', 4),
              '\u00d2' : ('O', 4),
              '\u00f2' : ('o', 4),
              '\u00d9' : ('U', 4),
              '\u00f9' : ('u', 4),
              '\u01db' : ('V', 4),
              '\u01dc' : ('v', 4),
}

INVERSE_DIACRITICS = dict((v, k) for k, v in iter(DIACRITICS.items()))

def _isValidPinyinCharacter(c):
    if c in CONSONANTS:
        return True
    elif c in VOWELS:
        return True
    elif '1' <= c <= '5':
        return True
    elif c in DIACRITICS:
        return True
    elif c in COMBINING_CHARACTERS:
        return True
    elif c == ZERO_WIDTH_SPACE:
        return True
    else:
        return False

def _normalizeVowels(pinyin):
    result = ''
    i = 0
    while True:
        if i >= len(pinyin):
            break
        c = pinyin[i]
        if c in CONSONANTS:
            result += c
        elif c in VOWELS:
            if c == 'u':
                if i + 1 < len(pinyin):
                    if pinyin[i + 1] == ':':
                        result += 'v'
                        i += 1
                    else:
                        result += c
                else:
                    result += c
            elif c == '\u00fc':
                result += 'v'
            else:
                result += c
        elif c in COMBINING_CHARACTERS:
            pass
        elif c in DIACRITICS:
            result += DIACRITICS[c][0]
        else:
            msg = "Unknown character: '" + repr(c) + "', pinyin: " + repr(pinyin)
            raise Exception(msg)
        i += 1
    return result

def _listDiacritics():
    for tone in range(1, 5):
        for key, value in sorted(list(DIACRITICS.items()), key = lambda item: item[0]):
            if value[1] == tone:
                print(key, value[0])
        print()

def _splitNormalizedFragment(pinyin):
    result = []
    buf = ''
    for i in range(len(pinyin)):
        c = pinyin[i]
        buf += c
        if buf.lower() in PINYIN_SYLLABLES:
            if (i < len(pinyin) - 1):
                if (pinyin[i + 1] not in VOWELS):
                    l = _splitNormalizedFragment(pinyin[i + 1:])
                    if l != []:
                        for sublist in l:
                            sublist.insert(0, buf)
                            result.append(sublist)
                else:
                    continue
            else:
                result.append([buf])
    return result

def _getFragments(pinyin):
    result = []
    buf = ''
    for c in pinyin:
        if ('1' <= c) and (c <= '5'):
            result.append(buf)
            buf = ''
        elif c == "'":
            if buf != '':
                result.append(buf)
            buf = ''
        elif c == ' ':
            result.append(buf)
            buf = ''
        else:
            buf += c
    if buf != '':
        result.append(buf)
    return result

def _normalizeWord(pinyin):
    result = []
    frags = _getFragments(pinyin)
    i = 0

    for f in frags:
        fragment = _normalizeVowels(f)
        try:
            syllables = _splitNormalizedFragment(fragment)[-1]
        except IndexError:
            msg = 'Invalid pinyin? Is an apostrophe missing? [' + pinyin + ']'
            raise Exception(msg)

        for syllable in syllables:
            tone = 5
            for _ in range(len(syllable)):
                c = pinyin[i]
                if c == "'":
                    i += 1
                    c = pinyin[i]
                if c in DIACRITICS:
                    _, tone = DIACRITICS[c]
                elif c in COMBINING_CHARACTERS:
                    tone = _getToneFromCombiningCharacter(c)
                    i += 1
                i += 1
            if i < len(pinyin):
                if _isToneChar(pinyin[i]):
                    tone = int(pinyin[i])
                    i += 1
                elif pinyin[i] in COMBINING_CHARACTERS:
                    tone = _getToneFromCombiningCharacter(pinyin[i])
                    i += 1
            result.append(str(syllable) + str(tone))
    return result

def _getWords(pinyin):
    return pinyin.split()

def _isToneChar(c):
    if ('1' <= c) and (c <= '5'):
        return True
    else:
        return False

def _test():
    p = 'fan4guan3'
    print(_normalizeWord(p))

    p = 'f' + diacritic('a', 4) + 'nguan3r'
    print(_normalizeWord(p))

    p = "x" + diacritic('i', 1) + "an"
    print(_normalizeWord(p))

    p = "x" + diacritic('i', 1) + "'an"
    print(_normalizeWord(p))

    p = "xi" + MACRON + "'" + diacritic('a', 1) + 'n'
    print(_normalizeWord(p))

    p = 'rui4shi' + GRAVE
    print(_normalizeWord(p))

def _getToneFromCombiningCharacter(c):
    if c == MACRON:
        return 1
    elif c == ACUTE:
        return 2
    elif c == CARON:
        return 3
    elif c == GRAVE:
        return 4
    else:
        raise Exception("Not a combining character: " + c)

def _getCombiningCharacterFromTone(t):
    t = int(t)
    if t == 1:
        return MACRON
    elif t == 2:
        return ACUTE
    elif t == 3:
        return CARON
    elif t == 4:
        return GRAVE
    else:
        return ''

def sandhify(syllables, allHanzi):
    result = []
    prevTone = ''
    prevBase = ''
    prevHanzi = ''
    for i in range(len(syllables)):
        syllable = syllables[i]
        base = syllable[:-1]
        tone = syllable[-1]
        result.append(0)
        if (tone == '3') and (prevTone == '3'):
            result[i - 1] = 1
        if prevBase == 'bu' and prevHanzi == '\u4e0d':
            if tone == '4':
                result[i - 1] = 1
        if prevBase == 'yi' and prevHanzi == '\u4e00':
            result[i - 1] = 1
        prevBase = base
        prevTone = tone
        prevHanzi = allHanzi[i]
    return result

def _testSandhify():
    print(sandhify(['ni3', 'hao3', 'ma5'], '\u4f60\u597d\u5417'))
    print(sandhify(['yi1', 'ge4'], '\u4e00\u4e2a'))
    print(sandhify(['bu4', 'yao4'], '\u4e0d\u8981'))

def diacritic(vowel, tone):
    if tone == 5:
        return vowel
    else:
        return INVERSE_DIACRITICS[(vowel, tone)]

def normalize(pinyin):

    cleanedPinyin = ''
    for c in pinyin:
        if _isValidPinyinCharacter(c):
            if c != ZERO_WIDTH_SPACE:
                cleanedPinyin += c
        else:
            cleanedPinyin += ' '

    words = _getWords(cleanedPinyin)
    result = []
    for word in words:
        result.append(_normalizeWord(word))
    return result

def _useToneMarkers(pinyin, combiningCharacters=False):
    aIdx = -1
    eIdx = -1
    oIdx = -1
    uIdx = -1
    lastVowelIdx = -1

    tone = pinyin[len(pinyin) - 1]

    for i in range(len(pinyin) - 1):
        c = pinyin[i].lower()
        if c in VOWELS:
            lastVowelIdx = i
        if c == 'a':
            aIdx = i
        elif c == 'e':
            eIdx = i
        elif c == 'o':
            oIdx = i
        elif c == 'u':
            uIdx = i

    if aIdx >= 0:
        toneIdx = aIdx
    elif eIdx >= 0:
        toneIdx = eIdx
    elif uIdx == oIdx + 1:
        toneIdx = oIdx
    else:
        toneIdx = lastVowelIdx

    result = ''
    for j in range(len(pinyin) - 1):
        if j!= toneIdx:
            result += pinyin[j]
        elif combiningCharacters:
            result += pinyin[j] + _getCombiningCharacterFromTone(tone)
        else:
            result += diacritic(pinyin[j], int(tone))

    return result

AEO = ['a', 'e', 'o']

def useToneMarkers(pinyin, combiningCharacters=False):
    result = ''
    l = normalize(pinyin)
    first = True
    for w in l:
        if not first:
            result += ' '
        first = False
        useApostrophe = False
        for p in w:
            if useApostrophe and (p[0] in AEO):
                result += "'"
            useApostrophe = True
            result += _useToneMarkers(p, combiningCharacters=combiningCharacters)
    result = result.replace('v', '\u00fc')
    return result

def useToneNumbers(pinyin):
    result = ''
    l = normalize(pinyin)
    first = True
    for w in l:
        if not first:
            result += ' '
        first = False
        useApostrophe = False
        for p in w:
            if useApostrophe and (p[0] in AEO):
                result += "'"
            useApostrophe = True
            result += p
    result = result.replace('v', '\u00fc')
    return result

if __name__ == '__main__':
#    p = 'h' + diacritic('u', 1) + u'l\u00fc' + diacritic('e', 4)
#    print p
#    print useToneMarkers(p)
#    print useToneNumbers(p)
#
#    print useToneMarkers('A1yi2')
    print(normalize("zong'eryanzhi"))
