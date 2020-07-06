from django.shortcuts import render

# Create your views here.

def main(request):
    return render(request, 'main.html') 

def result(request):
    full_text = request.GET['totaltext']
    word_num = full_text.split()
    word_dic = {}
    for word in word_num:
        if word in word_dic:
            word_dic[word] = word_dic[word] + 1 #{"종이컵":2}
        else:
            word_dic[word]=1   #{"종이컵":1}
#{"종이컵":2, "물통":1}
    return render(request, 'result.html', {'total_text': full_text, 'num': len(word_num), 'dictionary': word_dic.items()}) 
    
