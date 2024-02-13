from django.shortcuts import render

# Create your views here.
# image_upload/views.py
from django.shortcuts import render, redirect
from .models import Image
from .forms import ImageForm

def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('image_list')
    else:
        form = ImageForm()
    return render(request, 'up/upload_image.html', {'form': form})

def image_list(request):
    images = Image.objects.all()
    return render(request, 'up/image_list.html', {'images': images})

