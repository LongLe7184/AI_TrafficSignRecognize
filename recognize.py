import numpy as np
import sys
import tensorflow as tf
from PIL import Image
import tkinter as tk
from tkinter import filedialog

IMG_WIDTH = 30
IMG_HEIGHT = 30

classes = {1: 'Speed limit (20km/h)',
           2: 'Speed limit (30km/h)',
           3: 'Speed limit (50km/h)',
           4: 'Speed limit (60km/h)',
           5: 'Speed limit (70km/h)',
           6: 'Speed limit (80km/h)',
           7: 'End of speed limit (80km/h)',
           8: 'Speed limit (100km/h)',
           9: 'Speed limit (120km/h)',
           10: 'No passing',
           11: 'No passing veh over 3.5 tons',
           12: 'Right-of-way at intersection',
           13: 'Priority road',
           14: 'Yield',
           15: 'Stop',
           16: 'No vehicles',
           17: 'Veh > 3.5 tons prohibited',
           18: 'No entry',
           19: 'General caution',
           20: 'Dangerous curve left',
           21: 'Dangerous curve right',
           22: 'Double curve',
           23: 'Bumpy road',
           24: 'Slippery road',
           25: 'Road narrows on the right',
           26: 'Road work',
           27: 'Traffic signals',
           28: 'Pedestrians',
           29: 'Children crossing',
           30: 'Bicycles crossing',
           31: 'Beware of ice/snow',
           32: 'Wild animals crossing',
           33: 'End speed + passing limits',
           34: 'Turn right ahead',
           35: 'Turn left ahead',
           36: 'Ahead only',
           37: 'Go straight or right',
           38: 'Go straight or left',
           39: 'Keep right',
           40: 'Keep left',
           41: 'Roundabout mandatory',
           42: 'End of no passing',
           43: 'End no passing veh > 3.5 tons'}

def select_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.png")])
    if file_path:
        print(f"Selected image path: {file_path}")
        return file_path
        # Now you can process the image using the selected path.
        # Add your image processing code here.

def process_image(image_path):
	try:
		model = tf.keras.models.load_model(sys.argv[1])
		image = Image.open(image_path)
		image.show()  # Display the cropped image
		img_resize = image.resize((30, 30))
		img_exdim = np.expand_dims(img_resize, axis=0)
		img_arr = np.array(img_exdim)
		print(img_arr.shape)
		pred = model.predict(img_arr).argmax()
		sign = classes[pred + 1]
		print(sign)
	except Exception as e:
		print(f"Error processing image: {e}")
		

root = tk.Tk()
root.withdraw()  # Hide the main window
# Call the function with the selected image path
selected_image_path = select_image()
process_image(selected_image_path)

# Check command-line arguments
if len(sys.argv) != 2:
    sys.exit("Usage: python recognition.py [model.h5]")
