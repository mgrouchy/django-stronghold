from django.conf.urls import patterns, url
import views


urlpatterns = patterns(
    '',
    url(r'^protected/$', views.ProtectedView.as_view(), name="protected"),
    url(r'^public/$', views.PublicView.as_view(), name="public"),
)
