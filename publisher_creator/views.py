from django.shortcuts import render, redirect
# from django.http import HttpResponseRedirect
from .models import PublisherCreator

def publisher_creator_detail(request, pcid):
    pc = PublisherCreator.objects.get(pk = pcid)
    is_following = True if request.user in pc.followers.all() else False
    context = {
        'pc': pc,
        'is_following': is_following
    }
    return render(request, 'publisher/publisher_creator.html', context)

def follow_pc(request, pcid):                       #NOTE - Скоро удалим
    followers = PublisherCreator.objects.get(pk = pcid).followers
    if request.user in followers.all():
        followers.remove(request.user)
    else:
        followers.add(request.user)

    return redirect(request.META.get('HTTP_REFERER'))