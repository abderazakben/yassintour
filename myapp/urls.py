from django.urls import path
from .views import Three , Home , LogoutUser ,excursions ,activitisform , AdminLoginView , HomePageView ,Excursionsform , ExDetail ,AddToCartView ,MyCartView , MangeCartView ,EmptyCartView ,ChechoutView ,HotilLoginForm , HomePageHotilView

app_name = 'myapp'

urlpatterns = [
    path('', Home, name="home" ),
    path('excursions/',  excursions, name="excursions"),
    path('excursions/<str:slug>', ExDetail, name="Detail"),
    path('activitie/', Three, name="activitie"),
    #  Ussre page urls
    path('logout/',LogoutUser,name="logout"),

    # Add  the Cart  

    path("add-to-cart-<int:pro_id>" , AddToCartView.as_view(), name="addtocart"),
    path('my-cart/', MyCartView.as_view() , name="mycart"),
    path("mange-cart/<int:cp_id>/",MangeCartView.as_view(), name='mangecart'),
    path("empty-cart/" , EmptyCartView.as_view(), name="emptycart"),
    path("checkout/", ChechoutView.as_view() , name="chechout"),




    #adminpage///
    path('activitieform/', activitisform, name="activitieform"),
    path('excursionsform/', Excursionsform, name="excursionsform"),
    path("admin-login/", AdminLoginView.as_view(), name="adminlogin"),
    path("pageadmin/",  HomePageView.as_view(), name="pageadmin"),
    path("hotil_login/", HotilLoginForm.as_view(), name="hotillogin"),
     path("pagehoteladmin/",  HomePageHotilView.as_view(), name="pagehotiladmin"),
    
]

