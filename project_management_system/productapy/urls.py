from django.urls  import path
from . import views

urlpatterns=[
    path("",views.ProductsListView.as_view(),), #get.post
    path('<int:product_id>/',views.ProductDetailsView.as_view()),#get,put,patch,delete
]