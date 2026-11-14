default rel
global main
extern puts
extern snprintf

section .rodata
    fizzbuzz_text db "FizzBuzz", 0
    fizz_text db "Fizz", 0
    buzz_text db "Buzz", 0
    number_format db "%d", 0

section .bss
    number resb 12

section .text
fizzbuzz:
    push rbx
    mov ebx, edi
    mov eax, ebx
    xor edx, edx
    mov ecx, 15
    div ecx
    lea rax, [fizzbuzz_text]
    test edx, edx
    jz .done
    mov eax, ebx
    xor edx, edx
    mov ecx, 3
    div ecx
    lea rax, [fizz_text]
    test edx, edx
    jz .done
    mov eax, ebx
    xor edx, edx
    mov ecx, 5
    div ecx
    lea rax, [buzz_text]
    test edx, edx
    jz .done
    lea rdi, [number]
    mov esi, 12
    lea rdx, [number_format]
    mov ecx, ebx
    xor eax, eax
    call snprintf wrt ..plt
    lea rax, [number]
.done:
    pop rbx
    ret

main:
    push r12
    mov r12d, 1
.loop:
    mov edi, r12d
    call fizzbuzz
    mov rdi, rax
    call puts wrt ..plt
    inc r12d
    cmp r12d, 100
    jle .loop
    xor eax, eax
    pop r12
    ret

section .note.GNU-stack noalloc noexec nowrite progbits
