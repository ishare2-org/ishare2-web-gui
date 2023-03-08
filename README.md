# ishare2 GUI

ishare2 GUI is a web interface for the ishare2 project, designed to provide a graphical user experience for managing and downloading bin, QEMU, Dynamips, and Docker images for network emulators. It leverages the capabilities of the [ishare2 CLI](https://github.com/pnetlabrepo/ishare2), executing its commands under the hood to simplify image management for network administrators.

## Table of Contents

- [Features](#features)
- [Screenshots](#screenshots)
- [Install from ishare2 (Coming soon)](#install-from-ishare2-coming-soon)
- [Installation (as root)](#installation-as-root)
  - [Prerequisites](#prerequisites)
  - [Change to root user](#change-to-root-user)
  - [Clone the repository](#clone-the-repository)
  - [Create a virtual environment](#create-a-virtual-environment)
  - [Install dependencies](#install-dependencies)
  - [Run the application](#run-the-application)
  - [Run the application uvicorn](#run-the-application-uvicorn)
- [Docker container (Experimental)](#docker-container-experimental)
  - [Build Docker image](#build-docker-image)
  - [Load image](#load-image)
  - [Run Docker](#run-docker)
  - [Run Docker (Detached mode)](#run-docker-detached-mode)

## Features

- Manage bin, QEMU, Dynamips, and Docker images
- Download bin, QEMU, Dynamips, and Docker images
- Frontend for ishare2 CLI

## Screenshots

![alt ishare2-GUI's Homepage](web_app/src/static/images/Homepage%20-%20ishare2.png)

The ishare2 GUI is currently under development and may not be stable yet. It has only been tested on PNetLab, but it may be adaptable to work on other network emulators.

The ishare2 GUI is designed to make it easy for you to manage your network emulation environment by providing a simple, intuitive interface. You can use the "Manage" dropdown in the navbar to access different management options, such as managing your bin images, QEMU images, Dynamips images, or Docker images. Additionally, the "Download" option in the sub-menu gives you access to the different image types that you can download.

The ishare2 GUI has a clear and modern look and feel, with a logo and favicon representing the tool, and a user-friendly interface that makes it easy to navigate. You can find more information about the project on the [ishare2-GUI](https://github.com/ishare2-org/ishare2-gui) GitHub page, or reach out to the support team on [Telegram](https://t.me/unetlab_cloud).

So if you're looking for a tool that can help you manage and download the images you need for your network emulation environment, consider checking out ishare2 GUI!

Other useful chats tho not directly associated:
[PNetLab Group Chat](https://t.me/pnetlab)

## Install from ishare2 (Coming soon)

```bash
placeholder
```

## Installation (as root)

ishare2 GUI needs to be run as root, as it needs to access the /opt/unetlab directory to manage the images.
You can install ishare2 GUI on your system following these steps:

### Prerequisites

- Python 3.8 or higher
- pip
- virtualenv

```bash
sudo apt-get install python3 python3-pip python3-venv -y
```

### Change to root user

```bash
sudo su
```

### Clone the repository

Choose a directory where you want to clone the repository, and then clone it. It is recommended to clone the repository in the /opt/ishare2/gui/ directory. However, you can clone it anywhere you want inside the root's home directory.
You can clone the repository using the following command:

```bash
git clone https://github.com/ishare2-org/ishare2-web-gui.git /opt/ishare2/gui/
cd /opt/ishare2/gui/
```

### Create a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the application

```bash
python3 main.py
```

The application will be available at <http://localhost:5000>

### Run the application uvicorn

```bash
uvicorn main:app --reload
```

The application will be available at <http://localhost:8000>

## Docker container (Experimental)

### Build Docker image

```bash
git clone https://github.com/ishare2-org/ishare2-web-gui.git
cd ishare2-web-gui
sudo docker build
docker build - < Dockerfile
```

### Load image

```bash
sudo docker load -i /path/to/ishare2.tar
```

### Run Docker

```bash
sudo docker run -p 5000:5000 -v /opt/unetlab:/opt/unetlab -it ishare
```

### Run Docker (Detached mode)

```bash
sudo docker run -d -p 5000:5000 -v /opt/unetlab:/opt/unetlab -it ishare
```
