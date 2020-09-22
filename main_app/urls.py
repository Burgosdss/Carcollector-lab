from django.urls import path
from . import views

urlpatterns = [
   path('', views.home, name='home'),
   path('about/', views.about, name='about'),
   path('cars/', views.cars_index, name='index'),
   path('cars/<int:car_id>', views.cars_detail, name='detail'),
   path('cars/create/', views.CarCreate.as_view(), name='cars_create'),
   path('cars/<int:car_id>/add_maint/', views.add_maint, name='add_maint'),
   path('cars/<int:car_id>/assoc_addon/<int:addon_id>/', views.assoc_addon, name='assoc_addon'),
   path('cars/<int:car_id>/add_photo/', views.add_photo, name='add_photo'),
   path('cars/<int:pk>/update/', views.CarUpdate.as_view(), name='cars_update'),
   path('cars/<int:pk>/delete/', views.CarDelete.as_view(), name='cars_delete'),
   path('addons/', views.addons_index, name='addons_index'),
   path('addons/<int:addon_id>/', views.addons_detail, name='addons_detail'),
   path('addons/create/', views.AddonCreate.as_view(), name='addons_create'),
   path('addons/<int:pk>/update/', views.AddonUpdate.as_view(), name='addons_update'),
   path('addons/<int:pk>/delete/', views.AddonDelete.as_view(), name='addons_delete'),
   path('account/signup', views.signup, name='signup'),
]