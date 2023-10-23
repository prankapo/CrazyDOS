#!/usr/bin/python3
import os
import sys

'''
Usage: builddisk -i <Name of the image file> -m <Size of the disk> -o <Name of the disk>
'''
try:
	i = sys.argv.index('-i')
	image = sys.argv[i + 1]
except:
	print('Specify image file using -i')
	exit(1)
try:
	i = sys.argv.index('-m')
	memory = sys.argv[i + 1]
except:
	print('Specify the size of the disk you want using -m')
	exit(1)
try:
	i = sys.argv.index('-o')
	disk = sys.argv[i + 1]
except:
	print('Specify the name of the disk to be written using -o')
	exit(1)

size = float(memory[0:len(memory) - 1])
if memory[-1] == 'k':
	size = int(size * 1024)
	print(f'Size of disk: {size} kiB')
elif memory[-1] == 'M':
	size = int(size * 1024 * 1024)
	print(f'Size of disk: {size} MiB')
elif memory[-1] == 'G':
	size = int(size * 1024 * 1024 * 1024)
	print(f'Size of disk: {size} GiB')
else:
	print(f'Unknown unit {memory[-1]} in {memory}')

with open(image, 'rb') as imagefp:
	buffer = bytearray(imagefp.read())
size_delta = size - len(buffer)
print(f'{size_delta} bytes need to be written to get the virtual disk...')
with open(disk, 'wb') as diskfp:
	diskfp.write(buffer)
	buffer = bytearray([0x00 for i in range(size_delta)])
	diskfp.write(buffer)
print('Done.')