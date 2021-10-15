def compararString(a, b):
    i = 0
    while i < len(a):
        if a[i] != b[i]:
            return False
            break
        i += 1
    return True