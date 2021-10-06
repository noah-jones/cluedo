![logo](https://github.com/noah-jones/cluedo/raw/master/logo.jpg?raw=true)

# Cluedo Top Secret Passcodes

You need to print out your passwords because you can never remember them? Be smart and use this tool to make them totally safe to print out.

An adversary can never read your secret passcodes because it's only possible if you have a red magnifying glass, like in the board game Cluedo.

## Dependencies

* python3
* `svgwrite>=1.4.1`
* red looking glass


## Usage

### Encrypt your secret code visually and save it to a file

    cluedo "your secret code here" > encrypted.svg

or 

    cluedo "your secret code here" -o encrypted.svg

### Encrypt your secret code visually and write it to stdout

    cluedo "your secret code here"

### Encrypt your secret code visually and place it within a circle

    cluedo "your secret code here" -c 

or 

    cluedo "your secret code here" --circle

### Get a drawing object in Python

```python
from cluedo import get_encrypted_secret

dwg = get_encrypted_secret("your secret code here")
```

