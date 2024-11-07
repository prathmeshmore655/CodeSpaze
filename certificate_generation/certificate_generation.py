import os
from PIL import Image, ImageDraw, ImageFont
from reportlab.pdfgen import canvas
from tkinter import Tk, Label, Entry, Button, messagebox

# Function to generate the certificate
def generate_certificate(name, date, template_path, output_folder):
    try:
        # Open certificate template
        certificate = Image.open(template_path)
        draw = ImageDraw.Draw(certificate)

        # Use default font (platform-independent)
        font = ImageFont.load_default()

        # Add name and completion date
        draw.text((300, 250), name, fill="black", font=font)
        draw.text((300, 350), f"Completed on: {date}", fill="black", font=font)

        # Save the certificate as an image
        img_output = os.path.join(output_folder, f"{name}_certificate.png")
        certificate.save(img_output)

        # Convert image to PDF
        pdf_output = os.path.join(output_folder, f"{name}_certificate.pdf")
        pdf = canvas.Canvas(pdf_output, pagesize=certificate.size)
        pdf.drawImage(img_output, 0, 0, width=certificate.width, height=certificate.height)
        pdf.showPage()
        pdf.save()

        messagebox.showinfo("Success", f"Certificate generated for {name}!")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Function to handle button click in GUI
def generate_from_gui():
    name = name_entry.get()
    date = date_entry.get()

    if not name or not date:
        messagebox.showerror("Input Error", "Please enter both name and date.")
        return

    template_path = r"/home/ordinary-person/Desktop/Codspaz/certificate_generation/template.png"  # Update with the path to your template
    output_folder = "./Certificates"
    os.makedirs(output_folder, exist_ok=True)

    generate_certificate(name, date, template_path, output_folder)

# Set up GUI using tkinter
root = Tk()
root.title("Automated Certificate Generator")

# GUI Labels and Entries
Label(root, text="Intern Name:").grid(row=0, column=0, padx=10, pady=10)
name_entry = Entry(root, width=30)
name_entry.grid(row=0, column=1, padx=10, pady=10)

Label(root, text="Completion Date:").grid(row=1, column=0, padx=10, pady=10)
date_entry = Entry(root, width=30)
date_entry.grid(row=1, column=1, padx=10, pady=10)

# Generate Button
Button(root, text="Generate Certificate", command=generate_from_gui).grid(row=2, columnspan=2, pady=20)

# Start the GUI loop
root.mainloop()
