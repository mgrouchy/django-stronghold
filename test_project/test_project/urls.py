from django.conf.urls import patterns, url
import views


urlpatterns = patterns(
    '',
    url(r'^protected/$', views.ProtectedView.as_view(), name="protected_view"),
    url(r'^public_decorator/$', views.PublicViewDecorator.as_view(), name="public_decorator"),
    url(r'^public_url/$', views.PublicViewURL.as_view(), name="public_url"),
    url(r'^public_named_url/$', views.PublicViewNamedURL.as_view(), name="public_named_url"),
    url(r'^public_named_url/(\w+)/$', views.PublicViewNamedURL.as_view(), name="public_named_url_params"),

)
