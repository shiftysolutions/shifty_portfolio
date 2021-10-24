from django.urls import path

from landing.views import *

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('about/', AboutView.as_view(), name="about"),
    path('works/', WorksView.as_view(), name="works"),
    path('contact/', ContactView.as_view(), name="contact"),
]


urlpatterns += [
    path('services/', ServicesView.as_view(), name="services"),
]

urlpatterns += [
    path('hiring/', HiringListView.as_view(), name="hiring_list"),
    path('hiring/project-manager/', HiringDetailsView.as_view(), name="hiring_details"),
]

