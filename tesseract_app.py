from cgi import test
import pyocr
import pyocr.builders
from PIL import Image
import cv2

def main(img_path, lang):
    tools = pyocr.get_available_tools()
    tool = tools[0]

    img = Image.open(img_path)

    # HSV変換
    # img_bgr = cv2.imread('image/test.jpg')
    # img_hsv = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2HSV)
    # h,s,v = cv2.split(img_hsv)
    # cv2.imshow('w,s,v', cv2.hconcat([h,s,v]))
    # cv2.imshow('v',v)
    # cv2.waitKey(0)

    builder = pyocr.builders.TextBuilder(tesseract_layout=6)
    text = tool.image_to_string(img, lang=lang, builder=builder)

    print(text)

if __name__ == '__main__':
    main('ignore/image/chi.jpg', 'chi_sim')