section .data
    hello db 'Hello, World!',0 ; null-terminated string

section .text
    global _start

_start:
    ; write string to stdout
    mov eax, 4 ; system call for sys_write
    mov ebx, 1 ; file descriptor for stdout
    mov ecx, hello ; address of string to write
    mov edx, 13 ; length of string to write
    int 0x80 ; call kernel

    ; exit program
    mov eax, 1 ; system call for sys_exit
    xor ebx, ebx ; exit status = 0
    int 0x80 ; call kernel
