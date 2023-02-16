def power(Base, Exponent):
    if Exponent == 0 or Base == 0:
        return 1

    if Exponent % 2 == 0:
        NewBase = power(Base, Exponent/2)
        return NewBase * NewBase

    else:
        NewBase = power(Base, (Exponent-1)/2)
        return (NewBase * NewBase) * Base