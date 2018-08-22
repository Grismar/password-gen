import os
import time
import random
import pyperclip
import urllib.request

# name of file read (or generated) for a dictionary
filename = 'google-10000-english-usa-no-swears-medium.txt'
# for how low to leave the password on the clipboard, when sharing
delay = 15
# how many words to use in the password
nparts = 4
# what to separate the words with
separator = '-'
# whether to show the password in the script output (on screen)
show = False
# whether to share the password on the clipboard for {delay} seconds
share = True

assert nparts > 0
assert delay >= 0

# download 10000 most common words, minus swears from github, if not in current directory
if not os.path.isfile(filename):
    url = 'https://raw.githubusercontent.com/first20hours/google-10000-english/master/'+filename
    response = urllib.request.urlopen(url)
    with open(filename, 'w') as f:
        f.write(response.read().decode('utf-8'))

# generate password
with open(filename, 'r') as f:
    words = f.read().splitlines()
    parts = [words[random.randint(0, len(words)-1)] for _ in range(0, nparts)]
    caps = [random.randint(0, 1) for p in parts]
    # if all capitalisation are the same, flip a random one
    if all([c == caps[0] for c in caps]):
        caps[random.randint(0, nparts)] = (caps[0] + 1) % 2
    pwd = separator.join([part if cap == 0 else part.upper() for part, cap in zip(parts, caps)])

if show:
    print(f'Password: {pwd}')

if share:
    # put it on the clipboard for 12 seconds, or until interrupted
    pyperclip.copy(pwd)
    print(f'Password on clipboard for {delay} seconds (Ctrl-C to stop now)...')
    try:
        time.sleep(delay)
    except KeyboardInterrupt:
        pass
    pyperclip.copy('')
    print('Password removed, done.')
