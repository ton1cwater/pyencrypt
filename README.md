# pyencrypt
Simple encryption tool written in python :)

## Usage
```pyencrypt [action] [file1] [file2]```

Flags: 

```-k [name of .key file (no extension)]``` generate key

```-e [file to encrypt] [.key file]``` encrypt file

```-d [file to decrypt] [.key file]``` decrypt file

## Install
Make sure you have Python ```>=v3.11``` and ```pipx``` installed.
Installing [pipx](https://pipx.pypa.io/stable/#install-pipx) is highly recommended.
If you have pipx, run ```pipx install git+https://github.com/ton1cwater/pyencrypt/``` then ```pipx inject pyencrypt cryptography```

Now you can type ```pyencrypt``` in the terminal to run.

### Without pipx:
Download project and cd into directory.

On all machines: ```python3 -m venv .venv```

Windows:

```.venv/Scripts/activate```

```pip install -r requirements.txt```

```python -m pyencrypt.py```

Mac/Linux:

```source .venv/bin/activate```

``` pip install -r requirements.txt```

```python -m pyencrypt.py```
