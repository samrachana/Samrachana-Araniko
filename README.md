### Content <!-- omit in toc -->

- [Introduction](#introduction)
- [Installation](#installation)
- [Getting Started](#getting-started)
- [For Developers](#for-developers)
- [Frequently Asked Questions](#frequently-asked-questions)

---

### Introduction

Samrachana is a free and open source structural analysis software based on Direct Stiffness Method. It is ideal for analysing 2D beams, frames and trusses.

The current version `version 0.x` is named after ancient Nepali architect Araniko. The version `0.1` is `pre-release` and thus is susceptible to bugs and issues.

> Learn more about the [versioning system we follow](https://link-to-docs-versioning).

> If you find a bug or an issue, post it in the [discussion forum]()

---

### Installation

1. ##### Windows

   > Although you can install Samrachana as an executable application, we don't recommend that when the version is labelled `pre-release`. Please wait until the label changes to `beta` or `stable`.

   To install Samrachana on Windows, you can download installer from [here](https://link-to-installer) and simply run it. After the installation is completed, you can launch Samrachana just like you launch any other software.

2. ##### MacOS, Linux or other OS [^1]

   [^1]: Installers for these systems will be available soon.

   At the moment, no installer is available for operration systems other than windows. So, the only option is to [build from source](#build-from-source).

3. ##### Build from source [^2]

   [^2]: If you want to contribute, please refer [For Developers](#for-developers) section.

   If you just want to try out Samrachana, or want to contribute to this repository, the best way to install it is to build from scratch. There are a few options available. Choose the one that suits you!

---

### Getting Started

Samrachana is made keeping users interested in function rather than interface of the application in mind. So, the learning curve of interface is as straight as possible. You can start by playing around with different functions on a simply supported beam. A video demonstrating how you can get your feet wet with Samrachana can be found [here](https://link-to-video).

For detail documentation of all the features available, refer to the docs [here](https://link-to-docs).

---

### For Developers

If you are interested in contributing to this repository and make Samrachana a better software, you can start by reading the [CONTRIBUTING markdown file](./CONTRIBUTING.md).

Note that, Samrachana is entirely written in `python` and requires python to be installed in your system. Currently, we are working with `python3.8.5`. For the sake of compatibility, please install the same version.

Other dependencies can be installed in virtual environment. The required packages are listed in [requirements text file](src/requirements.txt).

---

### Frequently Asked Questions

> Before asking questions in discussion forum, please make sure that your question is not already answered by this file.

1. Is Samrachana free to use?

   Samrachana is and always will be open source and free. You can not only use the software for free, but also download and modify the source code too. For details regarding what you can and can't do with the software and the source code, please read the [LICENSE file](LICENSE).

2. How can I install Samrachana in my phone?

   Samrachana is a desktop application and can't be installed in other devices. (Or at least, it is not intended to be.)

3. Can I work with 3D structures in Samrachana?

   Unfortunately, you can't work with 3D structures currently. However, we are working to develop a 3D version of the software too.

4. Can Samrachana perform Finite Element Analysis?

   In general, no. Samrachana is entirely designed for students just getting familiar with structural analysis. So, it only supports one dimensional line elements. (Although, curves are supported, they are broken down into small lines behind the scenes.) One can argue that, FEA can be performed to some extent using the software, but we will develop a separate version for that. So, stay tuned.

5. Can I submit my assignments using Samrachana?

   Note that, the software comes with absolutely no warranty or liability. If your professor and institution has no problem with using the software to complete your assingments, that is completely fine with us. However, you can always use it to check your answers!
