import os
import argparse

from PIL import Image, ImageEnhance, ImageFilter

def improve_image(image_path):
    """Improve the quality of the image"""
    
    # Open the image file
    image = Image.open(image_path)
    
     # Apply sharpness enhancement
    enhancer = ImageEnhance.Sharpness(image)
    image = enhancer.enhance(2.0)
    
    # Apply contrast enhancement
    enhancer = ImageEnhance.Contrast(image)
    image = enhancer.enhance(1.0)
    
    # Apply brightness enhancement
    enhancer = ImageEnhance.Brightness(image)
    image = enhancer.enhance(1.1)

    # Save the improved image
    base_name = os.path.basename(image_path)
    dir_name = os.path.dirname(image_path)
    name, ext = os.path.splitext(base_name)
    output_path = os.path.join(dir_name, f"{name}_improved{ext}")
    image.save(output_path)
    print(f"Image saved to {output_path}")
    
def main():
    """Parse the command line arguments"""
    
    parser = argparse.ArgumentParser(description="Improve image quality")
    parser.add_argument("image_path", help="Path to the image file")
    args = parser.parse_args()
    
    improve_image(args.image_path)

if __name__ == "__main__":
    main()
    