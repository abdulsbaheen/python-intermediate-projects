from pypdf import PdfWriter
import os
import shutil
merger = PdfWriter()


def pdf_merger(user_path):
    
    path = user_path
    try:
        path_files = os.listdir(path)
    
        pdf_files = []
    except Exception as e:
         print("\n",e)    
        
    try:
        for filename in path_files:
            if filename.endswith(".pdf"):
                pdf_files.append(filename)
    except Exception as e:
        print("\n",e)
    new_path = os.makedirs("output_pdf", exist_ok=True)  
    
    try:
        with open("output_pdf/new_merged_pdf.pdf" , "wb") as out_put:
            for each_pdf in pdf_files:
                merger.append(os.path.join(path,each_pdf))
            merger.write(out_put)
            merger.close()  
    
            print("pdf is merger successfully")
    except Exception as e:
        print("\n",e)  


if __name__ == "__main__":
    print("________________________________________________________________________")
    print("------------------------------- PDF MERGER------------------------------")
    print("________________________________________________________________________")
    print("\nTHIS IS THE PRGRAM WHERE YOU CAN MERG MULTIPLE PDF FILES INTO ONE")
    print("\nenter the path from where you want to merg pdf (please give the exect path)")
    user_path = input("/")
    pdf_merger(user_path)
