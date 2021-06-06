# ********************* COPYING PyPDF2 ***************************
import PyPDF2

with open("C:/Users/Satish/Desktop/practice.pdf", "rb") as f:
    pdfobj = PyPDF2.PdfFileReader(f)
    objw = PyPDF2.PdfFileWriter()
    pgnum = pdfobj.getNumPages()
    print("No of pages in the pdf = ", pgnum)
    for i in range(pgnum):
        pageobj = pdfobj.getPage(i)
        d = pageobj.extractText()
        print(d)
        objw.addPage(pageobj)
    # pageindex = [11, 13, 15, 17]
    # for i in pageindex:
    # pageobj = pdfobj.getPage(i)
    # d = pageobj.extractText()
    # print(d)
    # objw.addPage(pageobj)
with open("copy2.pdf", "wb") as f1:
    objw.write(f1)

# **************************** MERGING *****************************
import PyPDF2

objw = PyPDF2.PdfFileWriter()

with open("copy1.pdf", "rb") as f1:
    pdfobj1 = PyPDF2.PdfFileReader(f1)
    pgnum1 = pdfobj1.getNumPages()
    for i in range(pgnum1):
        pageobj1 = pdfobj1.getPage(i)
        d1 = pageobj1.extractText()
        print(d1)
        objw.addPage(pageobj1)
with open("copy2.pdf", "rb") as f2:
    pdfobj2 = PyPDF2.PdfFileReader(f2)
    pgnum2 = pdfobj2.getNumPages()
    for j in range(pgnum2):
        pageobj2 = pdfobj2.getPage(j)
        d2 = pageobj2.extractText()
        print(d2)
        objw.addPage(pageobj2)
with open("merg.pdf", "wb") as f3:
    objw.write(f3)

# ******************************* SPLITTING ********************************
import PyPDF2

objw = PyPDF2.PdfFileWriter()
with open("copy2.pdf", "rb") as f1:
    objr = PyPDF2.PdfFileReader(f1)
    n = objr.getNumPages()
    print("no of pages : ", n)
    for i in range(n):
        Fname = "split" + str(i) + ".pdf"
        print("_______________________________________")
        print(Fname)
        print("_______________________________________")
        pobj = objr.getPage(i)
        d2 = pobj.extractText()
        print(d2)
        objw.addPage(pobj)

with open("split.pdf", "wb") as f2:
    objw.write(f2)