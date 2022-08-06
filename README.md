# <p align="center">Data Mining Projects</p>

# Table of Contents
- [Introduction](https://github.com/mohammadtavakoli78/Data-Mining#introduction)
- [First_Project](https://github.com/mohammadtavakoli78/Data-Mining#-First_Project)
- [Second_Project](https://github.com/mohammadtavakoli78/Data-Mining#-Second_Project)
- [Third_Project](https://github.com/mohammadtavakoli78/Data-Mining#-Third_Project)
- [Fourth_Project](https://github.com/mohammadtavakoli78/Data-Mining#-Fourth_Project)
- [Technologies](https://github.com/mohammadtavakoli78/Data-Mining#technologies)

## Introduction
This repository contains projects of Data Mining Course. There are four projects.<br>
> 1.  first project, is about ```preprocessing``` that we use ```pandas``` and ```Scikit-learn``` for this purpose. The dataset we use is ```iris-dataset```.<br><br>
> 2.  second project, is about creating a ```Neural Network``` and we train the model for two datasets: ```make_circles``` and ```fashion_mnist```.<br><br>
> 3.  third project, is about ```Association Rules``` and also ```Clustering```, There are two different projects.<br><br>
> 4.  and final project, we train a model with a dataset which has more than 70k records and we should decide whether a person has a special disease or not, for this project we use ```XGBoost``` that is a ```decision tree```.

## 💻 First_Project
This project is about ```preprocessing``` that we use ```pandas``` and ```Scikit-learn``` for this purpose. The dataset we use is ```iris-dataset``` which can be downloaded by this [link](https://github.com/mohammadtavakoli78/Data-Mining/blob/master/Project%201/iris.data). i do the following steps for preprocessing ```iris-dataset```.<br>
> 1.  handle ```missing values``` and find NaN values and fill them with proper values or remove them.
> 2.  convert categorical features to numerical features by ```Label Encoding``` and ```One Hot Encoding```.
> 3.  nomalize data frame by the help of ```Standard Scalar```.
> 4.  dimension reduction with ```PCA```.
> 5.  ```visualization```.<br>

The visualization of the final result is:<br>

<img src="https://github.com/mohammadtavakoli78/Data-Mining/blob/master/Project%201/images/9.PNG" width="400px" height="300px" display="block" /><br>
you can access to project and code by this [link](https://github.com/mohammadtavakoli78/Data-Mining/tree/master/Project%201).

## 💻 Second_Project
This project is about creating a ```Neural Network``` and we train the model for two datasets: ```make_circles``` and ```fashion_mnist```.<br><br>
for first dataset (```make_circles```) i follow these steps:
> 1.  make 1000 circles.
> 2.  split train and test dataset.
> 3.  create a ```Neural Network``` with two hidden layers.
> 4.  train model.
> 5.  plot loss and accuracy.<br>

for acctivation functions i used ```relu``` for hidden layers and ```sigmoid``` for the output layer and ```binary_crossentropy``` for loss function.<br>
You can access to code of this section by this [link](https://github.com/mohammadtavakoli78/Data-Mining/blob/master/Project%202/DM_HW2_1.ipynb).<br><br>

for second dataset (```fashion_mnist```) i follow these steps:
> 1.  load dataset.
> 2.  split train and test dataset.
> 3.  create a ```Convolutional Neural Network``` with two hidden layers.
> 4.  train model.
> 5.  plot loss and accuracy.
> 6.  ```print confusion_matrix``` and ```classification_report```.<br>

for acctivation functions i used ```relu``` for hidden layers and ```softmax``` for the output layer and ```categorical_crossentropy``` for loss function and ```adam``` for optimizer.<br>
You can access to code of this section by this [link](https://github.com/mohammadtavakoli78/Data-Mining/blob/master/Project%202/DM_HW2_2.ipynb).<br><br>

## 💻 Third_Project
. [Codes are in this link](https://github.com/mohammadtavakoli78/Data-Mining/tree/master/Project%203).

## 💻 Fourth_Project
. [Codes are in this link](https://github.com/mohammadtavakoli78/Data-Mining/tree/master/Project%204).

## Technologies
Project is created with:
* Python version: 3.8

