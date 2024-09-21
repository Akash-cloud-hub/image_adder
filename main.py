'''
Alpha : is the transparency channel in open CV , starting from 0 (fully transparent) to 255 (fully opaque)

Beta : is used to control brightness or contrast of the image

Gamma : correction applied to brightness , it is used to make the image used more natural

Horizontal ,vertical and Alpha integeration . These are types of image concatenation .
'''
import cv2


def main():
    img1 = cv2.imread('moon1_cropped.jpg')
    img2 = cv2.imread('monkey-nft.png')
    v_combined_img = combine_vertically(img1, img2)
    show_img("vertical", v_combined_img)


def combine_vertically(img1, img2):
    if img1 is None or img2 is None:
        print("unable to load images")
    else:
        # print('height', img1.shape[0])
        # print('width', img1.shape[1])
        #
        # print('height', img2.shape[0])
        # print('width', img2.shape[1])
        # v_combined = cv2.vconcat([img1, img2])
        # return v_combined
        img1 , img2 = crop_img(img1 , img2 , True)
        v_combined = cv2.vconcat([img1, img2])
        return v_combined


def combine_horizontally(img1, img2):
    pass


def crop_img(img1, img2, is_vertical=True):
    cropped_img1 = img1
    cropped_img2 = img2
    min_value = 0

    if not is_vertical:
        img1_height = img1.shape[0]
        img2_height = img2.shape[0]

        if img1_height > img2_height:
            min_value = img2_height
            cropped_img1 = img1[0:0 + min_value]  # gives a range of x and y-axis coordinates to crop
        elif img2_height > img1_height:
            min_value = img1_height
            cropped_img2 = img2[0:0 + min_value]  # gives a range of x and y-axis coordinates to crop

    elif is_vertical:
        img1_width = img1.shape[1]
        img2_width = img2.shape[1]

        if img1_width > img2_width:
            min_value = img2_width
            cropped_img1 = img1[0:0 + min_value]
        elif img2_width > img1_width:
            min_value = img1_width
            cropped_img2 = img2[,0:0 + min_value]


    else:
        print("Error")

    return cropped_img1, cropped_img2


def show_img(window_name, img):
    cv2.imshow(window_name, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
