import qrcode

# Ask the user for input
data = input("Enter a URL or text: ")

# Generate a QR code
img = qrcode.make(data)

# Save the QR code
img.save("qrcode.png")

print("QR code generated successfully!")
