from django.shortcuts import render
from .forms import ColorfulContactForm
from django.http import HttpResponse
from django.template.loader import get_template
import os
from .settings import PROJECT_ROOT

def home(request):
    if request.method == 'POST':
        form = ColorfulContactForm(request.POST)
        if form.is_valid():
            pass
    else:
        form = ColorfulContactForm()
        if form.is_valid():
            return http.HttpResponseRedirect('')

    return render(request, 'home.html', {'form': form})

def return_data(request):
    f = 0
    if request.POST.get('latin') == '':
        text = request.POST.get('cyrillic')
        f = 1
    elif request.POST.get('cyrillic') == '':
        text = request.POST.get('latin')
        f = 2
    else:
        return HttpResponse('Error! For transliteration type text only in one field!')
    fd = open(os.path.join(PROJECT_ROOT, 'orthography_table_shugnanskiy.txt'),'r', encoding="utf8")
    tr = {}
    for line in fd.readlines():
        line = line.strip('\n')
        q = line.split('\t')
        if f == 1:
                tr[q[0]]=q[1]
        elif f == 2:
                tr[q[1]]=q[0]
    text_trans = ''
    sentence = text.split('\n')
    print(sentence)
    for s in sentence:
            newtranslit = ''
            for orig_smb in s:
                    if orig_smb in tr:
                            new_smb = tr[orig_smb]
                    else:        
                            new_smb = orig_smb
                    newtranslit = newtranslit + new_smb
            text_trans = text_trans + newtranslit + '\n'
    return render(request, 'output.html', {'translit': text_trans})





