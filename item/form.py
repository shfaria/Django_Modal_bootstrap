from dataclasses import fields
from django.forms import ModelForm
from django.utils.translation import gettext as _
from django import forms
from django.contrib.auth import get_user_model
from .models import *


class simple(ModelForm):
    class Meta:
        model = Demo
        fields = '__all__'
        