import qrcode
from pathlib import Path
from PIL import ImageColor

#function for asking user input
def get_qr_data():
     while True:
        data = input("Enter a URL or text: ").strip()
        if not data:
            print("QR data cannot be blank.")
            continue
        return data

# asking for color
def get_valid_color(prompt):   
    while True:
        color = input(prompt).strip()
        if not color:
            print("Color cannot be blank.")
            continue
        
        try:
            ImageColor.getrgb(color)
            return color
        except ValueError:
            print("Enter a valid color")     
        
    

# Generate a QR code
def generate_qr(data, forcolor, backcolor): 
    qr = qrcode.QRCode(
        box_size=10,
        border=4
        )

    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(
        fill_color=forcolor,
        back_color=backcolor
        ) 
      
    return img


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
fill_color = get_valid_color("Enter a color for QRCode: ")
back_color = get_valid_color("Enter a background color for QRCode: ")
img = generate_qr(data,fill_color,back_color)
final_file_name = get_file_name()
img.save(f"{final_file_name}.png")
print(f"QR code saved as {final_file_name}.png")
