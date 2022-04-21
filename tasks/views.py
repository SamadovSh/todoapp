from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import TodoItem
from .forms import TodoItemForm
from django.views import View
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from datetime import datetime


def index(request):
    print('sssss')
    return redirect('/accounts/login')


def complete_task(request, uid):
    t = TodoItem.objects.get(id=uid)
    t.is_completed = True
    t.save()
    return HttpResponse('OK')


def delete_task(request, uid):
    t = TodoItem.objects.get(id=uid)
    t.delete()
    messages.success(request, "Deleted")
    return redirect('/tasks/list')


class TaskListView(LoginRequiredMixin, ListView):
    model = TodoItem
    context_object_name = 'tasks'
    template_name = 'tasks/list.html'

    def get_queryset(self):
        qs = super().get_queryset()
        u = self.request.user
        if u.is_anonymous:
            return []
        return qs.filter(owner=u)


class TaskCreateView(View):
    def post(self, request, *args, **kwargs):
        form = TodoItemForm(request.POST)
        if form.is_valid():
            new_task = form.save(commit=False)
            new_task.owner = request.user
            new_task.save()
            messages.success(request, 'Successfully added')
            return redirect('/tasks/list')

        return render(request, 'tasks/create.html', {"form": form})

    def get(self, request, *args, **kwargs):
        form = TodoItemForm()
        return render(request, 'tasks/create.html', {"form": form})


class TaskDetailsView(DetailView):
    model = TodoItem
    template_name = 'tasks/details.html'


class TaskEditView(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        t = TodoItem.objects.get(id=pk)
        form = TodoItemForm(request.POST, instance=t)
        if form.is_valid():
            new_task = form.save(commit=False)
            new_task.owner = request.user
            new_task.updated = datetime.now()
            new_task.save()
            return redirect('/tasks/list')

        return render(request, 'tasks/edit.html', {"form": form, "tasks": t})

    def get(self, request, pk, *args, **kwargs):
        t = TodoItem.objects.get(id=pk)
        form = TodoItemForm(instance=t)
        return render(request, 'tasks/edit.html', {"form": form, "tasks": t})

