from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('product-view-page/<int:id>', views.product_view, name="product_view"),
    path('brand-wise-products/<str:brands>', views.brands_product, name="brands_product"),
    path('category-wise-products/<str:category>', views.categorial_product, name="categorial_product"),
    path('aboutus/', views.aboutus, name="aboutus"),
    path('contactus/', views.contactus, name="contactus"),
    path('checkout/', views.checkout, name="checkout"),
    path('search/', views.search, name="search"),
    path('signup', views.handelSignup, name='handelSignup'),
    path('login', views.handelLogin, name='handelLogin'),
    path('logout', views.handelLogout, name='handelLogout'),
]