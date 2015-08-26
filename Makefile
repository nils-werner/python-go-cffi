.PHONY: all clean

all: c/main py/_sum.py go/sum
clean:
	rm go/*.h
	rm go/*.so
	rm c/*.so
	rm c/main
	rm py/_*.py

go/sum: go/sum.go
	go build -o go/sum go/sum.go

go/sum.so: go/sum.go
	# Compile Go code to C shared object
	go build -buildmode=c-shared -o go/sum.so go/sum.go

go/sum.h: go/sum.so
	true

c/main: c/main.c go/sum.so go/sum.h
	# Copy SO to C directory so we can link against it
	cp go/sum.so c/
	# Compile C stub that imports shared object
	gcc -Wall -o c/main c/main.c c/sum.so

py/_sum.py: py/build_sum.py go/sum.so go/sum.h
	# Compile Python stub using CFFI
	python py/build_sum.py
