'''
Alpha : is the transparency channel in open CV , starting from 0 (fully transparent) to 255 (fully opaque)

Beta : is used to control brightness or contrast of the image

Gamma : correction applied to brightness , it is used to make the image used more natural

Horizontal ,vertical and Alpha integeration . These are types of image concatenation .
'''
import cv2

import logging


def main():
    img1 = cv2.imread('sun-man_cropped.jpg')
    img2 = cv2.imread('monkey-nft.png')
    img3 = cv2.imread('porche911GT3R.jpg')
    img4=cv2.imread('moon1_cropped.jpg')
    # v_combined_img = combine_vertically(img1, img2)
    # show_img("vertical", v_combined_img)

    height = img1.shape[0]
    width = img1.shape[1]

    beta = 0.5
    overlay_img = overlay(img1,img2,beta)
    overlay_img2 = overlay(img3,img4,beta)

    # overlay_img , overlay_img2 = crop_img(overlay_img , overlay_img2 , )
    v_combined_img = combine_vertically(overlay_img,overlay_img2)

    show_img("overlayed_img",v_combined_img)

def overlay(img1,img2,beta):
    height = img1.shape[0]
    width = img1.shape[1]
    img1 = cv2.resize(img1, (width // 2, height // 2)).copy()
    img2 = cv2.resize(img2, (width // 2, height // 2)).copy()
    beta = 0.5
    overlay_img = cv2.addWeighted(img1, 1 - beta, img2, beta, 0)
    return overlay_img

def combine_vertically(img1, img2):
    if img1 is None or img2 is None:
        print("unable to load images")
    else:
        img1_width = img1.shape[1]
        img2_width = img2.shape[1]
        img1= cv2.resize(img1, (img1_width // 2, img1.shape[0] // 2)).copy()
        img2 = cv2.resize(img2, (img1_width // 2, img2.shape[0] // 2)).copy()

        print(img1.shape[1] ,img2.shape[1] )
        print(img1.shape[0] ,img2.shape[0] )
        v_combined = cv2.vconcat([img1, img2])
        return v_combined


def combine_horizontally(img1, img2):
    pass



def crop_img(img1, img2, is_vertical=True):
    cropped_img1 = img1
    cropped_img2 = img2
    min_value = 0

    img1_height = img1.shape[0]
    img2_height = img2.shape[0]

    img1_width = img1.shape[1]
    img2_width = img2.shape[1]

    if not is_vertical:

        if img1_height > img2_height:
            min_value = img2_height
            cropped_img1 = img1[0:0 + min_value,0:0+img1_width]  # gives a range of x and y-axis coordinates to crop
        elif img2_height > img1_height:
            min_value = img1_height
            cropped_img2 = img2[0:0 + min_value , 0:0+img2_width]  # gives a range of x and y-axis coordinates to crop

    elif is_vertical:

        if img1_width > img2_width:
            min_value = img2_width
            cropped_img1 = img1[0:0+img1_height,0:0 + min_value]
        elif img2_width > img1_width:
            min_value = img1_width
            cropped_img2 = img2[0:0+img2_height,0:0 + min_value]

    else:
        logging.exception("Error occurred cropping images ...")

    return cropped_img1, cropped_img2



def show_img(window_name, img):
    cv2.imshow(window_name, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
