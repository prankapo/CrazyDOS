void boot() {
	char message[13] = "Hello, world\n";
	boot_print(message, 13);
}

void boot_print(char *string, int len) {
	for (int i = 0; i < len; ++i) {
		if (string[i] != '\n') {
			__asm__(
				".intel_syntax noprefix;"
				".code16;"
				"mov al, %0;"
				"mov ah, 0x0e;"
				"int 0x10;"
				:: "m"(string[i])
				: "ax"
			);
		}
		else {
			__asm__(
				".intel_syntax noprefix;"
				".code16;"
				"mov al, 0x0a;"
				"mov ah, 0x0e;"
				"int 0x10;"
				"mov al, 0x0d;"
				"int 0x10;"
				::
				: "ax"
			);
		}
	}
}