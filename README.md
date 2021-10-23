# Hex
Quick command to translate from hex to str and str to hex.

# Installation

- Get the project : `~$ git clone https://github.com/Ectario/hex.git`

- Add aliases if wanted :

Cd in home `~$ cd ~` and then depending of if you use zsh or bash `~$ nano .zshrc` or `~$ nano .bashrc` 

Then creating aliases: 

`alias hex="python3 /home/USERNAME/.../hex/hex.py"`

`alias hexd="python3 /home/USERNAME/.../hex/hex.py -d"`

Activate aliases:

`~$ source .bashrc` or `~$ source .zshrc`

# Usage
- hex.py -d to decode the hexadecimal

  `~$ python3 hex.py -d < textInHexa.txt`
        
  `~$ echo "7475746f0a" | python3 hex.py -d`
        
- hex.py to encode in hexadecimal 

  `~$ python3 hex.py < textInASCII.txt`
 
  `~$ echo "tuto" | python3 hex.py`

###   ↓ *If you have aliases* ↓

- hex -d to decode the hexadecimal

  `~$ hexd < textInHexa.txt`
        
  `~$ echo "7475746f0a" | hexd`
        
- hex to encode in hexadecimal 

  `~$ hex < textInASCII.txt`
 
  `~$ echo "tuto" | hex`
