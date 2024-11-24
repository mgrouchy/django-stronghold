from django.urls import re_path
from . import views


urlpatterns = [
    re_path(r'^protected/$', views.ProtectedView.as_view(), name="protected_view"),
    re_path(r'^public/$', views.PublicView.as_view(), name="public_view"),
    re_path(r'^public2/$', views.PublicView2.as_view(), name="public_view2"),
    re_path(r'^public3/$', views.public_view3, name="public_view3")
]
