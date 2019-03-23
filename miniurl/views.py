from django.shortcuts import render, redirect, get_object_or_404
from .models import URL
from .forms import URLForm
from django.http import HttpResponseRedirect


def generate_url(request):
    if request.method=='POST' or 'go' in request.POST:
        form = URLForm(request.POST)
        if form.is_valid():
            url = form.save(commit=False)
            url.generate_url()
            url.save()
            return redirect('url_detail', pk=url.tiny_url)
    else:
        form = URLForm(initial={'original_url': 'http://'})
    return render(request, 'miniurl/url.html', {'form': form})

def url_detail(request, pk):
    url = get_object_or_404(URL, pk=pk)
    return render(request, 'miniurl/url_detail.html', {'url': url})

def url_redirect(request, tiny_url):
    url = get_object_or_404(URL, pk=tiny_url)
    return HttpResponseRedirect(url.original_url)
