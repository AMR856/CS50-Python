#!/usr/bin/python3
from PIL import Image, ImageOps
import sys

VALID_FORAMTS = ['jpg', 'jpeg', 'png']
def main():
    if len(sys.argv) == 3:
        input_image = sys.argv[1]
        output_image = sys.argv[2]
        try:
            input_extension = input_image.split('.')[1].lower()
            output_extension = output_image.split('.')[1].lower()
            if input_extension not in VALID_FORAMTS:
                print('Invalid input')
                sys.exit(1)
            if output_extension not in VALID_FORAMTS:
                print('Invalid output')
                sys.exit(1)
            if input_extension != output_extension:
                print('Input and output have different extensions')
                sys.exit(1)
            try:
                im_input = Image.open(input_image)
                shirt_image = Image.open('shirt.png')
                fittted_input = ImageOps.fit(im_input, size=(600, 600))
                fittted_input.paste(shirt_image, (0, 0), shirt_image)
                fittted_input.save(output_image)
                sys.exit(0)
            except FileNotFoundError:
                print("File wasn't found")
                sys.exit(1)
        except IndexError:
            print('Invalid input')
            sys.exit(1)

    elif len(sys.argv) > 3:
        print('Too many command-line arguments')
    else:
        print('Too few command-line arguments')
    sys.exit(1)

if __name__ == '__main__':
    main()
