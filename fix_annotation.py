import glob
import xml.etree.ElementTree as ET
import os

annotations = glob.glob("./filter-images-annot/*.*")
index = 0
for annotation in annotations:
    print(annotation)
    image_path = annotation.replace("filter-images-annot", "filter-images")
    image_path = image_path.replace("xml", "jpg")

    et = ET.parse(annotation)
    root = et.getroot()
    for object in root.findall('object'):
        if "person" in object.find('name').text:
            object.find('name').text = "person"

        if "vest" in object.find('name').text:
            object.find('name').text = "safety vest"

    et.write(annotation)

    # file_name = image_path[image_path.rindex("\\") + 1: image_path.index(".jpg")]
    # new_image_path = image_path.replace(file_name, str(index).zfill(5))
    # new_annotation = annotation.replace(file_name, str(index).zfill(5))
    # index += 1
    # os.rename(image_path, new_image_path)
    # os.rename(annotation, new_annotation)