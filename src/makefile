.PHONY: all clean rebuild
rebuild:
	rm -rf test.asm
	rm -rf test.o
	python3 main.py test.eng
	nasm -f elf64 -o test.o test.asm
	echo ".o file created successfully"
	ld test.o -o test
	echo "executable created successfully"
	./test	

all:
	python3 main.py test.eng
	nasm -f elf32 -o test.o test.asm
	echo ".o file created successfully"

clean:
	rm -rf test.asm
	rm -rf test.o
