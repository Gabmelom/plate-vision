import os
import cv2
import numpy as np
import pytesseract as tess
import matplotlib.pyplot as plt

image_folder = "./data/fareselmenshawii/imgs/"
label_folder = "./data/fareselmenshawii/labels/"

if __name__ == "__main__":
    # Get 1000 images from the data folder
    image_files = os.listdir(image_folder+"/test")
    image_files = image_files[:1000]

    # Get the corresponding labels by replacing the image extension with .txt
    label_files = [file.replace(".jpg", ".txt") for file in image_files]
    
    # Check if all label files exist
    for label_file in label_files:
        if not os.path.exists(label_folder+"/test/"+label_file):
            print("Label file not found: ", label_file)

    # Display one example image using OpenCV and bounding box
    image = cv2.imread("data/fareselmenshawii/imgs/test/0c756c9366a8cb10.jpg")
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    h, w, _ = image.shape
    print(h, w)

    # Read the corresponding label file
    # label_file = label_files[0]
    with open("data/fareselmenshawii/labels/test/0c756c9366a8cb10.txt", "r") as f:
        lines = f.readlines()

    for line in lines:
        # Read the YOLO annotation files
        parts = line.strip().split(" ")
        class_id = int(parts[0])
        x_center = float(parts[1])
        y_center = float(parts[2])
        width = float(parts[3])
        height = float(parts[4])

        # Convert YOLO format to x1, y1, x2, y2
        x1 = int((x_center - width/2) * w)
        y1 = int((y_center - height/2) * h)
        x2 = int((x_center + width/2) * w)
        y2 = int((y_center + height/2) * h)

        # Draw the bounding box
        cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)

    plt.imshow(image)
    plt.show()