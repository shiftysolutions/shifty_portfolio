from django.urls import path, include

urlpatterns = [
    path('', include('landing.urls')),
    path('en/', include('en_landing.urls')),
]
