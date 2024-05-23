import qrcode


qr_code = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

qr_code.add_data('This is my data.')
qr_code_image = qr_code.make_image()
qr_code_image.save('qr_code.png')
print('qr code is generated.')
print('just a print statement.')