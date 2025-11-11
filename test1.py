import qrcode
import urllib.parse

html_content = """
<!DOCTYPE html>
<html lang='en'>
<head>
  <meta charset='UTF-8'>
  <meta name='viewport' content='width=device-width, initial-scale=1.0'>
  <title>Choose a Link</title>
</head>
<body style='font-family: Arial; text-align: center; margin-top: 50px;'>
  <h2>Welcome! Choose a link:</h2>
  <a href='https://www.openai.com' target='_blank'>Visit OpenAI</a><br><br>
  <a href='https://www.google.com' target='_blank'>Go to Google</a><br><br>
  <a href='https://www.github.com' target='_blank'>Go to GitHub</a><br><br>
  <a href='https://wa.me/1234567890' target='_blank'>Chat on WhatsApp</a><br><br>
</body>
</html>
"""

# Encode HTML as a data URI
data_uri = "data:text/html," + urllib.parse.quote(html_content)

# Generate QR
img = qrcode.make(data_uri)
img.save("embedded_html_qr.png")

print("✅ QR code with embedded HTML saved as 'embedded_html_qr.png'")
