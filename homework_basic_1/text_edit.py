sentences = ['123', 'My name is 9Pasha ebashu1', '123й']


def process(sentences):
    result = []
    for i in sentences:
        prom = list(filter(lambda x: x.isalpha(), i.split()))
        result.append(" ".join(prom))
    return result


print(process(sentences))
