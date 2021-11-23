from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('fr/', include('landing.urls')),
    path('', include('en_landing.urls')),
]

handler404 = 'en_landing.views.error_404'
handler500 = 'en_landing.views.error_500'
handler403 = 'en_landing.views.error_403'
handler400 = 'en_landing.views.error_400'