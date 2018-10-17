from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('^$',views.home,name = 'home'),

    url(r'^signup/$', views.signup, name='signup'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
    url(r'^new/image$', views.new_image, name='new-image'),
    url(r'^post/(\d+)',views.post,name ='post'),
    url(r'search/', views.search_projects, name='search_projects'),
    # url(r'^user/(\d+)$', views.profile, name='profile'),
    url(r'^project/(\d+)/review_design/$', views.add_design, name='add_design'),
    url(r'^project/(\d+)/review_usability/$', views.add_usability, name='review_usability'),
    url(r'^project/(\d+)/review_content/$', views.add_content, name='review_content'),
    url(r'^comment/(\d+)',views.comment,name='comment'),





]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
