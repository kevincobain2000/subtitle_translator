#! /usr/bin/env python
# -*- coding: utf-8 -*-
import sys 

if __name__ == '__main__':
    prev = []
    with open('TOC.rst') as f:
        toc = f.readlines()
    index = open('index.rst','wb')
    for line in toc:
        if not line.startswith('@'): prev.append(line.strip())
        if line.startswith('@'):
            with open(line.strip('@').strip()) as chapter:
                include = chapter.readlines()
                for line in include:
                    if prev[-2] == '::':
                        index.write('\t')
                    index.write(line)
        else:
            index.write(line)
                
        
