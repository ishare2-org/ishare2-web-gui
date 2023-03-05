# iShare2 GUI

iShare2 GUI is a web interface for the iShare2 project, designed to provide a graphical user experience for managing and downloading bin, QEMU, Dynamips, and Docker images for network emulators. It leverages the capabilities of the [iShare2 CLI](https://github.com/pnetlabrepo/ishare2), executing its commands under the hood to simplify image management for network administrators.

## Table of Contents

- [Features](#features)
- [Screenshots](#screenshots)
- [Docker container (Experimental)](#docker-container-experimental)
  - [Build Docker image](#build-docker-image)
  - [Load image](#load-image)
  - [Run Docker](#run-docker)
  - [Run Docker (Detached mode)](#run-docker-detached-mode)

## Features

- Manage bin, QEMU, Dynamips, and Docker images
- Download bin, QEMU, Dynamips, and Docker images
- Frontend for iShare2 CLI

## Screenshots

![alt iShare2-GUI's Homepage](web_app/src/static/images/Homepage%20-%20ishare2.png)

The iShare2 GUI is currently under development and may not be stable yet. It has only been tested on PNetLab, but it may be adaptable to work on other network emulators.

The iShare2 GUI is designed to make it easy for you to manage your network emulation environment by providing a simple, intuitive interface. You can use the "Manage" dropdown in the navbar to access different management options, such as managing your bin images, QEMU images, Dynamips images, or Docker images. Additionally, the "Download" option in the sub-menu gives you access to the different image types that you can download.

The iShare2 GUI has a clear and modern look and feel, with a logo and favicon representing the tool, and a user-friendly interface that makes it easy to navigate. You can find more information about the project on the [iShare2-GUI](https://github.com/ishare2-org/iShare2-gui) GitHub page, or reach out to the support team on [Telegram](https://t.me/unetlab_cloud).

So if you're looking for a tool that can help you manage and download the images you need for your network emulation environment, consider checking out iShare2 GUI!

Other useful chats tho not directly associated:
[PNetLab Group Chat](https://t.me/pnetlab)

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
