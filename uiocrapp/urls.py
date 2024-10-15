from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
 
# urlpatterns=[
#     path('',views.customer_form_view),
# ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns=[
    path('',views.customer_form_view),
    # path('getValuesFromDB', views.getDBValues),
    # path('getFileFromOutbound',views.getDBValues)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)