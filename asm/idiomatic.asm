default rel
global _start

section .rodata
    fizz db "Fizz"
    buzz db "Buzz"
    newline db 10

section .bss
    digits resb 3

section .text
_start:
    mov r12d, 1
    mov r13d, 3
    mov r14d, 5
.loop:
    xor r15d, r15d
    dec r13d
    jnz .check_buzz
    mov r13d, 3
    lea rsi, [fizz]
    mov edx, 4
    call write
    inc r15d
.check_buzz:
    dec r14d
    jnz .check_number
    mov r14d, 5
    lea rsi, [buzz]
    mov edx, 4
    call write
    inc r15d
.check_number:
    test r15d, r15d
    jnz .end_line
    mov eax, r12d
    mov ebx, 10
    lea rsi, [digits + 3]
    xor ecx, ecx
.digit:
    xor edx, edx
    div ebx
    add dl, '0'
    dec rsi
    mov [rsi], dl
    inc ecx
    test eax, eax
    jnz .digit
    mov edx, ecx
    call write
.end_line:
    lea rsi, [newline]
    mov edx, 1
    call write
    inc r12d
    cmp r12d, 100
    jle .loop
    mov eax, 60
    xor edi, edi
    syscall

write:
    mov eax, 1
    mov edi, 1
    syscall
    ret

section .note.GNU-stack noalloc noexec nowrite progbits
