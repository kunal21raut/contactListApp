from django.shortcuts import render, redirect
from .models import Contact
# Create your views here.
def index(request):
    contacts = Contact.objects.all()

    search_input = request.GET.get('searchbar')

    if search_input:
        contacts = Contact.objects.filter(full_name__icontains=search_input)
    else:
        contacts = Contact.objects.all()
        search_input = ''
        
    context = {
        'contacts':contacts,
        'search_input':search_input,
    }
    return render(request,'contactListApp/index.html',context=context)

def addcontact(request):
    if request.method == 'POST':
        new_contact = Contact(
            full_name = request.POST['fullname'],
            relationship = request.POST['relationship'],
            email = request.POST['email'],
            phone_number =request.POST['phonenumber'],
            address = request.POST['address']
        )
        new_contact.save()
        return redirect('index')
    return render(request,'contactListApp/add-contact.html')

def contactprofile(request,pk):
    contact = Contact.objects.get(id = pk)

    context = { 'contact':contact }
    return render(request,'contactListApp/contact-profile.html',context=context)

def editcontact(request,pk):
    contact =  Contact.objects.get(id=pk)

    if request.method == 'POST':
        contact.full_name = request.POST['fullname']
        contact.relationship = request.POST['relationship']
        contact.phone_number = request.POST['phonenumber']
        contact.email = request.POST['email']
        contact.address = request.POST['address']

        contact.save()
        return redirect('/contactprofile/'+str(contact.id))

    context = { 'contact':contact }
    return render(request,'contactListApp/edit-contact.html',context=context)

def deletecontact(request,pk):
    contact = Contact.objects.get(id=pk)
    if request.method == 'POST':
        contact.delete()
        return redirect('/')
    context = { 'contact':contact }
    return render(request,'contactListApp/delete-contact.html',context=context)