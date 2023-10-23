CC16 := gcc -std=c99 -masm=intel -m16 -ffreestanding -nostdlib
CC32 := gcc -std=c99 -masm=intel -m32 -ffreestanding
CC := gcc -std=c99 -masm=intel -m32 -ffreestanding

# Build disks and everything else
build: build-disk
	@echo "\nBuilding done."

# For building disk
build-disk: build-img tools/builddisk
	@echo "\nBuilding the disk"
	tools/builddisk -m 2.8M -i CrazyDOS.img -o disk1.img

# For building a minimum image containing the bootloader and the OS
build-img: build-bootloader build-system build-tools
	@echo "\nBuilding a system image"
	tools/buildflat -b boot/boot.bin -s system.bin -o CrazyDOS.img
	@echo "\nTaking a hexdump and disassembling"
	hexdump -Cv CrazyDOS.img > CrazyDOSimg.hex.log
	objdump -D -Mintel,i386 -b binary -m i386 CrazyDOS.img > CrazyDOSimg.s.log

# Build bootloader
build-bootloader:
	(cd boot; make build;)

# Build the system
build-system:
	@echo "Building the binary of the operating system"
	touch system.bin

# Build tools
build-tools: tools/buildflat.py tools/builddisk.py
	(cd tools; cp buildflat.py buildflat; sudo chmod +x buildflat)
	(cd tools; cp builddisk.py builddisk; sudo chmod +x builddisk)

# For running the computer
qemu-on:
	@echo "Launching qemu"
	qemu-system-i386 -m 16M -k en-us -rtc base=localtime\
		-device sb16\
		-device adlib\
		-device cirrus-vga\
		-soundhw pcspk\
		-fda disk1.img -boot order=a

# Clean stuff up!
clean: 
	@echo "Cleaning root directory..."
	-rm *.s *.o *.elf *.bin *.img *.log
	@echo "Done."
	(cd boot; make clean)