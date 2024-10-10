from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, UpdateView, ListView
from .models import Member
from .forms import MemberForm
from django.contrib.auth.mixins import LoginRequiredMixin


class ContactListView(ListView):
    model = Member
    template_name = 'Member_list.html'
    context_object_name = 'page_obj'
    paginate_by = 10


class ContactCreateView(LoginRequiredMixin, CreateView):
    model = Member
    form_class = MemberForm
    template_name = 'Member_form.html'
    success_url = reverse_lazy('members_list')


class ContactUpdateView(LoginRequiredMixin, UpdateView):
    model = Member
    form_class = MemberForm
    template_name = 'Member_form.html'
    success_url = reverse_lazy('members_list')


class ContactDeleteView(LoginRequiredMixin, DeleteView):
    model = Member
    template_name = 'member_confirm_del.html'
    success_url = reverse_lazy('members_list')
