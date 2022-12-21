section .data
msg db 'Hello, World!',0

section .text
global _start

_start:
  mov eax, 4 ; system call for write
  mov ebx, 1 ; file descriptor for stdout
  mov ecx, msg ; address of the message
  mov edx, 14 ; length of the message
  int 0x80 ; invoke system call

  mov eax, 1 ; system call for exit
  xor ebx, ebx ; exit code 0
  int 0x80 ; invoke system call

nasm -f elf hello.asm
ld -o hello hello.o
