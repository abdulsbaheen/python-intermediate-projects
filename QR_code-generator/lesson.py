import qrcode as qr

def generate_qrcode(data):
    QR = qr.make(data)
    QR.save("QRcode.png")

if __name__ == "__main__":
    pass
    # main()