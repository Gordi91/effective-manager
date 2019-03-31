from django.urls import path
from . import views

urlpatterns = [
    # certificates
    path('', views.CertificatesListView.as_view(), name='show_certificates'),
    path('new-certificate', views.NewCertificate.as_view(), name='new_certificate'),
    path('modify-certificate/<int:id>/', views.ModifyCertificate.as_view(), name='modify_certificate'),
    path('delete-certificate/<int:id>/', views.DeleteCertificate.as_view(), name='delete_certificate'),
    path('show-certificate/<int:id>/', views.ShowCertificate.as_view(), name='show_certificate'),
    path('<int:pk>/poll-done/', views.poll_done, name='poll_done'),
    path('<int:pk>/certificate-done/', views.certificate_done, name='certificate_done'),
    # clients
    path('clients/', views.ShowClients.as_view(), name='show_clients'),
    path('new-client', views.NewClient.as_view(), name='new_client'),
    path('modify-client/<int:id>/', views.ModifyClient.as_view(), name='modify_client'),
    path('delete-client/<int:id>/', views.DeleteClient.as_view(), name='delete_client'),
    path('show-client/<int:id>/', views.ShowClient.as_view(), name='show_client'),
]
