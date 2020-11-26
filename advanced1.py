import cv2
import glob


## Loading an image

folder_path = 'source/*'
images = sorted(glob.glob(folder_path))

print(images)

def dodgeV2(x, y):
    return cv2.divide(x, 255-y, scale=256)

for img in images:
    name = img.split('\\')[-1]

    img = cv2.imread(img, 1)

    h, w, c = img.shape
    # print('{0}, {1}, {2}'.format(h, w, c))

    if w > h:
        width, height = 1000, 650
        dim = (width, height)
        img = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)

    else:
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
    cv2.imwrite('./result/new1_{0}.jpg'.format(name), final_img)

print("작업 완료")


