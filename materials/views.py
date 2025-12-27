from django.shortcuts import render, redirect
from .models import Material
from django.contrib.auth.decorators import login_required

def home(request):
    materials = Material.objects.all().order_by('-uploaded_at')
    return render(request, 'home.html', {'materials': materials})

@login_required
def upload_material(request):
    if request.method == 'POST':
        Material.objects.create(
            user=request.user,
            title=request.POST['title'],
            subject=request.POST['subject'],
            description=request.POST['description'],
            file=request.FILES['file']
        )
        return redirect('home')
    return render(request, 'upload.html')
