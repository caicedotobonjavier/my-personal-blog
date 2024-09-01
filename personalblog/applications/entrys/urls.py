from django.urls import path, re_path, include
#
from . import views

app_name = 'entry_app'

urlpatterns = [
    path('entrys/', views.AllEntrysView.as_view(), name='list_entrys'),
    path('new-entry/', views.CreateNewEntry.as_view(), name='new_entrys'),
]