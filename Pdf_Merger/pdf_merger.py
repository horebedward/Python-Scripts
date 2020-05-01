import PyPDF2
import sys

filenames  = sys.argv[1:]

def pdf_merger(input):
	for pdf in input:
		merger = PyPDF2.PdfFileMerger()
		merger.append(pdf)	
	merger.write('super.pdf')


pdf_merger(filenames)

