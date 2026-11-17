import qrcode

# Ask the user for input
data = input("Enter a URL or text: ")

# Generate a QR code
img = qrcode.make(data)

# Ask for file name
file_name = input("Enter a file name: ").strip()
file_name = "".join(file_name.split())
# Save the QR code
if not file_name:
    file_name = "qrcode"

img.save(f"{file_name}.png")
print(f"QR code saved as {file_name}.png")
