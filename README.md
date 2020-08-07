# Number-Plate-Detection
Number Plate Detection carried out with help of YOLO

The project was execute in follwoing steps :
* Creating a custom dataset.
* Labelling the dataset.
* Training the YOLO V3 Model in Darknet framework.
* testing the trained YOLO V3 model in OpenCV framework.

# Creating the Dataset
For creating the dataset, a total of 1077 car images from different angles were downloaded. It was ensured that there is no bias in the data towards a specific angle image of cars. Cars of different manufacturers, colours and sizes were taken for this data, to maintain versatility of the dataset. [Here](https://drive.google.com/drive/folders/1kkp7mTdD5HDUvXAohoynXPKSFzUc5axh?usp=sharing) is the link to the Dataset.

<img src="images/cb13.jpeg" alt="car back" width="220"/> <img src="images/cbs1.jpeg" alt="car back side" width="220"/> <img src="images/cf71.jpeg" alt="car front" width="220"/> <img src="images/cfs44.jpeg" alt="car front side" width="220"/> 

# Labelling the dataset 
For labelling the image, we use **LabelImg** software. It provides an extremely easy interface for creating annotations in Yolo format.  

<img src="images/labelimg_empty.png" alt="label img" width="460"/> <img src="images/labelimg.png" alt="label img c" width="460"/>
<p align="center"> LabelImg interface to make annotations </p>

The Labels will be saved as *.txt* files in YOLO format. These *.txt* files have to be saved in the same folder that has all the images. 

<p align="center">
<img src="images/yolo_format.JPG" alt="yolo format" width="460"/></p>
<p align="center">
YOLO format </p>

# Training the YOLO V3 Model in Darknet framework.
For training the data, GPU service provided by Google Colab was used. Following were the steps executed to set up training environment and train the model:
* Open a new Notebook in google colab and Mount the drive in it. 
* Clone the official darknet github repository in our notebook environment.
* Make necessary edits in darknet folder to give GPU the necessary access and configure for later use in OpenCV.
* Creating a *.cfg* file for training our custom dataset.
* Various file (like *obj.names*, *obj.data*, etc) are created.
* Images are extracted in obj folder and the names are saved in *train.txt*.
* The Network is trained. 

We trained our model till 3000 iterations. [*Train_YoloV3_car.ipynb*](https://github.com/mohit138/Number-Plate-Detection/blob/master/Car_number_plate/Train_YoloV3_car.ipynb) is the the Training Notebook and [here](https://drive.google.com/drive/folders/1kkp7mTdD5HDUvXAohoynXPKSFzUc5axh?usp=sharing) is the link to Trained Weights.

# Testing the Model 
The Trained Model is tested in OpenCV framework. [*yolo_car_number_plate_detection.py*](https://github.com/mohit138/Number-Plate-Detection/blob/master/Car_number_plate/yolo_car_number_plate_detection.py) script is used to apply the model on given images and extract out the Number Plate from the image. Following are the results obtained:

<img src="images/plate_1.JPG" alt="plate1" width="306"/> <img src="images/car_1.JPG" alt="car 1" width="614"/>  
<img src="images/car1.JPG" alt="car 1" width="614"/> <img src="images/np1.JPG" alt="plate1" width="306"/>
<img src="images/np2.JPG" alt="plate1" width="306"/> <img src="images/car2.JPG" alt="car 1" width="614"/> 
<img src="images/car3.JPG" alt="car 1" width="614"/> <img src="images/np_3.JPG" alt="plate1" width="306"/>

