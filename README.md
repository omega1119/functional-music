# Functional Music App Setup Guide

This guide explains how to set up your Python environment for the Functional Music App using Conda.

---

## Prerequisites

Ensure you have the following installed:

- [Conda (Miniconda or Anaconda)](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html)

---

## Step-by-Step Setup

### 1. Clone the Repository

```bash
git clone https://github.com/omega1119/functional-music
cd functional-music
```

### 2. Create and Activate the Conda Environment

Create a new Conda environment named `functional_music` with Python 3.11 (or your preferred version):

```bash
conda create -n functional_music python=3.11 -y
conda activate functional_music
```

### 3. Install Dependencies

Ensure your project includes a `requirements.txt`. You can generate one using:

```bash
pip freeze > requirements.txt
```

Then install dependencies:

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

---

## Managing Your Environment

### Activate Environment

```bash
conda activate functional_music
```

### Deactivate Environment

```bash
conda deactivate
```

### Update Dependencies

When adding new dependencies:

```bash
pip install <new-package>
pip freeze > requirements.txt
```

### Delete Environment

```bash
conda remove -n functional_music --all
```

---

## Running Your App

Example command to run your Python app:

```bash
python app.py
```

Replace `app.py` with the entry point of your application.

---

## Helpful Commands

Check installed packages:

```bash
conda list
```

Export environment (Conda format):

```bash
conda env export > environment.yml
```

---

You're all set! Enjoy building your Functional Music App.