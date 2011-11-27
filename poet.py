import random

def randomly_split(seq):
    index = 0
    split_seq = []
    while index < len(seq):
	offset = random.randint(1, len(seq) - index)
	split_seq.append(seq[index:index + offset])
	index += offset
    return split_seq


def make_poem(string):
    words = string.split()
    return '\n'.join(' '.join(line) for line in randomly_split(words))
