#! /usr/bin/env python
# -*- coding: utf-8 -*-
import re

class Parser(object):
    def srtParser(self, srtfile):
        timings_text = {}
        SRTFILE = open(srtfile).readlines()
        in_out_time = re.compile('\d\d:\d\d.*?-->.*?\d\d:\d\d.*')
        count = 1
        for line in SRTFILE:
            match_time = re.search(in_out_time, line)
            if match_time:
                count += 1
                in_out = match_time.group().strip()
                timings_text[in_out] = ''
            else:
                if str(count) != line.strip():
                    timings_text[in_out] += line
        return timings_text

if __name__ == "__main__":
    parser = Parser()
    parsed = parser.srtParser('sample.srt')
    for idx,i in enumerate(sorted(parsed), 1):
        print idx
        print i
        print parsed[i].strip()
        print


