import qrcode

# Les données que vous souhaitez encoder dans le QR Code, par exemple une URL
data = "https://soundcloud.com/oui-koui"

# Création d'une instance de QR Code
qr = qrcode.QRCode(
    version=1,  # Version du QR Code, 1 à 40, où 1 est la plus petite taille
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Niveau de correction d'erreur
    box_size=10,  # Taille de chaque boîte dans le QR code
    border=4,  # Largeur de la bordure autour du QR code
)

# Ajout des données au QR Code
qr.add_data(data)
qr.make(fit=True)

# Création d'une image du QR Code et sauvegarde
img = qr.make_image(fill='black', back_color='white')
img.save("myqr.png")

print("QR Code generated successfully!")