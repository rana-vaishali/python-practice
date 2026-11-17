import qrcode
from pathlib import Path

# Ask the user for input
data = input("Enter a URL or text: ")

# Generate a QR code
img = qrcode.make(data)

while True:
    # Ask for file name
    file_name = input("Enter a file name: ").strip()
    file_name = "".join(file_name.split())
    # Save the QR code
    if not file_name:
        print("File name cannot be blank")
        continue
    # check if the file already exists
    file = Path(f"{file_name}.png")
    if file.exists():
        print("File already exists!")
        continue
    else:
        break

img.save(f"{file_name}.png")
print(f"QR code saved as {file_name}.png")
