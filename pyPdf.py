import PyPDF2
with open("C:/Users/Satish/Desktop/python.pdf","rb") as f:
    pdfobj = PyPDF2.PdfFileReader(f)
    pgnum = pdfobj.getNumPages()
    print("No of pages in the pdf = ",pgnum)
    for i in range(pgnum):
        pageobj = pdfobj.getPage(i)
        d = pageobj.extractText()
        print(d)
    """pageindex = [1,3,5,7,9]
        for i in pageindex:
            pageobj = pdfobj.getPage(i)
            d = pageobj.extractText()
            print(d)"""
with open("python.txt","w") as f1:
    f1.write(d)



"""import PyPDF2
with open("C:/Users/Satish/Desktop/python.pdf","rb") as f:
    pdfobj = PyPDF2.PdfFileReader(f)
    pdfwriter = PyPDF2.PdfFileWriter()
    pgnum = pdfobj.getNumPages()

    pageobj = pdfobj.getPage(1)
    pdfwriter.addPage(pageobj)
f2 = open("python1.pdf","wb")
pdfwriter.write(f2)
f2.close()"""