from django.urls import path
from . import views
urlpatterns = [
    path("new/", views.patient_create),
    path("", views.patient_list),
    path("<int:patient_id>/", views.patient_detail),
    path("<int:patient_id>/update/", views.patient_update),
    path("<int:patient_id>/delete/", views.patient_delete)

]