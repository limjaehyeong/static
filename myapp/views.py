from django.shortcuts import render

def main(request):
    return render(request, 'main.html')

def result(request):
    word_text = request.GET['totaltext']    
    word_list = word_text.split()

    word_dict = {}
    for word in word_list:
        if word in word_dict:
            word_dict[word] +=1
        else:
            word_dict[word] =1

    return render(request, 'result.html', {'total_text' : word_text, 'total' : len(word_list),
    'dictionary' : word_dict.items()})

def profile(request):
    return render(request, 'profile.html')

