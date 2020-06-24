# Visualize-Neural-Networks

My attempt at mixing my web dev knowledge with Machine Learning. Created a Neural Network Visualizer using [streamlit](https://www.streamlit.io/) :heart_eyes: and [Flask](https://pypi.org/project/Flask/)

Trained a simple model with three layers on MNIST dataset and created an endpoint using Flask which first chosen a random image from MNIST dataset and runs the trained model against the choosed image and outputs the value of each neuron and the chosen image.

Used Streamlit to consume this API and display this data in an easy to understand and clean, usable frontend.


## Exploring file in the project
`The files which have not been listed were used while deploying the project to Heroku and aren't of any importance while running the server locally`
### Backend
 - build_model
	- [Train_MNIST_model.ipynb](\backend\build_model\Train_MNIST_model.ipynb): Used to train MNIST model and generate model.h5
 - [app.py](\backend\app.py): Contains the core logic of server and script which runs the model to generate output
 - [requirements.txt](\backend\requirements.txt): Contains all the PyPi packages need to run this server

### Frontend:
 - [app.py](\frontend\app.py): Contains the core logic of frontend written using streamlit
 - [requirements.txt](\frontend\requirements.txt): Contains all the PyPi packages need to run this server



## Steps to run the project locally

> Make sure you have at least 2-3 GB of free RAM available because you will have to run two servers (Flask and streamlit) locally  

Its a very simple procedure to run the project locally, It is just a matter of 5-6 lines of commands. It may take more time depending on your internet connection and if you already have the requirements or not (especially tensorflow :stuck_out_tongue_winking_eye:)

### Download the project using git clone

```
git clone https://github.com/jai-dewani/Visualize-Neural-Networks.git
cd Visualize-Neural-Networks
```

`Open two terminals as you will have to keep two server up and running`
### Running Flask Server
```
cd backend
pip install requirements.txt
pyython app.py
```

### Running Streamlit Server
Get the url in which your flask server is running like ```localhost:3000``` or something.  
Replace this value with the current placeholder URL in [app.py](\frontend\app.py) in the frontend folder
```
pip install requirements.txt
streamlit run app.py
```