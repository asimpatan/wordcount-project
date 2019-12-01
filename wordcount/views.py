from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    return render(request,"index.html")

def count(request):
    fulltext = request.GET['fulltext']
    # print(fulltext)
    wordlist = fulltext.split()
    word_dictionary = {}

    for word in wordlist:
        if word in word_dictionary:
            # increase
            word_dictionary[word] += 1
        else:
            # add to word_dictionary
            word_dictionary[word] = 1
    # return render(request, "count.html", {'fulltext': fulltext , 'count': len(wordlist), 'word_dictionary': word_dictionary.items() })
    # 2nd method
    sortedwords = sorted(word_dictionary.items(), key = operator.itemgetter(1), reverse = False )

    return render(request, "count.html", {'fulltext': fulltext , 'count': len(wordlist), 'sortedwords': sortedwords })


def about(request):
    return render(request,"about.html")
