import glob
import xml.etree.ElementTree as ET
import os

annotations = glob.glob("./train-images-annotations/*.*")
index = 0
for annotation in annotations:
    print(annotation)
    image_path = annotation.replace("train-images-annotations", "train-images-data")
    image_path = image_path.replace("xml", "jpg")

    file_name = image_path[image_path.rindex("\\") + 1: image_path.index(".jpg")]
    new_image_path = image_path.replace(file_name, str(index).zfill(5))
    new_annotation = annotation.replace(file_name, str(index).zfill(5))

    et = ET.parse(annotation)
    root = et.getroot()
    path = root.find('path').text
    old_path_file = path[path.rindex("\\") + 1: path.index(".jpg")]
    root.find('path').text = path.replace(old_path_file, str(index).zfill(5))
    root.find('filename').text = str(index).zfill(5) + ".jpg"
    print(old_path_file, root.find('path').text)
    for object in root.findall('object'):
        if "person" in object.find('name').text:
            object.find('name').text = "person"

        if "vest" in object.find('name').text:
            object.find('name').text = "safety vest"

    et.write(annotation)


    os.rename(image_path, new_image_path)
    os.rename(annotation, new_annotation)

    index += 1