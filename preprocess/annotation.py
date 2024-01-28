import cv2
import os
import xml.etree.ElementTree as ET

def read_annotations(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    annotations = {}

    for track in root.findall(".//track"):
        label = track.attrib["label"]

        for box in track.findall(".//box"):
            frame_number = int(box.attrib["frame"])
            xmin = int(float(box.attrib["xtl"]))
            ymin = int(float(box.attrib["ytl"]))
            xmax = int(float(box.attrib["xbr"]))
            ymax = int(float(box.attrib["ybr"]))

            if frame_number not in annotations:
                annotations[frame_number] = []

            annotations[frame_number].append({
                'label': label,
                'bbox': (xmin, ymin, xmax, ymax)
            })

    return annotations

def convert_to_yolo_format(class_id, image_width, image_height, bbox):
    x_center = (bbox[0] + bbox[2]) / 2 / image_width
    y_center = (bbox[1] + bbox[3]) / 2 / image_height
    width = (bbox[2] - bbox[0]) / image_width
    height = (bbox[3] - bbox[1]) / image_height

    return f"{class_id} {x_center} {y_center} {width} {height}"

def split_video(video_path, xml_file, output_image_directory, output_annotation_directory, frame_rate=1):
    cap = cv2.VideoCapture(video_path)
    annotations = read_annotations(xml_file)

    frame_number = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        if frame_number in annotations:
            image_height, image_width, _ = frame.shape

            # Save the frame as an image
            output_image_file = os.path.join(output_image_directory, f"frame_{frame_number:04d}.jpg")
            cv2.imwrite(output_image_file, frame)

            # Save YOLO format annotation to file
            annotation_file_path = os.path.join(output_annotation_directory, f"frame_{frame_number:04d}.txt")
            with open(annotation_file_path, 'w') as yolo_file:
                for annotation in annotations[frame_number]:
                    xmin, ymin, xmax, ymax = annotation['bbox']
                    label = annotation['label']

                    # Get class_id from the class_ids dictionary
                    class_id = class_ids.get(label)
                    if class_id is not None:
                        yolo_format = convert_to_yolo_format(class_id, image_width, image_height, (xmin, ymin, xmax, ymax))
                        yolo_file.write(f"{yolo_format}\n")

        # Create the output directories if they don't exist
        os.makedirs(output_image_directory, exist_ok=True)
        os.makedirs(output_annotation_directory, exist_ok=True)

        # Save the frame if it's within the desired frame rate
        if frame_number % int(cap.get(cv2.CAP_PROP_FPS) / frame_rate) == 0:
            frame_number += 1
            continue

        frame_number += 1

    cap.release()

if __name__ == "__main__":
    video_directory = "C:/Users/user/Downloads/FYP/fypfiles/mbgdataset/flightavi"
    annotation_directory = "C:/Users/user/Downloads/FYP/fypfiles/mbgdataset/flightann"
    output_image_directory = "C:/Users/user/Downloads/projects/MBGprocess/imageframes"
    output_annotation_directory = "C:/Users/user/Downloads/projects/MBGprocess/labelframes"
    frame_rate = 1

    class_ids = {"tire": 0, "bottle": 1, "bucket": 2, "watertank": 3, "pool": 4, "puddle": 5}

    video_files = [f for f in os.listdir(video_directory) if f.endswith(".avi")]

    for video_file in video_files:
        video_path = os.path.join(video_directory, video_file)
        xml_file = os.path.join(annotation_directory, f"{os.path.splitext(video_file)[0]}.xml")
        split_video(video_path, xml_file, output_image_directory, output_annotation_directory, frame_rate)
