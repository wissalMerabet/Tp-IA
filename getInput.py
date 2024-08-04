def but(text):
    return text.strip('\n').split(',')


def baseFait(text):

    return text.strip('\n').split(',')


def regles(text):

    R = text.split('\n')
    R = [(elem.split('=>')[0].split('+'), elem.split('=>')[1]) for elem in R]
           # parti1                            # parti2
    return R


def file(c=True, file='file'):

    with open(file+'.txt') as f:
        inputdata = f.read()
        data = inputdata.split('\n\n')

        if c:
            return data[0], data[1]
        else:
            return data[0], data[1], data[2]

