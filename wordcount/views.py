from django.shortcuts import render
from firstproject import settings
# Create your views here.
def home(request):
    return render(request, 'wordcount/home.html')

def about(request):
    return render(request, 'wordcount/about.html', {
        'STATIC_URL' : settings.STATIC_URL,
    })

def count(request):
    full_text = request.GET['fulltext']
    word_list = full_text.split()
    word_dictionary = {}

    for word in word_list:
        if word in word_dictionary:
            word_dictionary[word]+=1
        else:
            word_dictionary[word]=1
            
    return render(request, 'wordcount/count.html', {
        'full_text': full_text,
        'total' : len(word_list),
        'dictionary' : word_dictionary.items(),
    })