from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse_lazy
from rest_framework import generics as views, permissions, status
from django.views.generic import CreateView, ListView, UpdateView, DetailView, DeleteView
from rest_framework.response import Response

from CPDM.accounts.models import Profile
from CPDM.activities.forms import ActivityCreateForm, ActivityUpdateForm, DeleteActivityForm
from CPDM.activities.models import Activity
from CPDM.activities.serielizers import ActivityListSerializer, ActivityCreateSerializer, ActivityDetailsSerializer, \
    ActivityDeleteSerializer


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
        profile = Profile.objects.get(pk=self.request.user)
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

    def get_object(self, **kwargs):
        obj = get_object_or_404(Activity, pk=self.kwargs.get('activity_id'))
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = self.request.user
        activity_id = self.kwargs['activity_id']
        context['profile'] = profile
        context['activity_id'] = activity_id
        return context

    def form_valid(self, form):
        form.instance.owner_id = self.request.user.pk
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy(
            'activity_details',
            kwargs={
                'pk': self.request.user.pk,
                'activity_id': self.kwargs['activity_id']}
        )


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
    template_name = 'activities/activity_details.html'

    def get_object(self, **kwargs):
        obj = get_object_or_404(Activity, pk=self.kwargs.get('activity_id'))
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = Profile.objects.get(pk=self.request.user)
        context['profile'] = profile

        return context

    def get_success_url(self):
        return reverse_lazy('activity_list', kwargs={'pk': self.request.user.pk})


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


class ActivityDeleteView(LoginRequiredMixin, DeleteView):
    form_class = DeleteActivityForm
    template_name = 'activities/activity_delete.html'
    form_class.base_fields['title'].disabled = True
    form_class.base_fields['description'].disabled = True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = Profile.objects.get(pk=self.request.user.pk)
        context['profile'] = profile
        return context

    def get_object(self, **kwargs):
        obj = get_object_or_404(Activity, pk=self.kwargs.get('activity_id'))
        return obj

    # populate the form
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = self.object
        return kwargs

    def get_success_url(self):
        return reverse_lazy('activity_list', kwargs={'pk': self.request.user.pk})


def delete_activity(request, pk, activity_id):
    profile = Profile.objects.get(pk=pk)
    activity = Activity.objects.get(pk=activity_id)

    form = DeleteActivityForm(instance=activity)
    if request.method == 'POST':

        activity.delete()
        return redirect('activity_list', pk=request.user.pk)

    context = {
        'profile': profile,
        'activity': activity,
        'form': form,
    }

    return render(request, 'activities/activity_delete.html', context)


class ActivityListApiView(views.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    list_serializer_class = ActivityListSerializer

    def get_queryset(self):
        super().get_queryset()
        queryset = Activity.objects.filter(owner=self.request.user)
        return queryset


class ActivityCreateApiView(views.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ActivityCreateSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ActivityDetailsUpdateDeleteApiView(views.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]

    details_serializer_class = ActivityDetailsSerializer
    update_serializer_class = ActivityCreateSerializer
    delete_serializer_class = ActivityDeleteSerializer

    serializer_class = details_serializer_class

    def get_object(self):
        obj = Activity.objects.get(pk=self.kwargs.get('activity_id'))
        return obj

    def get_serializer_class(self):
        if self.request.method == 'PUT':
            self.serializer_class = self.update_serializer_class
        elif self.request.method == 'DELETE':
            self.serializer_class = self.delete_serializer_class
        elif self.request.method == 'GET':
            self.serializer_class = self.details_serializer_class

        return self.serializer_class
