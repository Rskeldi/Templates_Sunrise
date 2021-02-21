import json

from django.contrib.auth import get_user_model
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from apps.User.forms import UserEditForm

User = get_user_model()


def update_profile(request, pk):
    args = {}

    if request.method == 'POST':
        json_post = json.load(request)
        user = User.objects.get(pk=request.user.pk)
        user.first_name = json_post['first_name']
        user.last_name = json_post['last_name']
        user.save()
    form = UserEditForm()
    obj = User.objects.get(pk=pk)
    args['form'] = form
    args['object'] = obj
    return render(request, 'account/user_edit.html', args)