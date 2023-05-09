import qrcode


content = str(input('QR code content: '))
code_color_G = int(input('Code color - R: '))
code_color_B = int(input('Code color - G: '))
code_color_R = int(input('Code color - B: '))
background_color_R = int(input('Background color - R: '))
background_color_G = int(input('Background color - G: '))
background_color_B = int(input('Background color - B: '))
file_name = str(input('Write the file name: '))


qr_obj = qrcode.QRCode(version = None,
                       error_correction = qrcode.constants.ERROR_CORRECT_H)

qr_obj.add_data(content)
qr_obj.make(fit = True)

qr_img = qr_obj.make_image(fill_color = (code_color_R, code_color_G, code_color_B),
                           back_color = (background_color_R, background_color_G, background_color_B))

qr_img.save(f'{file_name}.png')


