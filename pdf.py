from heapq import merge
import PyPDF2
import sys

# save arguments
input_file = sys.argv[1]
wt_file = sys.argv[2]
output_file = sys.argv[3]

# open input and watermark file as read binary
with open(input_file, 'rb') as in_file, open(wt_file, 'rb') as w_file:
    # Read input and watermark file page
    in_pdf = PyPDF2.PdfFileReader(in_file)
    w_pdf = PyPDF2.PdfFileReader(w_file)

    # get watermark page
    w_page = w_pdf.getPage(0)

    # output writer
    output = PyPDF2.PdfFileWriter()

    # iterate though input file pages
    for i in range(in_pdf.getNumPages()):

        # get i'th page of the input file
        pdf_page = in_pdf.getPage(i)

        # merge watermark with input page
        pdf_page.mergePage(w_page)

        # add page to output writer
        output.addPage(pdf_page)

    # write the output page to the output pdf
    with open(output_file, 'wb') as merged_file:
        output.write(merged_file)

# **pdf merger**
# inputs = sys.argv[1:]


# def pdf_combiner(pdf_list):
#     merger = PyPDF2.PdfFileMerger()
#     for pdf in pdf_list:
#         print(pdf)
#         merger.append(pdf)
#     merger.write('super2.pdf')


# *****pdf_combiner(inputs)******

# make new pdf and rotate pages

# with open('dummy.pdf', 'rb') as file:
#     reader = PyPDF2.PdfFileReader(file)
#     page = reader.getPage(0)
#     page.rotateCounterClockwise(90)
#     writer = PyPDF2.PdfFileWriter()
#     writer.addPage(page)

#     with open('tilt.pdf', 'wb') as new_file:
#         writer.write(new_file)
