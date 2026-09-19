# ZX-DDoS

**ZX-DDoS** is a Python-based **DDoS Tool** for educational and testing purposes only.

> **DISCLAIMER:**  
> This repository is strictly for educational, research, and network testing purposes only.  
> **The author is not responsible for any misuse or illegal activities.**

Repository: [https://github.com/MrGoofyDev/ZX-DDoS](https://github.com/MrGoofyDev/ZX-DDoS)

---

## Table of Contents

- [Description](#description)
- [Screenshot](#screenshot)
- [Main File](#main-file)
- [Installation](#installation)
    - [Termux](#termux)
    - [Debian-based GNU/Linux](#debian-based-gnulinux)
    - [Windows](#windows)
    - [MacOS](#macos)
- [Usage](#usage)
- [Mandatory Inputs](#mandatory-inputs)
- [Requirements](#requirements)
- [Disclaimer](#disclaimer)

---

## Description

**ZX-DDoS** is a Distributed Denial of Service (DDoS) tool, written in Python, to help understand the mechanics of network stress testing and security evaluation.  
**Use only in controlled and legal environments.**

---

## Screenshot

![Screenshot](https://raw.githubusercontent.com/MrGoofyDev/ZX-DDoS/refs/heads/main/File/Screenshot.png)


---

## Main File

- The main entry point for this tool is: **`start.py`**

---

## Installation

### Prerequisites

- `Python 3.6+`
- `pip` (Python package manager)

### 1. Clone the Repository

```sh
git clone https://github.com/MrGoofyDev/ZX-DDoS
cd ZX-DDoS
```

### 2. Install Requirements

All dependencies are listed in `requirements.txt`.

```sh
pip install -r requirements.txt
```

---

## Step-by-Step Usage Instructions

### Termux

```sh
pkg update && pkg upgrade
pkg install git python
git clone https://github.com/MrGoofyDev/ZX-DDoS
cd ZX-DDoS
pip install -r requirements.txt
python3 start.py
```

### Debian-based GNU/Linux

```sh
sudo apt update && sudo apt upgrade
sudo apt install git python3 python3-pip
git clone https://github.com/MrGoofyDev/ZX-DDoS
cd ZX-DDoS
pip3 install -r requirements.txt
python3 start.py
```

### Windows

1. Download & install [Python](https://www.python.org/downloads/).
2. Open `cmd` or PowerShell and run:
    ```sh
    git clone https://github.com/MrGoofyDev/ZX-DDoS
    cd ZX-DDoS
    pip install -r requirements.txt
    python start.py
    ```

### MacOS

```sh
brew install git python3
git clone https://github.com/MrGoofyDev/ZX-DDoS
cd ZX-DDoS
pip3 install -r requirements.txt
python3 start.py
```

---

## Usage

After installation, run the main file:

```sh
python3 start.py
```
or (on Windows):

```sh
python start.py
```

Follow the interactive prompts to configure your test.

---

## Mandatory Inputs

When running `start.py`, you will be **required** to enter the following (no optional fields):

- Target IP or URL / Domain    
- Number of workers (parallel threads)  
- Number of requests  


---

## Requirements

- **Supported Operating Systems:**
    - Linux
    - Termux (Android)
    - Windows
    - MacOS

- **Python 3 required**

---

## Disclaimer

> **For Educational Purposes Only!**
>
> ZX-DDoS is designed for security researchers, network administrators, and students to understand DDoS methodologies in a safe, controlled environment.
>
> **Do NOT use against networks, servers, or websites without explicit authorization. The author will not be held responsible for any misuse or damage caused by this tool.**

---
