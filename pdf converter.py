import PyPDF2
import sys

# Open the PDF file
pdf_file = open('example.pdf', 'rb')

# Create a PDF reader object
pdf_reader = PyPDF2.PdfFileReader(pdf_file)

# Get the number of pages in the PDF file
num_pages = pdf_reader.getNumPages()

# Create a PDF writer object
pdf_writer = PyPDF2.PdfFileWriter()

# Add each page in the PDF file to the PDF writer object
for page_num in range(num_pages):
    page = pdf_reader.getPage(page_num)
    pdf_writer.addPage(page)

# Save the PDF file to a new file
pdf_writer.write(open('example.txt', 'wb'))

# Close the PDF file
pdf_file.close()