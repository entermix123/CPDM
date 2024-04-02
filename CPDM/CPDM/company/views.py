from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DetailView, DeleteView

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
        profile = Profile.objects.get(pk=self.request.user.pk)
        context['profile'] = profile
        return context


class UpdateCompanyView(LoginRequiredMixin, UpdateView):
    form_class = CompanyUpdateForm
    template_name = 'company/update_company.html'

    def get_object(self):
        obj = get_object_or_404(Company, pk=self.kwargs.get('company_id'))
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = self.request.user
        company_id = self.kwargs['company_id']
        context['profile'] = profile
        context['company_id'] = company_id
        return context

    def form_valid(self, form):
        form.instance.owner_id = self.request.user.pk
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('company_list', kwargs={'pk': self.request.user.pk})


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
    return render(request, 'company/company_details.html', context)


class DetailsCompanyView(LoginRequiredMixin, DetailView):
    template_name = 'company/company_details.html'

    def get_object(self):
        obj = get_object_or_404(Company, pk=self.kwargs.get('company_id'))
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = Profile.objects.get(pk=self.request.user)
        context['profile'] = profile

        return context

    def get_success_url(self):
        return reverse_lazy('company_list', kwargs={'pk': self.request.user.pk})


class DeleteCompanyView(LoginRequiredMixin, DeleteView):
    form_class = CompanyDeleteForm
    template_name = 'company/delete_company.html'
    form_class.base_fields['type'].disabled = True
    form_class.base_fields['name'].disabled = True
    form_class.base_fields['industry'].disabled = True
    form_class.base_fields['website'].disabled = True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = Profile.objects.get(pk=self.request.user.pk)
        context['profile'] = profile
        return context

    def get_object(self):
        obj = get_object_or_404(Company, pk=self.kwargs.get('company_id'))
        return obj

    # populate the form
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = self.object
        return kwargs

    def get_success_url(self):
        return reverse_lazy('company_list', kwargs={'pk': self.request.user.pk})


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
