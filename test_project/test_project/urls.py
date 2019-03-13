from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^protected/$', views.ProtectedView.as_view(), name="protected_view"),
    url(r'^public/$', views.PublicView.as_view(), name="public_view"),
    url(r'^public2/$', views.PublicView2.as_view(), name="public_view2"),
    url(r'^public3/$', views.public_view3, name="public_view3")
]
