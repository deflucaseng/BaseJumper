def evaluatedassignnodegenerator(stackloc, lhs, op, rhs):
    dictcode = {
        "plus": "mov eax, [esp + {}]\
            \n\tadd eax, [esp + {}]\
        	\n\tmov [esp + {}], eax",
            
        "minus": "mov eax, [esp + {}]\
            \n\tsub eax, [esp + {}]\
            \n\tmov [esp + {}], eax",

        "divided": "mov eax, [esp + {}]\
            \n\tmov edx, 0\
            \n\tdiv dword [esp + {}]\
            \n\tmov [esp + {}], eax",

        "times": "mov eax, [esp + {}]\
            \n\tmul dword [esp + {}]\
            \n\tmov [esp + {}], eax",

        "equals": "mov eax, [esp + {}]\
            \n\tcmp eax, [esp + {}]\
            \n\tsete al\
            \n\tmovzx eax, al\
            \n\tmov [esp + {}], eax",

        "!equals": "mov eax, [esp + {}]\
            \n\tcmp eax, [esp + {}]\
            \n\tsetne al\
            \n\tmovzx eax, al\
            \n\tmov [esp + {}], eax",

        "and": "mov eax, [esp + {}]\
            \n\tand eax, [esp + {}]\
            \n\tmov [esp + {}], eax",

        "or": "mov eax, [esp + {}]\
            \n\tor eax, [esp + {}]\
            \n\tmov [esp + {}], eax",

        "xor": "mov eax, [esp + {}]\
            \n\txor eax, [esp + {}]\
            \n\tmov [esp + {}], eax",

        "nand": "mov eax, [esp + {}]\
            \n\tand eax, [esp + {}]\
            \n\tnot eax\
            \n\tmov [esp + {}], eax",

        "xnor": "mov eax, [esp + {}]\
            \n\txor eax, [esp + {}]\
            \n\tnot eax\
            \n\tmov [esp + {}], eax"
    }
    return f'{dictcode[op].format(lhs, rhs, stackloc)}'