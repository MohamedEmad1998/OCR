# import needed libraries
import cv2 as my_cv
import pytesseract as my_pt
import os
# get the image to work on
img=my_cv.imread("textbook_image_3.PNG")

# i had some problems with tesseract installation
# so i used this line as an explicit reference to tesseract path in my PC
my_pt.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# do some preprocess to the image to prepare it for the OCR
# change the image to grey scale image
grey_img=my_cv.cvtColor(img,my_cv.COLOR_BGR2GRAY)
# remove any noise from the image
no_noise_img=my_cv.medianBlur(grey_img,3)
# apply thresholding
thr_img=my_cv.threshold(no_noise_img,0,255,my_cv.THRESH_BINARY+my_cv.THRESH_OTSU)[1]

# get text from the the image
my_config=  r'--oem 3 --psm 6'
extracted_text=my_pt.image_to_string(img, lang='eng',config=my_config)

# create new file and give it a name and write mode access
txt_file= open("textbook_image_3.txt", 'w')
# write the text taken from the image to the file
txt_file.write(extracted_text)
txt_file.close()# close the file

#count the numbers of characters
num_ch=0
num_spaces=extracted_text.count(' ')
for i in extracted_text:
    num_ch=num_ch+1
num=num_ch-num_spaces
print("number of characters is ",num)

# open the text file and show it on the screen when running the program
os.startfile("textbook_image_3.txt")
# Resize the image and show it on the screen
resized_img = my_cv.resize(img, (0, 0), fx=0.5, fy=0.5)
my_cv.imshow("image", resized_img)
my_cv.waitKey(0)


