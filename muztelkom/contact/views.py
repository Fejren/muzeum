from django.shortcuts import render
from django import http
from contact.forms import MessageForm


def contact(request):
    if request.method == 'POST':
        formset = MessageForm(request.POST, request.FILES)
        if formset.is_valid():
            formset.save()
            return http.HttpResponseRedirect(request.path)
    else:
        formset = MessageForm()
    context = {
        'formset': formset,
    }
    return render(request, 'muzeum/contact/contact.html', context)