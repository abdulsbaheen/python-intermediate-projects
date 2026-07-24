from pypdf import PdfWriter
import os

merger = PdfWriter()

merger.append("input's_pdf/example_1.pdf")
merger.append("input's_pdf/example_2.pdf")

with open("output/new.pdf", "wb") as output_file:
    merger.write(output_file)

merger.close()

print("PDFs merged successfully!")

# path = "input's_pdf"


# dirname = os.listdir(path)

# for i in range(len(dirname)-1):
    
#     old = os.path.join(path,dirname[i])
#     new = os.path.join(path,"example_"+str(i+1)+ ".pdf")
#     os.rename(old,new)