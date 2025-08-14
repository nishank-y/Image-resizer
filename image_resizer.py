import os
from PIL import Image

input_folder = input("Enter input folder name: ").strip()
output_folder = input("Enter output folder name: ").strip()
width = int(input("Enter new width: "))
height = int(input("Enter new height: "))
new_size = (width, height)

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

images = [f for f in os.listdir(input_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]

total = len(images)

for idx, filename in enumerate(images, start=1):
    try:
        img_path = os.path.join(input_folder, filename)
        img = Image.open(img_path)
        img_resized = img.resize(new_size)
        ext = filename.split('.')[-1]
        save_path = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}_resized.{ext}")
        img_resized.save(save_path)
        print(f"[{idx}/{total}] {filename} resized and saved to {save_path}")

    except Exception as e:
        print(f"Error processing {filename}: {e}")

print("All images processed successfully!")
