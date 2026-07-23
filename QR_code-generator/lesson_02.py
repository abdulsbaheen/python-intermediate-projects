import qrcode as qr
# make a function to generate QR code
def generate_qrcode(data, filename):
    QR = qr.make(data)
    QR.save(filename)
    print(f"QR code saved as {filename}")

def main():
    print("-"*30)
    print("     QR Code Generator   ")
    print("-"*30)
    print("This program generates a QR code from the data you provide")
    print("\nTypes to store in the QR code")
    print("1.Website URl")
    print("2.Mobile numbers")
    print("3.Emails")
    print("4.Texts")
    print("5.Wifi passwords")

    input_data = input("\nPlease enter the data you want to encode into the QR code: ")
    #check the input data and generate the QR code accordingly
    if input_data == "1":
        website_url = input("Please enter the website URL: ")
        web_img = "weblink_qrcode.png"
        generate_qrcode(website_url, web_img)
    # check for other types of data  
    elif input_data == "2":
        mobile_numbel = input("Please enter the mobile number : ")
        num_img = "number_qrcode.png"
        generate_qrcode(mobile_numbel, num_img)
    # check for other types of data    
    elif input_data == "3":
        Email = input("Please enter the Email: ")
        e_img = "email_qrcode.png"
        generate_qrcode(Email, e_img)
    # check for other types of data    
    elif input_data == "4":
        Text = input("Please enter the Text: ")
        text_img = "text_qrcode.png"
        generate_qrcode(Text, text_img)
    # check for other types of data    
    elif input_data == "5":
        wifi_password = input("Please enter the Wifi password: ")
        password_img = "password_qrcode.png"
        generate_qrcode(wifi_password, password_img)
    # if the input data is not valid, print an error message
    else:
        print("Invalid choice. Please try again.")    
        
if __name__ == "__main__":
    main()        