from collections import Counter
def freq_histogram(words):
    freq=dict(Counter(words))
    for x,count in freq.items():
        print(x ,':' ,'*'*count)
    
words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
freq_histogram(words)