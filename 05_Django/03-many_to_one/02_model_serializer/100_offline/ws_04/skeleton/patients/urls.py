from django.urls import path
from . import views
urlpatterns = [
    path("", views.patient_list_create),
    path("<int:patient_id>/", views.patient_detail)

]