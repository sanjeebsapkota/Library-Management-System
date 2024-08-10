from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Library

# Create your views here.
def home(request):
    library_objs= Library.objects.all()
    data={'librarys':library_objs}
    

    return render(request,'index.html',context=data)


def create(request):
    if request.method=="POST":
        name = request.POST.get('name')
        description = request.POST.get('description')
        category = request.POST.get('category')
        author = request.POST.get('author')
        bookformat = request.POST.get('bookformat')
        Library.objects.create(Name=name,Description=description,Category=category,Author=author,BooksFormat=bookformat)
        return redirect('home')
    return render (request,'create.html')

def edit(request,pk):
    library_objs = Library.objects.get(id=pk)
    if request.method =="POST":
        
        name = request.POST.get('name')
        description = request.POST.get('description')
        category = request.POST.get('category')
        author = request.POST.get('author')
        bookformat = request.POST.get('bookformat')
        library_objs.Name = name
        library_objs.Description = description
        library_objs.Category = category
        library_objs.Author = author
        library_objs.BooksFormat = bookformat
        library_objs.save()
        return redirect('home')
    

    
    library_objs = Library.objects.get(id=pk)
    data = {'librarys':library_objs}
    return render (request,'edit.html',context=data)

def delete(request,pk):
    library_obj = Library.objects.get(id=pk)
    library_obj.delete()
    return redirect('home')