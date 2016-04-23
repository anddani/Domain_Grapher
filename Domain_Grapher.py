#!/usr/bin/env python3

# Header
print ('==============================')
print ('=       Domain Grapher       =')
print ('= -------------------------- =')
print ('=                version 0.1 =')

# Menu
print ('==============================')
print ('=                            =')
print ('=  1. Enter Domain           =')
print ('=  2. Start Crawl            =')
print ('=  3. Drop Tables            =')
print ('=  0. Exit                   =')
print ('=                            =')
print ('==============================')

item = input('Choose between [0-2]: ')

if item == '1':
    print('Enter Domain...')
elif item == '2':
    print('Starting Crawl...')
elif item == '3':
    print('Dropping all tables...')
elif item == '0':
    print('Exiting...')
else:
    print('Invalid input.')
