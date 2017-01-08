import pytesseract
import Image


class OCR(object): 
    """Class for OCR Engine"""

    def __init__(self):
        pass

    def __string__(self):
        pass

    def get_text(self, image_url):
        """Returns the text from an image"""
        img = Image.open(image_url)
        img.load()
        return pytesseract.image_to_string(img)


def main():
    p = OCR()
    print p.get_text('test.png')


if __name__ == '__main__':
    main()

