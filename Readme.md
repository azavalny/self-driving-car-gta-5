![](car1.gif)

Inspiration:
https://github.com/Sentdex/pygta5

Model:
https://arxiv.org/pdf/1512.03385.pdf

Installation:
* Clone this repository
* In the main directory, run ```pip install -r requirements.txt``` to get all the necessary libraries. I recommend doing this in a virtual environment to avoid versioning issues with your python packages
* ![Download the training data](https://www.kaggle.com/datasets/thelazyaz/gta-5-self-driving-car-balanced-data)

Training Data Game Settings:
* Window size should be 1280x720 but I rescale the images down to 640x480 to reduce memory
* Game time set to 12pm in clear weather
* Black Sedan (Michael's in game personal car)


Future Work:
* Obviously more data is needed to improve the accuracy of the model. Millions more examples would be a good start, and then use federated learning to train it on the cloud.
* Data Augmentation can be used (Tensorflow has one for Images, but requires likely at least 64 GB RAM otherwise the notebook will crash) to add additional examples of underrepresented driving controls. This makes sense, because you (hopefully) drive a car forwards more often than you drive it backwards. 
* Instead of using the entire raw image, the minimap on the bottom left of the screen could be utilized for steering properly since it dosen't include irrelevant background information.
* Using more modalities as inputs such as the car's current velocity, angular acceleration, and maybe including multiple camera views on the same car like Tesla does. They specifically convert their multiple cameras into a ![vector space](https://www.youtube.com/watch?v=j0z4FweCy4M) where the the objects around the car are features.

![](car2.gif)