# Installation

It is recommended to install the dependencies manually, requirements.txt doesn't seem to work consistenly. For EasyOCR you may need to install PyTorch separately, you might need a command from their [installation guide](https://pytorch.org/get-started/locally/).

General installation steps:
- Download the repository with `git clone https://github.com/Gabmelom/plate-vision.git`
- (Optional but recommended) In the root directory of the project, create a virtual environment with `python -m venv env` 
- Activate the environment for the current shell with `env/Scripts/activate`  
- Install the requirements with `pip install --force-reinstall tensorflow=="2.9.1" easyocr opencv-python matplotlib fastapi`
- [Download](https://cmailcarletonca-my.sharepoint.com/:u:/g/personal/gabrielmelomartins_cmail_carleton_ca/EQOqvuylHr5PrvktS3n37KQBdzGV6u-D5g7-3iLPkO9egw?e=cmzi8x) the model from the drive and copy it to the root folder of the project
- Start the server by navigating to the `app` folder and running `main.py` script. E.g `python3 main.py`
- Have fun!