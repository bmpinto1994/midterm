from django.shortcuts import render
from django.views.generic import TemplateView

class Home(TemplateView):
  template_name = "home.html"

from django.views.generic import CreateView
from django.core.urlresolvers import reverse_lazy
from .models import *

class MessageCreateView(CreateView):
  model = Message
  template_name = "message/message_form.html"
  fields = ['title', 'description']
  success_url = reverse_lazy('home')
# Create your views here.
