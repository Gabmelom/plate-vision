
# README
This file contain all information required for running the License Plate Detector as part of the COMP 4102 class. We have included two separate testing methods. 

<b>Included Files</b>
- app folder
	- contains all required document for running the fastapi application
	- main.py: python file for running fastapi application
- local_run.py: python file for running manual application
- plate_vision.ipynb: Jupyter notebook containing our entire workflow. This includes everything from data processing to model training and model predicting. <b>This notebook is set to read-me as many functions will throw errors due to the missing dataset </b>
- examples folder: 
	- contains a series of images for testing purpose.
- report.pdf: our final report
- demo video


<b>Running Instructions</b>
It is recommended to install the dependencies manually, requirements.txt doesn't seem to work consistenly. For EasyOCR you may need to install PyTorch separately, you might need a command from their [installation guide](https://pytorch.org/get-started/locally/).

General installation steps:
- (Optional but recommended) In the root directory of the project, create a virtual environment:
```
python -m venv env
```
- Activate the environment for the current shell:
```
env/Scripts/activate
```
- Install the requirements:
```
pip install --force-reinstall tensorflow=="2.9.1" easyocr opencv-python matplotlib fastapi uvicorn
```
- <b>IMPORTANT </b> [Download](https://cmailcarletonca-my.sharepoint.com/:u:/g/personal/gabrielmelomartins_cmail_carleton_ca/EQOqvuylHr5PrvktS3n37KQBdzGV6u-D5g7-3iLPkO9egw?e=cmzi8x) the model from the drive and copy it <b>INTO THE APP FOLDER. </b> If the model is not loaded, then both methods will throw out an error. Due to the model's size, we did not include it into our submission.
- Running the application
	- <b>Method 1 [Faster]</b>: Website
		- Navigate to the app folder. Run the python file main.py with the command: ``` python3 main.py ```
		- This will open a link in terminal. Follow it and it will lead you to the running website

	- <b>Method 2 [Slower but Easier] </b>: Local file
		- In the root directory is the file local_run.py
		- This python file requires one argument, which is a path to the image you wish to input into the program
		- The program can be run with: ``` python3 local_run.py filepath```

<b> Final Note </b>: Per request, we can provide our entire dataset and/or training and processing files
