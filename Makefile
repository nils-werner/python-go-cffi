.PHONY: all

all: c/main py/_sum.py

go/sum.so: go/sum.go
	# Compile Go code to C shared object
	go build -buildmode=c-shared -o go/sum.so go/sum.go

go/sum.h: go/sum.so
	true

c/main: c/main.c go/sum.so
	# Compile C stub that imports shared object
	gcc -Wall -o c/main c/main.c go/sum.so

py/_sum.py: go/sum.so go/sum.h
	# Compile Python stub using CFFI
	python py/build_sum.py
