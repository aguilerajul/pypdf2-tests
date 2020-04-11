import PyPDF2
import sys


def AppendOtherPdf(pdfPathList, finalPath, finalName='super'):
    '''
    Allow to combine multiple pdf files in 1 file

    pdfPathList = pdf path with .pdf extension

    finalPath = Where will be store it the final pdf

    finalName = The name that will have the new pdf generated
    '''
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdfPathList:
        print(pdf)
        merger.append(pdf)
    merger.write(f'{finalPath}/{finalName}.pdf')


def AddWaterMark(pdfPath, waterMarkPdfPath=None, finalName='waterMarked'):
    '''
    Add water mark by default call it DRAFT, you can use other WaterMark adding a PDF File with an specific Watermark

    pdfPath = Pdf File Path with extension .pdf

    fileName = finalName without .pdf extension
    '''

    template = PyPDF2.PdfFileReader(open(pdfPath, 'rb'))
    watermark = PyPDF2.PdfFileReader(open(
        './assets/pdf/wtm.pdf' if waterMarkPdfPath is None else waterMarkPdfPath, 'rb'))
    final_file = PyPDF2.PdfFileWriter()

    for pageNumber in range(template.getNumPages()):
        page = template.getPage(pageNumber)
        page.mergePage(watermark.getPage(0))
        final_file.addPage(page)

        with open(f'{finalName}.pdf', 'wb') as pdfFile:
            final_file.write(pdfFile)
