from django.shortcuts import render, redirect, get_object_or_404
from .models import URL
from .forms import URLForm


def generate_url(request):
    if request.method=='POST' or 'go' in request.POST:
        form = URLForm(request.POST)
        if form.is_valid():
            url = form.save(commit=False)
            url.generate_url()
            url.save()
            return redirect('url_detail', pk=url.pk)
    else:
        form = URLForm()
    return render(request, 'miniurl/url.html', {'form': form})

def url_detail(request, pk):
    url = get_object_or_404(URL, pk=pk)
    return render(request, 'miniurl/url_detail.html', {'url': url})
