
%macro abc 2
	mov eax,%1
	mov ebx,%2
	add eax,ebx
%endmacro
%macro pqr 2
	mov eax,%1
	mov ebx,%2
	sub eax,ebx
%endmacro
section .data
	a dd 4
	b dd 5
section .bss
	c resd 1
section .text
	global main
	extern printf
	extern scanf
main:
	mov eax,dword[a]
	mov ebx,dword[b]
	add eax,ebx
	mov dword[c],4
	mov eax,3
	push eax
	call printf
	call scanf
	add esp,4
	
