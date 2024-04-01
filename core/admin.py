from django.contrib import admin
from django.apps import apps

from core.models import *
models = apps.get_models()

for model in models:
    try:
        admin.site.register(model) #Register all models that aren't already registered
    except:
        pass #If the model is already registed, don't bother