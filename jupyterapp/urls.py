from django.urls import path, include
from jupyterapp.views import *
urlpatterns = [
	path('',homepage , name = 'homepage'),
	path('configure/',configure, name = 'configure'),
	path('select_data/', select_data, name = 'select_data'),
	path('load_data/',load_data, name = 'load_data'),
	path('preprocess/',preprocess, name = 'preprocess'),
	path('select_columns',select_columns , name = 'select_columns'),
	path('jupyter_data/', jupyter_data , name = 'jupyter_data'),
]