# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 11:01:41 2020

@author: j.khorami
"""

import os
from pdf2image import convert_from_path

import PyPDF2

    
    
def pdftojpeg_pdf2image(path):

    
    os.chdir(path)
    
        for pdf_file in os.listdir(path):
    
            if pdf_file.endswith(".pdf"):
    
                pages = convert_from_path(pdf_file, 300)
                pdf_file = pdf_file[:-4]
    
                for page in pages:
    
                   page.save("%s-page%d.jpg" % (pdf_file,pages.index(page)), "JPEG")
                   
                   
