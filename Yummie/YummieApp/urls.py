from django.urls import path

from YummieApp import views
app_name='YummieApp'
urlpatterns=[
    path('',views.allProdCat,name='allProdCat'),
    path('<slug:c_slug>/', views.allProdCat, name='Products_by_Category'),
    path('<slug:c_slug>/<slug:product_slug>/',views.ProdCatDetail,name='ProdCatDetail')

]