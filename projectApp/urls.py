from django.contrib.admindocs import views
from django.urls import path

# importing views from views..py
from .views import update_view, detail_view

from .views import detail_view
from .views import create_view
from .views import list_view
from .views import update_view
from .views import delete_view


urlpatterns = [
    path('', create_view),
    path('', list_view),
    path('<id>/', detail_view),
    path('<id>/update', update_view),
    path('<id>/delete', delete_view),
]