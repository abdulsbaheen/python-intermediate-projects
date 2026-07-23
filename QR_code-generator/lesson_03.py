import qrcode as qr
from PIL import Image
import os
#_______________________________________________
# make a function to generate a qrcode with logo
#_______________________________________________
def generate_qrcode(data, Logo, folder_name, filename,):
    # first make the QR code and describe it's properties
    QR = qr.QRCode(version=1,
                   error_correction = qr.constants.ERROR_CORRECT_H,
                   box_size=10,
                   border=4)
    # then add the data into qr img
    QR.add_data(data)
    QR.make(fit=True)
    # define  the QR how it will be looked 
    img_qr = QR.make_image(fill_color="black", back_color = "white").convert("RGB")
    img_width, img_height = img_qr.size
    
    # open the image of logo which you want to add to QR code image
    if user_permission == 1:
        try:
            logo = Image.open(Logo)
            logo = logo.resize((60,60))
            logo_width , logo_height = logo.size
        except Exception as e:
            print(f"{e}") 
    
    # final QR code image and paste the logo in the centre of qrcode
    if user_permission == 1 :
        x = int((img_width -logo_width)/2)
        y = int((img_height -logo_height)/2)
        img_qr.paste(logo, (x, y))
        path = os.path.join(folder_name, filename)
        img_qr.save(path)
        img_qr.show()
    else:
        path = os.path.join(folder_name, filename)
        img_qr.save(path)    
        img_qr.show()
    
    #-----------------------------------------------
    #----------------END PROCESS--------------------
    #-----------------------------------------------
    
#---------------------------------------------------------------------
#-----------MAKE A FUNCTION TO SAVE THE QR CODE IN A FOLDER ----------    
#---------------------------------------------------------------------   
def save_qrcode_in_folder(data, Logo, folder_name, filename):
    # check if the folder has already exist or not
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)
        
    generate_qrcode(data, Logo, folder_name, filename)

if __name__ == "__main__":
    
    data = input("\nEnter the data to encode into the QR code: ")
    
    print("\nDo you want to add a logo in QR code or not.")
    
    user_permission = int(input("\nplease enter 0 for not ,and 1 for yes:"))
    
    if user_permission == 1: 
        Logo = input("\nEnter the logo file address which you want to add in your QRcode (with .png (ext)) :")
    else:
        Logo = None    
    
    folder= input("\nEnter the folder name where you want to save the QR code: ")
    
    file = input("\nEnter the filename to save the QR code (with .png extension): ")
    if user_permission == 1:
       save_qrcode_in_folder(data, Logo, folder, file)
    else:
       save_qrcode_in_folder(data, Logo, folder, file)