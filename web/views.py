from utils import request_arg, optional_request_arg
from django.contrib.auth import authenticate
from django.contrib.auth import login as log_in
from django.contrib.auth import logout as log_out
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.core.context_processors import csrf
from templating import Template, error_page
from django.shortcuts import redirect
from backend.item_api import *
from backend.models import *
from itertools import izip_longest
from django.shortcuts import render
from forms import UserForm
from django.core.urlresolvers import reverse

def logout(request):
    if request.user.is_authenticated():
        log_out(request)
    return HttpResponseRedirect(reverse('login'))

def login(request):
    print request.session.items()
    context = {}
    context.update(csrf(request))
    form = UserForm(request.POST or None)
    if request.POST and form.is_valid():
        user = form.login(request)
        if user:
            log_in(request, user)
            return redirect(reverse("market"))
    context['form'] = form
    return render(request, 'web_login.html', context)

@login_required
def messages(request):
    user = request.user
    messages = Message.objects.filter(recipient=user)
    threads = []
    for message in messages:
        if message.thread not in threads:
            user2 = message.recipient if message.recipient != user else message.sender
            threads.append((message.thread, user2, message.thread.messages.all()))
    return render(request, 'inbox.html', {'user':user, 'threads':threads})

@login_required
def item(request, item_id):
    item = get_item(request, item_id=item_id)
    context =  {"item": item, 'user':request.user, 'supplier':item.supplier}
    context['user'] = request.user
    return Template("item.html", context)

@login_required
def market(request):
    context = {"items": get_all_items(request)}
    context['user']=request.user
    return render(request, 'market.html', context)

@login_required
def user(request, user_id):
    profile_user = CustomUser.objects.get(id=user_id)
    items = Item.objects.filter(supplier_id=user_id)
    context = {"profile_user" : profile_user, 'items': items, 'user':request.user}
    return render(request, 'user.html', context)

@login_required
def message(request):
    if request.method == "POST":
        user = request.user
        text = request.POST.get('text')
        print request
        if request.POST.get('thread_id'):
            print "reply id"
            print request.POST.get('thread_id')
            thread = Thread.objects.get(id=request.POST.get('thread_id'))
        else:
            thread = Thread()
            thread.save()

        message = Message(sender=user, thread=thread)
        if text:
            message.text = text
        else:
            message.text = ""
        user2_id = request.POST.get('user2_id')
        if user2_id:
            user2 = CustomUser.objects.get(id=user2_id)
            message.recipient = user2
        message.save()
        return HttpResponse("Message Sent")
    else:
        user_id = request.GET['user_id']
        user = request.user
        user2 = CustomUser.objects.get(id=user_id)
        context = {'user':user, 'user2':user2}
        if request.GET.get('thread_id'):
            context['thread_id'] = request.GET.get('thread_id')
        else:
            context['thread_id'] = False
        return render(request, 'message.html', context)
