# Lips Reading
This is the repository for the project of the course Vision and Cognitive System of the master degree in Computer Science at the University of Padova.

What fallows is the assignment of our project:

"*The aim of this project is to predict words or phrases from videos.
This task can be solved with both machine learning and deep learning techniques (for example, you can use a CNN to extract features from video frames and process extracted features with an RNN).
Pre-trained CNNs on human faces could improve classification results.
Data augmentation techniques should be applied to increase the number of samples.*"

We used the __[MIRACL-VC1](https://sites.google.com/site/achrafbenhamadou/-datasets/miracl-vc1)__ dataset, and to solve the main problem we relied on the __[Keras](https://keras.io/)__ library.

## Installation
In order to install the project, you need to clone the repo usign the command
```
git clone https://github.com/davidebassan/project-vcs
```

## Usage
Make sure to have an enviroment alredy setup (i.e. dowloand the datset form the official website and extract it), then install the dependecies from the `requirments.txt` file
```
pip install -r requirments.txt
```

Once you have done, you can run the notebook `Lips-Reading.ipynb` which contains all the code used for the project.

## Authors
- Baldo Massimiliano ([massimiliano.baldo@studenti.unipd.it](mailto:massimiliano.baldo@studenti.unipd.it))
- Bassan Davide ([mailto:davide.bassan.1@studenti.unipd.it](mailto:davide.bassan.1@studenti.unipd.it))
- Panighel Cristiano ([mailto:cristiano.panighel@studenti.unipd.it](mailto:cristiano.panighel@studenti.unipd.it))