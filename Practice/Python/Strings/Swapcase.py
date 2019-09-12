def swap_case(s):
    smallcase = []
    capscase = []
    swapcase = ""
    for letter in "abcdefghijklmnopqrstuvwxyz":
        smallcase.append(letter)
    for letterx in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        capscase.append(letterx)
    for letter in s:
        if letter in smallcase:
            swapcase += capscase[smallcase.index(letter)]
        elif letter in capscase:
            swapcase += smallcase[capscase.index(letter)]
        else:
            swapcase += letter
    return swapcase
