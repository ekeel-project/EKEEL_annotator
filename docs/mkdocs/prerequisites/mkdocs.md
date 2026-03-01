# Mkdocs
-------

The EKEEL project is documented with [mkdocs](https://www.mkdocs.org/getting-started/)

Its update is fully automated with every code modification, as long as classes and functions are documented in the [numpydoc](https://numpydoc.readthedocs.io/en/latest/format.html) format.

To modify and view the live-updated content locally:

1. Clone the repos starting from working directory inside `docs` folder

    This configuration allows to manage every project independently:
    ```bash
    cd ../
    git clone https://github.com/ekeel-project/annotator.git
    git clone https://github.com/ekeel-project/augmentator.git
    ```
    And will create the following structure:
    ```
    {workspace root}
    │
    ├── annotator
    │   └── (annotator project folders and files)
    │   
    ├── augmentator
    |   └── (augmentator project folders and files)
    │
    └── docs
        └── (docs project folders and files)
    ```

    It is suggested to use the first configuration in VSCode because it allows to manage all the three source control repos in the same environment (updates in the code can be seen immediately in the documentation) 

    Otherwise there is the project structure alternative:
    ```bash
    mkdir apps
    cd apps
    git clone https://github.com/ekeel-project/annotator.git
    git clone https://github.com/ekeel-project/augmentator.git
    ```
    This will create the following structure where both annotator and augmentator will be ignored to be pushed in the docs repo via gitignore:
    ```
    docs
    ├── apps
    │   ├── annotator
    │   │   └── (annotator project folders and files)
    │   └── augmentator
    │       └── (augmentator project folders and files)
    └── (docs project folders and files)
    ```

2. Install the packages from the ```requirements.txt``` file located in the ```mkdocs``` directory in a new environment:
    ```bash
    pip install -r mkdocs/requirements.txt
    mkdocs serve
    ``` 

3. Open your browser and navigate to `http://127.0.0.1:8000/docs/` to view the documentation.

    !!! warning
        Use a different environment from ```ekeel_anno_env``` and ```ekeel_aug_env``` (the two environments of the project) to avoid mixing packages and create possible conflicts

    !!! warning
        The branch `gh-pages` is used for the deployment of the website. Be careful not to use this branch.