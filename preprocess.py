import collections

def preprocessing(words):
    
    counter = collections.Counter(words)
    most_common, frequency = counter.most_common()[0]
    longest = max(words, key=len)
    often = str(most_common)
    max_len = str(longest)
    return [often, max_len]

    # print("Часто встречающееся: "+,"Самое длинное:"+ str(longest), sep="\n")

