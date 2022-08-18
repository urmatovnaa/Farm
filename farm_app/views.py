from rest_framework import viewsets
from django.shortcuts import render, redirect
from farm_app.forms import AboutUsForm

from farm_app.models import Contact, AboutUs, Main
from farm_app.serializers import ContactSerializer, AboutUsSerializer, MainSerializer


class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class AboutUsViewSet(viewsets.ModelViewSet):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializer

    def AboutUsList(request):
        aboutus = AboutUs.objects.all()
        return render(request, "book-list.html", {'aboutus': aboutus})

    def AboutUsCreate(request):
        if request.method == "POST":
            form = AboutUsForm(request.POST)
            if form.is_valid():
                try:
                    form.save()
                    model = form.instance
                    return redirect('aboutus-list')
                except:
                    pass
        else:
            form = AboutUsForm()
        return render(request, 'book-create.html', {'form': form})

    def AnoutUSDelete(request, id):
        about_us = AboutUs.objects.get(id=id)
        try:
            AboutUs.delete()
        except:
            pass
        return redirect('aboutus-list')


class MainViewSet(viewsets.ModelViewSet):
    queryset = Main.objects.all()
    serializer_class = MainSerializer

