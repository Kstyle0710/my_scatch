import cv2
import glob
from PIL import Image, ImageDraw, ImageFont
import imageio


## Loading an image
# source = './source/23445.jpg'

folder_path = 'source/*'
images = sorted(glob.glob(folder_path))

print(images)

def dodgeV2(x, y):
    return cv2.divide(x, 255-y, scale=256)

for img in images:
    name = img.split('\\')[-1]
    # source = Image.open('./source/{0}'.format(name))

    img = cv2.imread(img, 1)

## Resizing
    width, height = 650, 1000
    dim = (width, height)
    img = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)

## Converting an image into gray
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

## Inverting the image

    img_invert = cv2.bitwise_not(img_gray)

## Smoothing the image

    img_smoothing = cv2.GaussianBlur(img_invert, (21, 21), sigmaX=0, sigmaY=0)

## Obtaining the final sketch

    final_img = dodgeV2(img_gray, img_smoothing)
    cv2.imwrite('./result/new_{0}.jpg'.format(name), final_img)

print("작업 완료")
# cv2.imshow("", final_img)
# cv2.waitKey()
# cv2.destroyAllWindows()

