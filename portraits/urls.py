from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from portraits import views
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.PortraitList.as_view()),
    url(r'^(?P<pk>[0-9]+)/$', views.PortraitDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

from webtech import settings
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)