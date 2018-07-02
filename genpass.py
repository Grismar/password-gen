import os
import time
import random
import pyperclip
import urllib.request

filename = 'google-10000-english-usa-no-swears-medium.txt'

# download 10000 most common words, minus swears from github, if not in current directory
if not os.path.isfile(filename):
    url = 'https://raw.githubusercontent.com/first20hours/google-10000-english/master/'+filename
    response = urllib.request.urlopen(url)
    with open(filename, 'w') as f:
        f.write(response.read().decode('utf-8'))

# generate password
with open ('google-10000-english-usa-no-swears-medium.txt', 'r') as f:
    words = f.read().splitlines()
    parts = [words[random.randint(0, len(words)-1)] for _ in range(0,4)]
    pwd = '-'.join([part if random.randint(0,1) == 0 else part.upper() for part in parts])

# put it on the clipboard for 12 seconds, or until interrupted
pyperclip.copy(pwd)
print('Password on clipboard for 12 seconds (Ctrl-C to stop now)...')
try:
    time.sleep(12)
except KeyboardInterrupt:
    pass
pyperclip.copy('')
print('Password removed, done.')
