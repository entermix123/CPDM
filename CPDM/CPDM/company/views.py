from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView

from CPDM.accounts.models import Profile
from CPDM.company.forms import CompanyCreateForm, CompanyUpdateForm, CompanyDeleteForm
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
        return reverse_lazy('company_list', kwargs={'pk': self.request.user.pk})


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


def company_details(request, pk, company_id):
    profile = Profile.objects.get(pk=request.user.pk)
    company = Company.objects.get(pk=company_id)

    form = CompanyUpdateForm(instance=company)
    if request.method == 'POST':
        form = CompanyUpdateForm(request.POST, instance=company)
        if form.is_valid():
            form.save()
            return redirect('activity_list', pk=pk)

    context = {
        'company': company,
        'profile': profile,
        'form': form,
    }
    return render(request, 'company/company_details.html.html', context)


def company_update(request, pk, company_id):
    profile = Profile.objects.get(pk=request.user.pk)
    company = Company.objects.get(pk=company_id)

    form = CompanyCreateForm(instance=company)
    if request.method == 'POST':
        form = CompanyUpdateForm(request.POST, instance=company)
        if form.is_valid():
            form.save()
            return redirect('company_list', pk=pk)

    context = {
        'company': company,
        'profile': profile,
        'form': form,
    }
    return render(request, 'company/update_company.html', context)


def company_delete(request, pk, company_id):
    profile = Profile.objects.get(pk=pk)
    company = Company.objects.get(pk=company_id)

    form = CompanyDeleteForm(instance=company)
    if request.method == 'POST':

        company.delete()
        return redirect('company_list', pk=request.user.pk)

    context = {
        'profile': profile,
        'company': company,
        'form': form,
    }

    return render(request, 'company/delete_company.html', context)
