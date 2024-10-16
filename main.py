Alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def crypt(text):
    split = list(text)
    # print(split)
    cripted = ""
    for i in range(len(split)):
        # if split[i] in Alphabet:
            # print(Alphabet.index(split[i])+1)
        cripted += str(Alphabet.index(split[i])+1)

    print(cripted)


if __name__ == "__main__":
    crypt("hello")
    crypt("mamaco")
