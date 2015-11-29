def pan(phrase):
    for i in "abcdefghijklmnopqrstuvwxyz" :
        if  i not in phrase:
            return False
    return True


print pan("the quick  brown fox jumps over the lazy dog")

