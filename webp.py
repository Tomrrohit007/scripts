import os
from tkinter import Tk, filedialog
import subprocess

def convert_to_webp(input_file, output_file, quality):
    cwebp_cmd = ["/usr/bin/cwebp", "-q", str(quality), input_file, "-o", output_file]
    subprocess.run(cwebp_cmd)

def select_directory():
    root = Tk()
    root.withdraw()
    path = filedialog.askdirectory(title="Select Directory")
    return path

def get_quality_input():
    while True:
        try:
            quality = int(input("Enter the quality level (0-100): "))
            if 0 <= quality <= 100:
                return quality
            else:
                print("Quality level must be between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def main():
    path = select_directory()

    output_path = os.path.join(path, "webp")
    os.makedirs(output_path, exist_ok=True)

    print("Conversion Details:")
    print("-------------------")

    quality = get_quality_input()

    for filename in os.listdir(path):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            input_file = os.path.join(path, filename)
            output_file = os.path.join(output_path, os.path.splitext(filename)[0] + '.webp')
            convert_to_webp(input_file, output_file, quality)
            print(f"{filename} -> {os.path.basename(output_file)}")

    print("-------------------")
    print("Conversion complete. WebP files are saved in the 'webp' folder.")

if __name__ == "__main__":
    main()
