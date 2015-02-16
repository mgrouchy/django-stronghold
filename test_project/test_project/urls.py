from django.conf.urls import patterns, url
from . import views


urlpatterns = patterns(
    '',
    url(r'^protected/$', views.ProtectedView.as_view(), name="protected_view"),
    url(r'^public/$', views.PublicView.as_view(), name="public_view"),
)
