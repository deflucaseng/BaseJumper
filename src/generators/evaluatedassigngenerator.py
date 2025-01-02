def evaluatedassignnodegenerator(var, lhs, op, rhs):
    dictcode = {
        "plus": f'\
        mov eax, {lhs}\n\
        mov ebx, {rhs}\n\
        add eax, ebx\n\
        mov dword [{var}], eax\n',
            
        "minus": f'\
        mov eax, {lhs}\n\
        mov ebx, {rhs}\n\
        sub eax, ebx\n\
        mov dword [{var}], eax\n',

        "divided": f'\
        xor edx, edx\n\
        mov eax, {lhs}\n\
        mov ebx, {rhs}\n\
        div ebx\n\
        mov dword [{var}], eax\n',

        "times":f'\
        mov eax, {lhs}\n\
        mov ebx, {rhs}\n\
        mul ebx\n\
        mov dword [{var}], eax\n',

        "equals":f'\
        mov eax, {lhs}\n\
        mov ebx, {rhs}\n\
        cmp eax, ebx\n\
        setz cl\n\
        movzx ecx, cl\n\
        mov dword [{var}], ecx\n',

        "!equals":f'\
        mov eax, {lhs}\n\
        mov ebx, {rhs}\n\
        cmp eax, ebx\n\
        setz cl\n\
        xor cl, 1\n\
        movzx ecx, cl\n\
        mov dword [{var}], ecx\n',

        "and":f'\
        mov eax, {lhs}\n\
        mov ebx, {rhs}\n\
        and eax, ebx\n\
        mov dword [{var}], eax\n',

        "or":f'\
        mov eax, {lhs}\n\
        mov ebx, {rhs}\n\
        or eax, ebx\n\
        mov dword [{var}], eax\n',

        "xor":f'\
        mov eax, {lhs}\n\
        mov ebx, {rhs}\n\
        xor eax, ebx\n\
        mov dword [{var}], eax\n',

        "nand":f'\
        mov eax, {lhs}\n\
        mov ebx, {rhs}\n\
        and eax, ebx\n\
        not eax\n\
        mov dword [{var}], eax\n',

        "xnor": f'\
        mov eax, {lhs}\n\
        mov ebx, {rhs}\n\
        xor eax, ebx\n\
        not eax\n\
        mov dword [{var}], eax\n',

        "nor":f'\
        mov eax, {lhs}\n\
        mov ebx, {rhs}\n\
        or eax, ebx\n\
        not eax\n\
        mov dword [{var}], eax\n',
    }
    return dictcode[op]