from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView

from CPDM.company.forms import CompanyCreateForm
from CPDM.company.models import Company


class CreateCompanyView(LoginRequiredMixin, CreateView):
    form_class = CompanyCreateForm
    model = Company
    template_name = 'company/create_company.html'

    def get_queryset(self):
        user = self.request.user
        queryset = Company.objects.filter(owner=user)
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


class UpdateCompanyView(LoginRequiredMixin, UpdateView):
    form_class = CompanyCreateForm
    model = Company
    template_name = 'company/update_company.html'
    success_url = reverse_lazy('company_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = self.request.user
        context['profile'] = profile
        return context


class CompanyListView(LoginRequiredMixin, ListView):
    model = Company
    template_name = 'company/list_companies.html'

    def get_queryset(self):
        queryset = Company.objects.filter(owner=self.request.user)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = self.request.user
        return context
