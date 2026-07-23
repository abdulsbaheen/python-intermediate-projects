import qrcode as qr

def generate_qrcode(data, filename):
    QR = qr.make(data)
    QR.save(filename)
    print(f"QR code saved as {filename}")

if __name__ == "__main__":
    pass
    # input_data = input("Enter the data to encode into the QR code: ")
    # generate_qrcode(input_data, "QRcode.png")
    