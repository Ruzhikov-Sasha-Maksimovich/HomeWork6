from os.path import exists
from First import creating
from Second import writing_scv
from Second import writing_txt


path = 'Phonebook.csv'
valid = exists(path)
if not valid:
    creating()

writing_scv()
writing_txt()