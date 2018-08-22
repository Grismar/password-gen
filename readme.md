# Generate password

General purpose password generator. Uses a 10,000 most common English words dictionary to generate a password consisting of a number of words, in a combination of all lower case, all upper case, separated by some character.

For example, with:
```python
separator = '-'
nparts = 4
```

a generated password might be `sleep-WORD-closet-HAND`. A password will always at least contains one word in upper case and one in lower case.

## Usage 

Install pyperclip:
```
pip install pyperclip
```
or
```
pip install -r requirements.txt
```

Run script:
```
python genpass.py
```
