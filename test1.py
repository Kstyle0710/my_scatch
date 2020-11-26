import cv2


## Loading an image
source = './source/23445.jpg'
img = cv2.imread(source, 1)

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

def dodgeV2(x, y):
    return cv2.divide(x, 255-y, scale=256)

final_img = dodgeV2(img_gray, img_smoothing)

cv2.imshow("", final_img)
cv2.imwrite('./result/23445.jpg', final_img)
cv2.waitKey()
cv2.destroyAllWindows()

