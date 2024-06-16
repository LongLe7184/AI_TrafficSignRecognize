# AI_TrafficSignRecognize
Introduction to AI's Project: Using Python to build a neural network for classification image-based traffic signs.

**Description:**
- Training a neural network using Tensorflow, build a model file base on the **gtsrb** (_German Traffic Sign Recognition Benchmark_) database.
- Processing input images using OpenCV, give prediction about the meaning of the traffic sign that contain in the processed image.

**How to use:**
- Run trafficsign.py to create a model file base on gtsrb folder. (powershell syntax: "python trafficsign.py data_directory [model.h5]")
  + data_directory: direction to the gtsrb folder.
  + [model.h5]: name of the output model file.
- Use the model file has been created, run recognize.py and input image to predict the meaning of the traffic sign that has contain in the picture. (powershell syntax: "python regcognize.py [model.h5]")
  + [model.h5]: name of the model file has been created before.
