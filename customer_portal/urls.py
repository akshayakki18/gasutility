from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.chooseoption, name='home'),  # Updated home URL to redirect to chooseoption view
    path('ServiceRequest/', views.servicerequest, name='ServiceRequest'),
    path('TrackRequest/', views.trackrequest, name='TrackRequest'),
    path('button/', views.chooseoption, name='button'),
    # Path for editing service request
    re_path(r'^edit_service_request/(?P<entry_id>[0-9]+)$', views.editservicerequest, name='edit_service_request'),
]
