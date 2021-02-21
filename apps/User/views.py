import json

from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render

from apps.User.forms import UserEditForm

User = get_user_model()


@login_required
def update_profile(request, pk):
    if request.user.pk != pk:
        return HttpResponseRedirect('/')
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