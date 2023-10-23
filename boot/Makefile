CC16 := gcc -std=c99 -masm=intel -m16 -ffreestanding -nostdlib
CC32 := gcc -std=c99 -masm=intel -m32 -ffreestanding
CC := gcc -std=c99 -masm=intel -m32 -ffreestanding

build: boot.c boot.ld
	@echo "Building the binary of the bootloader"
	$(CC16) -c -O2 boot.c -o boot.o
	ld -m elf_i386 -Tboot.ld boot.o -o boot.elf
	objcopy -O binary boot.elf boot.bin
	@echo "\nBinary file made. Taking a hexdump and disassembling"
	hexdump -Cv boot.bin > boot.hex.log
	objdump -D -Mintel,i386 -b binary -m i386 boot.bin > boot.s.log

clean:
	@echo "Cleaning boot directory..."
	-rm *.s *.o *.elf *.bin *.img *.log
	@echo "Done."