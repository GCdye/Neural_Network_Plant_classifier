# Neural_Network_Plant_classifier
## Executive Summary
### Problem statement
"Is it possible to help new South African farmers increase their yield by proactively pruning away the weeds that grow kill crops?"
Using a neural network I was able to solve this problem with 85% accuracy! Using a seven layer Convolutional Neural Net I was able to deploy an application that can take in a full directory of images and make predictions quickly and efficiently while telling the user the location of weeds in the crop feild.
### Outside research and data gathering
This project was loosely based on a kaggle dataset uploaded by Pretoria University in South Africa. According to their research team crop yeilds can be reduced anywhere from 20-100% in a single season due to weeds, Either by competition and allelopathy. The university had a collection of around 5500 images of the eleven most common weed plants along with 260 maize seedling all in various stages of developement up to six weeks. Since a neural net is prone to overfitting I decided to use the keras method for data manipulation. During each epoch of training the Neural Net keras will randomly flip, brighten translate, or zoom on the image to give a new set of images everytime. This helps prevent the NN from being overfit while simultaneously protecting against the random placement of the target plant by the end-user. 
### Target Audience
The target audience is mainly for South African farmers with little to no experience. In bussiness, The first three years are the most important and hardest to survive. This can help new farmers get an inexspensive leg up against a large threat to crop yeild and increase profit margins in their most vulnerable years. 
### The model specifics
For this project Convolutional Neural Networks or CNNs are uniquely suited to handle image processing and excel at image classification. Due to limited time and computational power, my model is simple consisting of only seven layers with a max node count of 64. Pretoria University provided the base sample images 5500 over 12 classes. ranging from about 150 images per class to the max being 700 images. This gives the model baseline score of about 13%. To increase the data I used the keras method of DATAGEN to give new train data for all 20 epochs. The method randomly flips, brightens, translates, or alters the image thus effectively turning my sample data from 5500 to 110,000 images. This method alone greatly helped to reduce the chance of my network getting overfit, While simultaneously protecting from bad end-user input. 
### The model road map
optimizer used was Adam with a custom learning rate reducing the standard rate by an order of magnitude.
#### Layer one
A 32 node Convolutional 2D input layer.
#### Layer two
MAXPooling layer.
#### Layer three
A 64 node Convolutional 2D layer
#### Layer four
MAXPooling layer 
#### Layer five
Flattening layer
#### Layer six
32 node Fully conected layer
#### Layer seven
12 node fully connected output layer. softmax regularization
## How to use this program
The pictures to be predicted need to be .png format numbered sequentially starting at 1.
Two files from this program are specifically needed to run the model and get predictions. Simply download the final_model file along with predictions.py and make sure they are in the same directory. Then in that directory in terminal:
$python predict.py
You will be asked how many pictures followed by the directory to which the files are stored. 
### Example run
$python predictions.py
"Loading model..."
"Model Loaded!"
"How many pictures are you predicting?"
$ 5
"And What is the filepath?(start with a ./)"
$./crops/

"This is most likely a weed plant, Pluck it!
1
This is most likely a Maize/Corn plant, Do not pluck it!
2
This is most likely a Maize/Corn plant, Do not pluck it!
3
This is most likely a Maize/Corn plant, Do not pluck it!
4
This is most likely a Maize/Corn plant, Do not pluck it!
5 
Weed locations are at: [1],  1 total weed found! "
~program ends~
### example files
1.png
2.png
3.png

## Future developments
Ideally my endplan was to have this running on a server based out of flask, due to my time contraints I was only able to have a terminal ready product. First update will be a more user friendly design, ready for deployment. 
I would also like to remove constraints on file type as most smart phones save images on .jpg format. 
Last would be a language support for more languages in South Africa, such as Afrikaans. 
