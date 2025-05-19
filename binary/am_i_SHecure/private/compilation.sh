#!/bin/sh

gcc -Wall -Wextra -ansi -pedantic -Wuninitialized flag_generator.c -o flag_maker -lssl -lcrypto
gcc -Wall -Wextra -ansi -pedantic -Wuninitialized SHecure.c -o SHecure -lssl -lcrypto
