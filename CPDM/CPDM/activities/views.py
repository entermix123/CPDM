from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView

from CPDM.accounts.models import Profile
from CPDM.activities.forms import ActivityCreateForm
from CPDM.activities.models import Activity


class CreateActivityView(LoginRequiredMixin, CreateView):
    form_class = ActivityCreateForm
    model = Activity
    template_name = 'activities/create_activity.html'

    def get_queryset(self):
        profile = Profile.objects.get(pk=self.request.user.pk)
        queryset = Activity.objects.filter(owner=profile)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = self.request.user
        context['profile'] = profile
        return context

    def form_valid(self, form):
        profile = Profile.objects.get(pk=self.kwargs['pk'])
        form.instance.owner_id = profile.pk
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('activity_list', kwargs={'pk': self.request.user.pk})


class UpdateActivityView(LoginRequiredMixin, UpdateView):
    form_class = ActivityCreateForm
    model = Activity
    template_name = 'activities/update_activity.html'
    success_url = reverse_lazy('activity_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = self.request.user
        context['profile'] = profile
        return context


class ActivityListView(LoginRequiredMixin, ListView):
    model = Activity
    template_name = 'activities/list_activities.html'

    def get_queryset(self):
        queryset = Activity.objects.filter(owner=self.request.user)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = self.request.user
        return context
