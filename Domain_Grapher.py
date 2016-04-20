#!/usr/bin/env python3

# Header
print ('==============================')
print ('=       Domain Grapher       =')
print ('= -------------------------- =')
print ('=                version 0.1 =')

# Menu
print ('==============================')
print ('=                            =')
print ('=  1. Start Crawl            =')
print ('=  2. Drop Tables            =')
print ('=  0. Exit                   =')
print ('=                            =')
print ('==============================')

item = input('Choose between [0-2]: ')

if item == '1':
    print('Starting Crawl...')
elif item == '2':
    print('Dropping all tables...')
elif item == '0':
    print('Exiting...')
else:
    print('Invalid input.')
