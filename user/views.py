# from django.shortcuts import render
# from django.http import HttpResponse
# from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.decorators import login_required
from django.contrib import messages
from rest_framework import viewsets
from rest_framework.views import APIView
from .models import User as The_User
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer, UserProfileSerializer
from rest_framework.response import Response
from rest_framework import status
# from .forms import LoginForm, UserRegistrationForm, UserEditForm
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.permissions import AllowAny , IsAuthenticated
# from rest_framework.decorators import api_view, permission_classes
# from rest_framework.response import Response
# from rest_framework.authtoken.models import Token #Token
# from rest_framework.decorators import authentication_classes, permission_classes



# API views
class UserViewSet(viewsets.ModelViewSet):
    queryset = The_User.objects.all()
    serializer_class = UserSerializer
    http_method_names = ['get', 'post', 'put', 'patch', 'delete', 'head', 'options', 'trace']

    def get_queryset(self):
        if self.request.method in ['GET']:
            return The_User.objects.filter(id=self.request.user.id)
        return super().get_queryset()

    def perform_update(self, serializer):
        # Update details of the session user
        serializer.save()

    def update(self, request, *args, **kwargs):
        # Ensure only the session user can be updated
        instance = self.get_object()
        if instance.id != request.user.id:
            return Response({"detail": "Cannot modify other user details"}, status=status.HTTP_403_FORBIDDEN)
        return super().update(request, *args, **kwargs)
    
# API views
class SessionUserViewSet(viewsets.ModelViewSet):
    queryset = The_User.objects.all()
    serializer_class = UserProfileSerializer



# ###############################################################################################################3

# @api_view(['POST'])
# def register_user_api(request):
#     if request.method == 'POST':
#         username = request.data.get('username')
#         password = request.data.get('password')
#         email = request.data.get('email')
#         # re_password = request.data.get('re_password')
        

#         if username and password: # and re_password:
#             # if password == re_password:
#             if User.objects.filter(username=username).exists():
#                 return Response('Username already exists')  # Return error if email already exists
#             else:
#                 user = User.objects.create_user(username=username.lower(), password=password,email=email.lower())
#                 if user:
#                     user_data = {
#                         'id': user.id,
#                         'username': user.username,
#                         'email': user.email,
#                         'first_name': user.first_name,
#                         'last_name': user.last_name,
#                         # Add more user-related fields if needed
#                     }
#                     return Response(user_data)
#                 else:
#                     return Response('Failed to register user')
#         # else:
#         #     return Response(f"Password does not match - 1st : {password}  2nd : {re_password}")
#         else:
#             return Response('Bad request')


# @api_view(['POST'])
# def user_login_api(request)-> {'id','username','token'}:
#     if request.method == 'POST':
#         username = request.data.get('username')
#         password = request.data.get('password')

#         if username and password:
#             user = authenticate(username=username, password=password)
#             if user is not None:
#                 if user.is_active:
#                     login(request, user)
#                     token, created = Token.objects.get_or_create(user=user)
#                     print(token)
#                     logged_in_detail = {
#                                         'id'        : user.id ,
#                                         'username'  : user.username,
#                                         # 'email'     : user.email,
#                                         'token'     : str(token) ,
#                                         }
#                     return Response(logged_in_detail)
#                 else:
#                     return Response('Disabled account')
#             else:
#                 return Response('Invalid login')
#         else:
#             return Response('Bad request')



# @api_view(['POST'])
# # @authentication_classes([TokenAuthentication])  # Ensure proper authentication class
# @permission_classes([IsAuthenticated])  # Ensure permission classes
# def user_logout_api(request):
#     user = request.user
#     if user.is_authenticated:  # Check if the user is authenticated
#         # Delete the user's token(s)
#         tk = Token.objects.filter(user=user)
#         print(tk)
#         Token.objects.filter(user=user).delete()
#         return Response('Logged out successfully')
#     else:
#         return Response('User not logged in')

# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def get_userprofile(request):
#     user_profile = request.user.userprofile
#     print(user_profile)

#     if user_profile:
#         serializer = UserProfileSerializer(user_profile)
#         return Response(serializer.data)
#     else:
#         return Response('UserProfile not found', status=404)
        
# @api_view(['GET'])
# @permission_classes([IsAuthenticated]) #Filtering <<
# def current_user_detail(request):
#     print('-----------------')
#     user = request.user
#     if user:
#         user_data = {
#             'id' : user.id ,
#             'username': user.username,
#             'email': user.email,
#             'first_name': user.first_name,
#             'last_name': user.last_name,
#             # Add more user-related fields if needed
#         }
        
#         return Response(user_data) 
#     else:
#         return Response('User not found')

# @api_view(['GET'])
# # @permission_classes([IsAdminUser])  # Only allow access to admin users
# def get_active_users(request):
#     # Fetch all users with a valid token
#     active_tokens = Token.objects.select_related('user').all()
#     active_users = [token.user for token in active_tokens]

#     user_data_list = []
#     for user in active_users:
#         user_data = {
#             'id': user.id,
#             'username': user.username,
#             'email': user.email,
#             'first_name': user.first_name,
#             'last_name': user.last_name,
#             'token': user.auth_token.key  # Access the token key
#         }
#         user_data_list.append(user_data)

#     return Response(user_data_list)


# @api_view(['PUT'])
# def edit_user_api(request):
#     if request.method == 'PUT':
#         user = request.user
#         new_username = request.data.get('username')
#         new_email = request.data.get('email')

#         if user and new_username and new_email:
#             user.username = new_username
#             user.email = new_email
#             user.save()
#             return Response('User details updated successfully', content_type="text/plain")
#         else:
#             return Response('Bad request', content_type="text/plain")



# ########################################################################################################################
# ########################################################################################################################
# ########################################################################################################################
# ########################################################################################################################

# # Views for user authentication and profile management
# def user_login(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             cd = form.cleaned_data
#             user = authenticate(request, username=cd['username'], password=cd['password'])
#             if user is not None:
#                 if user.is_active:
#                     login(request, user)
#                     return HttpResponse('Authenticated successfully')
#                 else:
#                     return HttpResponse('Disabled account')
#             else:
#                 return HttpResponse('Invalid login')
#     else:
#         form = LoginForm()
#     return render(request, 'account/login.html', {'form': form})

# @login_required
# def user_logout(request):
#     logout(request)
#     return HttpResponse('Logged out successfully')

# @login_required
# def dashboard(request):
#     return render(request, 'account/dashboard.html', {'section': 'dashboard'})

# def register(request):
#     if request.method == 'POST':
#         user_form = UserRegistrationForm(request.POST)
#         if user_form.is_valid():
#             new_user = user_form.save(commit=False)
#             new_user.set_password(user_form.cleaned_data['password'])
#             new_user.save()
#             # UserProfile.objects.create(user=new_user)
#             return render(request, 'account/register_done.html', {'new_user': new_user})
#     else:
#         user_form = UserRegistrationForm()
#     return render(request, 'account/register.html', {'user_form': user_form})

# @login_required
# def edit(request):
#     if request.method == 'POST':
#         user_form = UserEditForm(instance=request.user, data=request.POST)
#         # profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)
#         if user_form.is_valid(): # and profile_form.is_valid():
#             user_form.save()
#             # profile_form.save()
#             messages.success(request, 'Profile updated successfully')
#         else:
#             messages.error(request, 'Error updating your profile')
#     else:
#         user_form = UserEditForm(instance=request.user)
#         # profile_form = ProfileEditForm(instance=request.user.profile)
#     return render(request, 'account/edit.html', {'user_form': user_form, }) #'profile_form': profile_form}
