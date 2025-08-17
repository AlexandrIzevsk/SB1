
from django.conf import settings
from django.urls import path
from django.contrib.auth import views
from .views import logout_view

#
# urlpatterns = [
#     path('logout/', logout_view, name='logout'),
# ]
urlpatterns = [
    path('logout', logout_view, name='logout')
]