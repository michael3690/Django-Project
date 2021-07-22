from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.mail import send_mail, get_connection
from django.urls import reverse
from django.contrib.auth.decorators import login_required, permission_required
from django.views.generic import ListView, DetailView

from . models import Page
from . models import Post
from .contact import ContactForm
from .content import ContentForm

def index(request, pagename=''):
    pagename = '/' + pagename
    pg = Page.objects.get(permalink=pagename)
    posts_all = Post.objects.all()
    posts={}
    for post in posts_all:
       posts[(post.title)] = post.maintext
    context = {
    'title': pg.title,
    'content': pg.bodytext,
    'last_updated': pg.update_date,
    'page_list': Page.objects.all(),
    'posts' : posts
    }
    return render(request, 'pages/page.html', context)

def contact(request):
    submitted = False
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            con = get_connection('django.core.mail.backends.console.EmailBackend')
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email', 'noreply@example.com'),
                ['noreply@example.com'],
                connection=con
            )
            return HttpResponseRedirect(reverse('contact') + '?submitted=True')
    else:
        form = ContactForm()
        if 'submitted' in request.GET:
            submitted = True
    context = {
        'form': form,
        'page_list': Page.objects.all(),
        'submitted': submitted
    }
    return render(request, 'pages/contact.html', context)

@login_required
@permission_required('pages.change_page', raise_exception=True)
def content(request):
    submitted = False
    if request.method == 'POST':
        print(request.user.id)
        form = ContentForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.author = request.user
            form.save()
            return HttpResponseRedirect(reverse('add_content') + '?submitted=True')
    else:
        form = ContentForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'pages/content.html', {'form':form, 'submitted':submitted})

class posts(ListView):
    model = Post
    template_name = 'pages/posts.html'
