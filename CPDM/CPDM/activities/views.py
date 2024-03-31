from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DetailView

from CPDM.accounts.models import Profile
from CPDM.activities.forms import ActivityCreateForm, ActivityUpdateForm
from CPDM.activities.models import Activity


class CreateActivityView(LoginRequiredMixin, CreateView):
    form_class = ActivityCreateForm
    model = Activity
    template_name = 'activities/create_activity.html'

    def get_queryset(self):
        user = self.request.user
        queryset = Activity.objects.filter(owner=user)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = self.request.user
        context['profile'] = profile
        return context

    def form_valid(self, form):
        form.instance.owner_id = self.request.user.pk
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('activity_list', kwargs={'pk': self.request.user.pk})


class UpdateActivityView(LoginRequiredMixin, UpdateView):
    form_class = ActivityUpdateForm
    template_name = 'activities/update_activity.html'
    success_url = reverse_lazy('activity_list')

    def get_queryset(self):
        activity_id = self.kwargs['activity_id']
        queryset = Activity.objects.filter(id=activity_id)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = self.request.user
        context['profile'] = profile
        return context

    def form_valid(self, form):
        form.instance.owner_id = self.request.user.pk
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('activity_list', kwargs={'pk': self.request.user.pk})


class ListActivityView(LoginRequiredMixin, ListView):
    model = Activity
    template_name = 'activities/list_activities.html'

    def get_queryset(self):
        queryset = Activity.objects.filter(owner=self.request.user)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = Profile.objects.get(pk=self.request.user.pk)
        context['profile'] = profile
        return context


class DetailsActivityView(LoginRequiredMixin, DetailView):
    model = Activity
    template_name = 'activities/activity_details.html'
    context_object_name = 'activity'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = self.request.user
        context['activity'] = self.object
        return context


def activity_details(request, pk, activity_id):
    profile = Profile.objects.get(pk=request.user.pk)
    activity = Activity.objects.get(pk=activity_id)

    form = ActivityUpdateForm(instance=activity)
    if request.method == 'POST':
        form = ActivityUpdateForm(request.POST, instance=activity)
        if form.is_valid():
            form.save()
            return redirect('activity_list', pk=pk)

    context = {
        'activity': activity,
        'profile': profile,
        'form': form,
    }
    return render(request, 'activities/activity_details.html', context)


def activity_update(request, pk, activity_id):
    profile = Profile.objects.get(pk=request.user.pk)
    activity = Activity.objects.get(pk=activity_id)

    form = ActivityCreateForm(instance=activity)
    if request.method == 'POST':
        form = ActivityUpdateForm(request.POST, instance=activity)
        if form.is_valid():
            form.save()
            return redirect('activity_list', pk=pk)

    context = {
        'activity': activity,
        'profile': profile,
        'form': form,
    }
    return render(request, 'activities/update_activity.html', context)
