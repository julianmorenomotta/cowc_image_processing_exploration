import cv2

input_image = '/Users/julianmoreno/Proyectos/Birds/bahn_park/selfgenerated_detection_patches_320_True/Columbus_CSUAV_AFRL/Columbus_EO_Run01_s2_301_15_00_31.99319028-Oct-2007_11-00-31.993_Frame_1.0.0.check.jpg'

image = cv2.imread(input_image)

scaling_factor = 15 / 50  # 15cm/pixel to 50cm/pixel
print(f'scaling factor: {scaling_factor}')

new_width = int(image.shape[1] * scaling_factor +0.5)
new_height = int(image.shape[0] * scaling_factor+.5)
new_dimensions = (new_width, new_height)

# print the processing result values
print(f'the image has been resized from {image.shape} to {new_dimensions}')


resized_image = cv2.resize(image, new_dimensions)

cv2.imwrite('output_img1cd.jpg', resized_image)
