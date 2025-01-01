def simpleassigngenerator(stackloc, value):
	return f"mov dword [ebp-{stackloc}], {value}"

