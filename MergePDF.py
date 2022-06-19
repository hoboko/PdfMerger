# -*- coding: utf-8 -*-
"""
Created on Fri Jan 14 19:19:14 2022

@author: hoboko
"""

import os
from PyPDF2 import PdfFileMerger

x = [a for a in os.listdir() if a.endswith(".pdf")]

merger = PdfFileMerger()

for pdf in x:
    merger.append(open(pdf, 'rb'))

with open("Merged.pdf", "wb") as fout:
    merger.write(fout)
    
