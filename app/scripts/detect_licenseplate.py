import cv2
import numpy as np
import easyocr as ocr
import tensorflow as tf
import io

from PIL import Image
from tensorflow.keras.preprocessing.image import img_to_array

# Helper Functions
def yolo_to_voc(x,y,w,h):
    x1 = (x - w/2)
    y1 = (y - h/2)
    x2 = (x + w/2)
    y2 = (y + h/2)
    
    return int(x1), int(y1), int(x2), int(y2)

# Helper Function
def voc_to_yolo(x1, y1, x2, y2):
    x = (x1 + x2) / 2
    y = (y1 + y2) / 2
    w = x2 - x1
    h = y2 - y1
    return x, y, w, h

# Find License Plate on Image
def find_license_plate(img, model):
        
    height, width, = img.shape[0], img.shape[1]
    
    data = []
    
    img_array = img_to_array(cv2.resize(img, (224, 224)))
    img_array = img_array / 255.0
    
    data.append(img_array)

    prediction = model.predict(np.array(data, dtype=np.float32))
    px, py, pw, ph = prediction[0]
    
    x1, y1, x2, y2 = yolo_to_voc(px*width, py*height, pw*width, ph*height)

    return [x1, y1, x2, y2]

# Detect the License Plate text
def detect_text(img, ocr_language, coords):
    
    x1, y1, x2, y2 = coords
    
    ocr_reader = ocr.Reader(ocr_language)
    
    raw_licenseplate = img[y1:y2, x1:x2]
    
    licenseplate = cv2.threshold(cv2.cvtColor(raw_licenseplate, cv2.COLOR_BGR2GRAY), 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    
    possible_text = ocr_reader.readtext(licenseplate)
    
    result = ''
    confidence = 0
    
    for detection in possible_text:
        if detection[2] > confidence:
            result = detection[1]
            confidence = detection[2]

    return result, confidence
    
# Create Image
def plot_plate(img, coords, text, confidence):
    x1, y1, x2, y2 = coords
    
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.rectangle(img, (x1, y1), (x2, y2), (0,255,0),2)
    img = cv2.rectangle(img, (x1, y1-30), (x2, y1), (0,255,0), -1)
    
    confidence = int(confidence * 100)
    img = cv2.putText(img, f"{text} {confidence}%", (x1+8, y1-8), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 2)

    return img
    
# Main Function   
def get_licenseplate_data(img):
    
    try:
        image = np.array(Image.open(io.BytesIO(img)))
        
        model = tf.keras.models.load_model('scripts/plate_detection_model.h5')
        
        coords = find_license_plate(image, model)
        
        text, confidence = detect_text(image, ['en'], coords)
        
        final_image = plot_plate(image, coords, text, confidence)
        
        _, encodded = cv2.imencode('.jpg', final_image)
        
        return encodded.tobytes()
    
    except:
        
        return -1
    

          
      
    
    
    