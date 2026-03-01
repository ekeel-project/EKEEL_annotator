# Install Annotation tool
------------

The document provides instructions for setting up the EKEEL Video Annotation project locally on your PC.  


## First Installation

### Prerequisites: ffmpeg

Open a Terminal and type:
```bash
sudo apt update && sudo apt upgrade
sudo apt install ffmpeg
sudo apt install tesseract-ocr
sudo apt install libtesseract-dev
```

---
### Install environment
---


"cd" to the folder annotator/code

    > cd {path to the folder annotator/code}


conda create the python environment from a yml file
```bash
conda env create -f conda_environment.yml
```

(Facoltative) If you have a gpu, to improve performances:
```bash
conda install m2w64-toolchain
conda install libpython
```

<br>

-----
## On any Change in Environment Packages 

To avoid inconsistency between local and server, yml file has been used to enforce same environment state

open a terminal:

    > cd {inside folder annotator/code}


overwrite the conda_environment.yml inside using
```
conda env export --no-builds | grep -v "^prefix: " | grep -v "en-core-web-lg" | grep -v "it-core-news-lg" > conda_environment.yml
```
and push the modifications to the repo. (The spacy models end up in the final distribution but must be ignored otherwise cause errors)

Then to synchronize the packages change in the server pull updates from the repo and on the server terminal update dependencies on the server:

The guide is [here](deploy.md#update-and-setup-video-annotation-app)



------
## Run locally

(Facoltative) Open VSCode with conda (if dev using VScode ide)
```bash
code .
```


After the installation is completed, launch the project with:
```bash
conda activate ekeel_anno_env
python main.py
```


------
## Notes
    
- Email 

    After some months the email sender could stop working and you can find errors on register or forgot password:

    * Login to the google account with this app credentials   
    (you can find those credentials on file .env) 
    
    * go to security settings -> allow less secure app

    * (More info -> https://support.google.com/accounts/answer/6010255?hl=en)

    If still not working:

    * after log in with the google account open this link:  
      https://accounts.google.com/DisplayUnlockCaptcha

    * (More info -> https://stackoverflow.com/questions/16512592/login-credentials-not-working-with-gmail-smtp)