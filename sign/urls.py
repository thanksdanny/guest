from django.conf.urls import url
from sign import views_if
from sign import view_if_sec

urlpatterns = [
    # sign system interface:
    # ex : /api/add_event/
    url(r'^add_event/', views_if.add_event, name='add_event'),
    # ex : /api/get_event_list/
    url(r'^add_guess/', views_if.add_guest, name='add_guess'),
    # ex : /api/get_event_list
    url(r'^get_event_list/', views_if.get_event_list, name='get_event_list'),
    # ex : /api/get_guess_list
    url(r'^get_guess_list/', views_if.get_guest_list, name='get_guess_list'),
    # ex : /api/user_sign/
    url(r'^user_sign/', views_if.user_sign, name='user_sign'),
    # ex : /api/sec_get_event_list/
    url(r'^sec_get_event_list/', view_if_sec, name='get_event_list')
]


