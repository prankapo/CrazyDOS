#!/usr/bin/python3
import os
import sys

'''
Usage: buildflat -b <binary of the bootloader> -s <system binary> -o <name of the output file>
'''
try:
	i = sys.argv.index('-b')
	bootloader = sys.argv[i + 1]
except:
	print('Specify binary of the bootloader using -b')
	exit(1)
try:
	i = sys.argv.index('-s')
	system = sys.argv[i + 1]
except:
	print('Specify binary of the system using -s')
	exit(1)
try:
	i = sys.argv.index('-o')
	img = sys.argv[i + 1]
except:
	print('Specify the name of the output file using -o')
	exit(1)

buffer = None
image = None
print(f'Reading binary of the bootloader...')
with open(bootloader, 'rb') as bootbinfp:
	buffer = bootbinfp.read()
print(f'Done.')
image = bytearray(buffer)
print(f'Date read is of type: {type(image)}')
size_delta = 512 - len(image)
print(f'Size of binary of the bootloader {size_delta}')
print(f'Generating sector...')
for block in range(size_delta):
	image.append(0x90)
print(f'Done.')
print(f'Including magic numbers...')
image[510] = 0x55
image[511] = 0xaa
print(f'Final size of bootsector: {len(image)}\n')

print(f'Reading binary of the system...')
with open(system, 'rb') as systembinfp:
	buffer = bytearray(systembinfp.read())
print(f'Done.')
print(f'Appending to the image...')
for i in range(len(buffer)):
	image.append(buffer[i])
print(f'Final size of the image: {len(image)}\n')

print(f'Writing to CrazyOS.img...')
with open(img, 'wb') as imgfp:
	imgfp.write(image)
print(f'Done.')