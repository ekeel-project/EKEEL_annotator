# Quickstart

To streamline the process of cloning and configuring the EKEEL repository, Visual Studio Code or PyCharm is highly suggested.

The following guide is for VS Code

The project has been tested to work on Ubuntu 22 and 24.  

It does not work on Windows for libraries compatibility issues, but only on Linux distributions or [WSL](https://learn.microsoft.com/en-us/windows/wsl/about).


---
## Prerequisites
---

### **Step 1: Install VS Code**
If you don't already have VS Code installed, download and install it from [here](https://code.visualstudio.com/).

---
### **Step 2: Clone the Repositories via VS Code**
Based on the project you are working on, clone one or both of the repositories, since they are independent.

1. Create a folder named `apps` at the same level as `docs`.
2. Clone the `annotator` repository:
    - Enter the repository URL: `https://github.com/ekeel-project/annotator.git`
    - Choose the `apps` directory as the local directory.
    - VS Code will clone the repository and prompt you to open the cloned folder. Click **Open**.
3. Clone the `augmentator` repository:
    - Enter the repository URL: `https://github.com/ekeel-project/augmentator.git`
    - Choose the `apps` directory as the local directory.
    - VS Code will clone the repository and prompt you to open the cloned folder. Click **Open**.

---
### **Step 3: Paste `secrets.env`**
- Ask the project manager for the `secrets.env` file and place the file in the directory `annotator/code` and in `augmentator/src/flask-server`


---
### **Step 4: Download Miniconda Installer**
```bash
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh
```

#### Installation Prompts
1. Press `Enter` to view license
2. Type `yes` to accept the license
3. Press `Enter` to confirm installation location
4. Type `yes` to initialize Miniconda3

#### Activate and Verify the Installation
```bash
source ~/.bashrc
conda --version
```

#### Clean Up Installer
```bash
rm Miniconda3-latest-Linux-x86_64.sh
```

**Note:** Restart your terminal or run `source ~/.bashrc` after installation.

---
## Annotator

To run Annotator follow [this guide](../annotator/install)

---
## Augmentator

To run Augmentator follow [this guide](../augmentator/install)