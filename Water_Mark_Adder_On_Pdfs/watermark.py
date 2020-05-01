import PyPDF2

def create_watermark(input,output):
	water_mark =PyPDF2.PdfFileReader(input)
	watermark_page = water_mark.getPage(0)
	pdf_reader = PyPDF2.PdfFileReader(output)
	pdf_writer = PyPDF2.PdfFileWriter()


	for page in range(pdf_reader.getNumPages()):
		page = pdf_reader.getPage(page)
		page.mergePage(watermark_page)
		pdf_writer.addPage(page)
		print(pdf_writer)
		
	with open('watermark_page.pdf','wb') as out:
		pdf_writer.write(out)
	

create_watermark('wtr.pdf','merged.pdf')

