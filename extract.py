import os
import pandas as pd
import csv

file_names = os.listdir('./data')


def check_file(file, loc='./process/previous_files.txt'):
    with open(loc) as f:
        lines = f.readlines()
    for line in lines:
        if line[:-1] == file:
            return False
    return True


def write_txt(name, file='./process/previous_files.txt'):
    with open(file, 'a') as f:
        f.write(name)
        f.write('\n')


def read_csv(file_name):
    data = pd.read_csv(f'./data/{file_name}')
    return data


def progress():
    for file_name in file_names:
        if check_file(file=file_name):
            #write_txt(file_name)
            return read_csv(file_name)
