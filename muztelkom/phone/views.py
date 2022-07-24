from django.shortcuts import render
from django import http

from core.models import Phone, Mark

from phone.forms import PhoneForm


def gallery(request):
    phones = Phone.objects.all()
    marks = Mark.objects.all()

    if request.method == 'GET':
        search = request.GET.get('mark_filter', None)
        if search is not None:
            phones = Phone.objects.filter(mark__mark=search)
        else:
            phones = Phone.objects.all()

    context = {
        'phones': phones,
        'marks': marks,
    }
    return render(request, 'muzeum/gallery/gallery.html', context)


def create_phone(request):
    count_of_phones = Phone.objects.count()
    if count_of_phones:
        last_id = Phone.objects.last().id+1
    else:
        last_id = None
    if request.method == 'POST':
        formset = PhoneForm(request.POST, request.FILES)
        if formset.is_valid():
            formset.save()
            return http.HttpResponseRedirect(request.path)
    else:
        formset = PhoneForm()
    context = {
        'formset': formset,
        'phones_count': count_of_phones,
        'last_id': last_id,
    }
    return render(request, 'muzeum/gallery/gallery_form.html', context)