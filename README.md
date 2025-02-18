# End-to-end-Machine-Learning-Project-with-Mlflow


## WorkFlows

1. update config.yaml
2. update schema.yaml
3. update params.yaml
4. update entity
5. update the configuration manager insrc config
6. update the components
7. update the pipelines
8. update the main.py
9. update the app.py



# How to run ? 

### STEPS

Clone the repository


***bash

https://github.com/WisdomAnalyst/End-to-end-Machine-Learning-Project-with-Mlflow
...

### STEP 01- Create a conda environment after opening the repository

***bash
conda create -n mlproj python=3.8 -y
***


***bash
conda activate mlproj
***

### STEP 2 - install the requirements 
***bash
pip install -r requirements.txt
***


***bash
#finally run the following command 
python app.py


now, 
***bash
open up your local host and port


#MLflow
[Documentation](https://mlflow.org/docs/latest/index.html)



#### cmd
-mlflow ui



### dagshub
[dagshub](https;//dagshub.com/)


MLFLOW_TRACKING_USERNAME=WisdomAnalyst
MLFLOW_TRACKING_PASSWORD=781aa8b98086477f57088d72da8f137a4686f662
MLFLOW_TRACKING_URI=https://dagshub.com/WisdomAnalyst/End-to-end-Machine-Learning-Project-with-Mlflow.mlflow
python script.py


Run this to export as env variables 

***bash

export MLFLOW_TRACKING_URI=https://dagshub.com/WisdomAnalyst/End-to-end-Machine-Learning-Project-with-Mlflow.mlflow

export MLFLOW_TRACKING_USERNAME=WisdomAnalyst

export MLFLOW_TRACKING_PASSWORD=781aa8b98086477f57088d72da8f137a4686f662