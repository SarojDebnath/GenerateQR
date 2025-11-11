# Install the qrcode and pillow libraries first (if not already installed)
# pip install qrcode[pil]

import qrcode

# The data to encode (you can replace this with any string or URL)
data = "https://www.facebook.com/share/16K4J14rnv/"

# Create a QR code instance
qr = qrcode.QRCode(
    version=1,  # Controls the size of the QR Code (1 = smallest, 40 = largest)
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
    box_size=10,  # Size of each box in pixels
    border=4,  # Thickness of the border
)

# Add data to the QR code
qr.add_data(data)
qr.make(fit=True)

# Create an image from the QR code
img = qr.make_image(fill_color="black", back_color="white")

# Save the image
img.save("qrcode.png")

print("✅ QR code generated and saved as 'qrcode.png'")
