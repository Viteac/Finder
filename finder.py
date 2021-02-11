import os

founded = []

def just_dir(dirname,text):
    m = os.listdir(dirname)
    print(m)
    for file in m:
        if os.path.isfile(f'{dirname}{file}'):
            with open(f'{dirname}{file}', encoding='utf-8', errors='ignore') as f:
                read = f.read()
                if text in read:
                    founded.append(f'{dirname}{file}')

def subdirectory(dirname,text):
    for root, dirs, files in os.walk(dirname):
        for name in files:
            with open(os.path.join(root, name), encoding='utf-8', errors='ignore') as f:
                read = f.read()
            if text in read:
                founded.append(f'{root}{name}')
def checkdir():
    dirname: str = input('Enter the file name \n >> ')
    if not dirname.endswith('/'):
        dirname = f'{dirname}/'
    if os.path.isdir(dirname) is True:
        return dirname

dirname = checkdir()

text = input('Enter the text to find\n>>')

which = input('Do You want to check subfolders Y/N? ').lower()
if which in 'y,n':
    if which == 'y':
        subdirectory(dirname,text)
    else:
        just_dir(dirname,text)

s = len(founded)

if s > 0:
    if s == 1:
        what = 'file'
    else:
        what = 'files'
    print(f'Found {s} {what} with: {text}:')
    for i in founded:
        print(i)
