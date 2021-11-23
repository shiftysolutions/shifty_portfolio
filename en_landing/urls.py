from django.urls import path

from en_landing.views import *

urlpatterns = [
    path('', IndexView.as_view(), name="en_index"),
    path('about/', AboutView.as_view(), name="en_about"),
    path('works/', WorksView.as_view(), name="en_works"),
    path('contact/', ContactView.as_view(), name="en_contact"),
]


urlpatterns += [
    path('services/', ServicesView.as_view(), name="en_services"),
]

urlpatterns += [
    path('hiring/', HiringListView.as_view(), name="en_hiring_list"),
    path('hiring/project-manager/', HiringDetailsView.as_view(), name="en_hiring_details"),
]

urlpatterns += [
    path('blog/', BlogListView.as_view(), name="en_blog"),
    path('blog/<str:article>/', BlogDetailsView.as_view(), name="en_blog_details"),
]