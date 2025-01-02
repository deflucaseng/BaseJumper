section .data
		true_msg db 'true', 0xA
		true_len equ $ - true_msg
		false_msg db 'false', 0xA
		false_len equ $ - false_msg
		newline db 10
section .text
		global _start
	
_start:
command1:
		mov dword [lastknownpos], command2
		mov eax, 0
		mov dword [var1], eax
command2:
		mov dword [lastknownpos], command3
		mov eax, 2
		mov dword [var2], eax
command3:
		mov dword [lastknownpos], command4
        mov eax, [var1]
        mov ebx, 1
        add eax, ebx
        mov dword [var1], eax
command4:
		mov dword [lastknownpos], command5
		mov eax, [var1]
		mov dword [num_to_print], eax
		jmp start_num_print
command5:
		mov dword [lastknownpos], command6
        mov eax, [var2]
        mov ebx, 2
        mul ebx
        mov dword [var2], eax
command6:
		mov dword [lastknownpos], command7
        mov eax, [var1]
        mov ebx, 5
        cmp eax, ebx
        setz cl
        movzx ecx, cl
        mov dword [var3], ecx
command7:
		mov dword [lastknownpos], command8
		mov eax, [var3]
		cmp eax, 1
		jne command3
command8:
		mov dword [lastknownpos], command9
		mov eax, [var2]
		mov dword [num_to_print], eax
		jmp start_num_print
command9:
		mov eax, 0x1
		mov ebx, 0
		int 0x80

print_true:
		mov ecx, true_msg
		mov edx, true_len
		jmp do_print
print_false:
		mov ecx, false_msg
		mov edx, false_len
do_print:
		mov eax, 4
		mov ebx, 1
		int 0x80
		jmp print_newline
start_num_print:
		mov ecx, buffer
		add ecx, 11
		mov byte [ecx], 0
		dec ecx
		mov ebx, 10
	
convert_loop:
		xor edx, edx
		div ebx
		add dl, '0'
		mov [ecx], dl
		dec ecx
		test eax, eax
		jnz convert_loop
		mov eax, [num_to_print]
		test eax, eax
		jns print_number
		mov byte [ecx], '-'
		dec ecx
print_number:
		mov edx, buffer
		add edx, 11
		sub edx, ecx
		inc ecx
		mov eax, 4
		mov ebx, 1
		int 0x80
		jmp print_newline
print_newline:
		mov eax, 4
		mov ebx, 1
		mov ecx, newline
		mov edx, 1
		int 0x80
		jmp [lastknownpos]
section .bss
		num_to_print resd 1
		lastknownpos resd 1
		buffer resb 12
		var1 resd 1
		var2 resd 1
		var3 resd 1
	