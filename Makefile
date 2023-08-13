build: src/main.c src/hello_world.o src/hello_world.h
	mkdir -p bin
	gcc -o bin/hello_world src/hello_world.o src/main.c
