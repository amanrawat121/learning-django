from django.urls import path, re_path
from .views import DictionaryView
urlpatterns = [
    re_path(r"define/(?P<word>[a-zA-Z]+)/", DictionaryView.as_view(), name="dict")
]
