# -*- coding: utf-8 -*-

import pdfkit


class WebSiteToPdf:
    """Class to convert websites to pdf"""

    def __init__(self, website, pdf_file):
        self.website = website
        self.convert = ''
        self.pdf_file = pdf_file

    def convert_site(self):

        while self.convert not in ['Y', 'N']:
            self.convert = input("Save %s to PDF (Y/N)? " % self.website).upper()

        if self.convert == 'Y':
            pdfkit.from_url(self.website, self.pdf_file)

        else:
            print("%s not saved as PDF" % self.website)
