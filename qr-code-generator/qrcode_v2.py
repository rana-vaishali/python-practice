import qrcode
from pathlib import Path

#function for asking user input
def get_qr_data():
    return input("Enter a URL or text: ")

# Generate a QR code
def generate_qr(data):    
    return qrcode.make(data)


#function for a valid file name
def get_file_name():
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
        
        return file_name
        


data = get_qr_data()
img = generate_qr(data)
final_file_name = get_file_name()
img.save(f"{final_file_name}.png")
print(f"QR code saved as {final_file_name}.png")
