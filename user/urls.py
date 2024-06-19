from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import UserViewSet,SessionUserViewSet
# from .views import UserProfileViewSet, UserViewSet, user_login, register, dashboard, edit, user_logout
# from .views import  (user_login_api ,
#                         current_user_detail , 
#                         edit_user_api , 
#                         user_logout_api , 
#                         register_user_api ,
#                         get_userprofile,
#                         get_active_users)

router = SimpleRouter()
router.register(r'', UserViewSet, basename='all-user')

router.register(r'self/', SessionUserViewSet, basename='session-user')

urlpatterns = [
    path('', include(router.urls)),
    # path('self/detail/', SessionUserViewSet, name='session-user-detail'),
    # path('dashboard/',  dashboard,  name='dashboard'),
    # path('signin/',     register,   name='register'),
    # path('edit_user/',  edit,       name='edit'),
    # path('login/',      user_login, name='login'),
    # path('logout/',     user_logout,name='logout'),  
    # # Login API URLs
    # path('api/v1/signup/',      register_user_api,  name='api-signup'),
    # path('api/v1/login/',       user_login_api,     name='api-login'),
    # path('api/v1/logout/',      user_logout_api,    name='api-logout'),             #TokenRequired
    # path('api/v1/user-edit/',   edit_user_api,      name='api-user-edit'),         #TokenRequired
    # path('api/v1/current_user/',current_user_detail , 
    #                                                 name='current-user'), #TokenRequired
    # path('api/v1/user_profile/', get_userprofile ,  name='user-profile'),    #TokenRequired
    # path('api/v1/active_users/', get_active_users , name='active-user'),

]


