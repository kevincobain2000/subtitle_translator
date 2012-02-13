#!/usr/bin/python
# -*- coding: utf-8 -*-
#author: Pulkit Kathuria
#Contact: www.jaist.ac.jp/~s1010205
#Licence: BSD

import argparse, os, re, sys
from subtranslate.parser import Parser
try: from mygengo import MyGengo
except ImportError:
    print "Install mygengo from git clone git://github.com/myGengo/mygengo-python.git"

HOME = os.getenv("HOME")
KEYS = (HOME+'/mygengo_keys/public_key.txt', HOME+'/mygengo_keys/private_key.txt')

def print_help_with_keys():
    print "Help with using Translator"
    print "<url>"
    exit()
    
def out_lang_codes():
    for lang in gengo.getServiceLanguages().values()[1]:
        print '{0:<10}{1:}'.format(lang.values()[2], lang.values()[3])

def findkeys(directory, regexp):
    fileList=os.listdir(directory)
    return [f for f in fileList if f.find(regexp) > -1]

gengo = MyGengo(
    public_key = open(KEYS[0]).read(),
    private_key = open(KEYS[1]).read(),
)

def translate_line(line, src_lang, trg_lang):
    translation = gengo.postTranslationJob(job = {
        'type': 'text',
        'slug': 'Translating Subtitles',
        'body_src': line,
        'lc_src': src_lang,
        'lc_tgt': trg_lang,
        'tier': 'machine',
        'auto_approve': 0,
        'comment': 'Machine Subtitle Translation',
        'callback_url': 'http://www.jaist.ac.jp/~s1010205/'
        })
    result = translation['response']['job']['body_tgt'].encode('utf-8')
    return result

def srt_translate(srt_path, source_lang, target_lang):
    parser = Parser()
    srt_target = open(target_lang+'-'+srt_path, "wb")
    parsed = parser.srtParser(srt_path)
    total_lines = len(parsed.keys())
    for idx, timing in enumerate(sorted(parsed), 1):
        srt_target.write(str(idx))
        srt_target.write('\n')
        srt_target.write(timing)
        srt_target.write('\n')
        for line in parsed[timing].splitlines():
            if not line.strip():continue
            srt_target.write(translate_line(line, source_lang, target_lang))
            srt_target.write('\n')
        srt_target.write('\n')
        sys.stdout.write("\rTranslating Line Number  %d/%s" %(idx, total_lines))
        sys.stdout.flush()
    print 'File Saved as %s'%srt_target.name
    srt_target.close()
    return ''

def __allchecks__(myarguments):
    if myarguments.s:
        print '\nLanguage Codes'
        print 'English to Target Language'
        print 'Target language to English'
        print '---------------------------'
        out_lang_codes()
        exit()
    if not myarguments.srtfiles:
        parser.print_help()
        print '\nLanguage Codes'
        print '---------------'
        out_lang_codes()
        print 'Usages (case insensitive)'
        print 'Either use abbreviation or full Lang name'
        print '-----------------------------------------'
        print 'translate_subs -i DieHard.srt -f en -t ja'
        print 'translate_subs -i DieHard.srt -f english -t japanaese'
        print 'Output --> Translated file saved to ja-Diehard.srt'
        exit()
    return ''
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(add_help = True)
    parser = argparse.ArgumentParser(description= 'Subtitle Translator')
    parser.add_argument('-i', action="store", nargs = '*', dest="srtfiles", type=argparse.FileType('rt'), help='-f subtitle.srt')
    parser.add_argument('-f', action="store", default='en', help='Source Language')
    parser.add_argument('-t', action="store", default='ja', help='Target Language')
    parser.add_argument('-s', action="store_true", default=False, help='Supported Languages')
    myarguments = parser.parse_args()

    __allchecks__(myarguments)
    totranslate = myarguments.srtfiles
    source_lang = myarguments.f[:2].lower()
    target_lang = myarguments.t[:2].lower()
    for srt in totranslate:
        srt_translate(srt.name, source_lang, target_lang)

