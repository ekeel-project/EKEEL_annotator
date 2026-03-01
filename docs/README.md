# EKEEL Documentation

Welcome to the EKEEL Annotator documentation. This repository uses [MkDocs](https://www.mkdocs.org/) to generate and host the documentation for the EKEEL project.

The documentation is available at the [ekeel-project/docs](https://ekeel-project.github.io/docs/) website

## Overview


EKEEL (Empowering Knowledge Extraction to Empower Learners) is a research project funded by the Italian Ministry of University and Research (MUR) under the PRIN 2022 PNRR programme, a nationally managed programme supported through the European Union – Next Generation EU.


The EKEEL_annotator repository hosts the code and official documentation of the EKEEL Annotator, which supports the annotation of video lectures, identifying concepts and prerequisite relations, their semantic representation according to the EKEEL data model, and the export of a JSON-LD file.
The documentation includes setup guides, deployment instructions, and technical references to the project components and codebase.

The documentation refreshes every Monday at 4 AM and updates the website content.


## Documentation

The documentation is organized using MkDocs with the Material theme. The documentation includes:

- **Quickstart Guides**: Instructions to quickly set up and deploy the services.
- **Codebase Documentation**: Detailed documentation of the codebase, generated using mkdocstrings.
- **Deployment Guides**: Step-by-step guides to deploy the services locally and remotely.

## Getting Started

The documentation deployment has been tested on Ubuntu 24 but should work with small adaptations on [WSL](https://learn.microsoft.com/en-us/windows/wsl/about)

To build and serve the documentation locally, follow these steps:

1. Clone this repository:
    ```bash
    git clone https://github.com/ekeel-project/ekeel.git
    cd ekeel
    ```

2. Clone the EKEEL_annotator repository:
    ```bash
    mkdir -p apps
    git clone https://github.com/ekeel-project/EKEEL_annotator.git apps/EKEEL_annotator
    ```

3. Install the required dependencies:
    ```bash
    pip install -r mkdocs/requirements.txt
    ```

4. Build and serve the documentation:
    ```bash
    mkdocs serve
    ```

5. Open your browser and navigate to `http://127.0.0.1:8000/docs/` to view the documentation.

# WARNING 

The branch `gh-pages` is used for the deployment of the website. Be careful not to overwrite this branch.

## Contributing

We welcome contributions to improve the documentation. If you find any issues or have suggestions, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
