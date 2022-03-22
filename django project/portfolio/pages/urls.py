from django.urls import path

from .views import index,contact,blog,blog_single

urlpatterns = [
    path("", index, name="index"),
    path("contact/", contact, name="contact"),
    path("blog/", blog, name="blog"),
    path("blog_single/", blog_single, name="blog_single")
]