from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    return render(request,'home.html')
def count(request):
    fulltext=request.GET['fulltext']
    
    wordList=fulltext.split()
    count=0
    for words in wordList:
        for char in words:
            print(count)
            count+=1
    avgchars= count/len(wordList)  
          
    return render(request,'count.html',{'fulltext':fulltext,'count':len(wordList),'avgchars':avgchars}) 
def about(request):
    return render(request, 'about.html') 