from django.urls import path
from . import views

urlpatterns = [
  path('login/', views.set_login, name='set_login'),
  path('data_entry/', views.set_data_entry, name='set_data_entry'),
  path('pengguna/', views.set_pengguna, name='set_pengguna'),
  path('pengguna/view/<id>', views.view_pengguna, name='view_pengguna'),
  path('api/pengguna/<int:user_id>/', views.get_pengguna_detail_api, name = 'get_pengguna_detail_api'),
  path('content/', views.set_content, name='set_content'),
  path('creation/', views.set_kelompok, name='set_kelompok'),
  path('pengguna/listpenggunabystate', views.search_pengguna_by_state, name='search_pengguna_by_state'),
  path('daftar/', views.set_icreation, name='set_icreation'),
  path('landingpage/', views.set_landing, name='set_landing'),
  path('homepage/', views.set_home, name='set_home'),
  path('icreation_list/', views.icreation_list, name='icreation_list'),
  
]
