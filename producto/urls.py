from django.urls import path


from .views import ProductoView, ProductoNew, ProductoEdit, producto_inactivar
    

urlpatterns = [

    path('producto/' , ProductoView.as_view(), name='producto_list'),
    path('producto/new' , ProductoNew.as_view(), name='producto_new'),
    path('producto/edit/<int:pk>' , ProductoEdit.as_view(), name='producto_edit'),
    path('producto/inactivar/<int:id>' , producto_inactivar, name='producto_inactivar'),

    
]
