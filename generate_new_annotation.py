import glob
import xml.etree.ElementTree as ET
import os
from shapely.geometry import Polygon

def get_object_pylogon(object):
    bndbox = object.find('bndbox')
    xmin = int(bndbox.find('xmin').text)
    ymin = int(bndbox.find('ymin').text)
    xmax = int(bndbox.find('xmax').text)
    ymax = int(bndbox.find('ymax').text)

    object_polygon = Polygon([(xmin, ymin), (xmax, ymin), (xmax, ymax), (xmin, ymax)])
    return object_polygon

annotations = glob.glob("./train-images-annotations/*.*")
for annotation in annotations:
    print(annotation)
    new_annotation = annotation.replace("train-images-annotations", "train-images-annotations-new")

    et = ET.parse(annotation)
    root = et.getroot()
    path = root.find('path').text
    old_path_file = path[path.rindex("\\") + 1: path.index(".jpg")]

    print(old_path_file, root.find('path').text)
    for object in root.findall('object'):
        if "person" in object.find('name').text:
            object_polygon = get_object_pylogon(object)
            count = 0
            for object_2 in root.findall('object'):
                if ("safety vest" in object_2.find('name').text) or ("helmet" in object_2.find('name').text):
                    object_2_polygon = get_object_pylogon(object_2)

                    intersection = object_polygon.intersection(object_2_polygon)
                    if (intersection.area / object_2_polygon.area) > 0.6:
                        count += 1

            if count == 0:
                object.find('name').text = "person without safety"
            elif count == 1:
                object.find('name').text = "person with partial safety"
            else:
                object.find('name').text = "person with full safety"
    et.write(new_annotation)

#
#
# polygon = Polygon([(3, 3), (5, 3), (5, 5), (3, 5)])
# other_polygon = Polygon([(3, 3), (5, 3), (5, 5), (3, 5)])
# intersection = polygon.intersection(other_polygon)
# print(intersection.area)
# # 0.5