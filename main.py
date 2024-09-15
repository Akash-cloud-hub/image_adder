'''
Alpha : is the transparency channel in open CV , starting from 0 (fully transparent) to 255 (fully opaque)

Beta : is used to control brightness or contrast of the image

Gamma : correction applied to brightness , it is used to make the image used more natural

Horizontal ,vertical and Alpha integeration . These are types of image concatenation .
'''
import cv2

def main():
    img1 = cv2.imread('moon1_cropped.jpg')
    img2 = cv2.imread('sun-man_cropped.jpg')

    print('height' , img1.shape[0])
    print('width' , img1.shape[1])

    print('height', img2.shape[0])
    print('width', img2.shape[1])


    v_combined = cv2.vconcat([img1,img2])
    cv2.imshow(v_combined)


if __name__ == '__main__':
    main()