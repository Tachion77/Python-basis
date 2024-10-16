f = open("poem.txt", "r")

word_stat = {}
for line in f:
    words = line.split(" ")
    print(words)
    for word in words:
        if word in word_stat:
            word_stat[word]+=1
        else:
            word_stat[word]=1

max_key = max(word_stat, key=word_stat.get)
print(f'Klucz z maksymalną wartością to: {max_key}, a wartość to: {word_stat[max_key]}')
