import glob
import cv2
image_paths = glob.glob("./train-images-data/*.*")

for image_path in image_paths:
    img = cv2.imread(image_path)
    cv2.imwrite(image_path, img)