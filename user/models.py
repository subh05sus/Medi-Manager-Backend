from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from user_role_mapping.models import UserRoleMapping
from role.models import Role
from enum import Enum

class UserAccountManager(BaseUserManager):
    def create_user(self, phone_number, password=None, **extra_fields):
        if not phone_number:
            raise ValueError('User must have an Phone number.')

        phone_number = self.normalize_email(phone_number)
        print('New User Detail : ', extra_fields)
        
        user = self.model(phone_number = phone_number, **extra_fields)
        user.set_password(password)
        user.save()

        if extra_fields.get('is_doctor'):
            doctor_role_id , _ = Role.objects.get_or_create(name='Doctor')
            user.is_doctor = True
            user.save()
            role_mapping , _ = UserRoleMapping.objects.get_or_create(
                user_id= user, 
                role_id = doctor_role_id )
            print("Role Mapped for Doctor",role_mapping)

        elif extra_fields.get('is_receptionist'):
            receptionist_role_id , _ = Role.objects.get_or_create(name='Receptionist')
            user.is_doctor = True
            user.save()
            role_mapping , _ = UserRoleMapping.objects.get_or_create(
                user_id= user, 
                role_id = receptionist_role_id )
            print("Role mapped for Receptionist", role_mapping)
        
        return user
    
    def create_superuser(self, phone_number, password=None, **extra_fields):
        """
        Create and return a superuser with an email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(phone_number, password, **extra_fields)

class GENDER_TYPES(Enum):
    MALE     = "ML"
    FEMALE    = "FL"
    OTHER     = "OT"
 

class User(AbstractBaseUser, PermissionsMixin):
    id  = models.AutoField(primary_key=True) 
    # user_id   = models.OneToOneField(User, on_delete=models.CASCADE)# ,to_field='username')
    # Email or Username will be entered from Front-End
    first_name  = models.CharField(max_length=50 , blank = True)
    last_name   = models.CharField(max_length=50,  blank = True)
    email       = models.EmailField(blank=True,null=True) #,unique=True)
    phone_number= models.CharField(max_length=10, 
                                   validators=[RegexValidator(regex   = '^[0-9]{10}$', 
                                                              message = 'Must be a 10-digit number', 
                                                              code    = 'invalid_number')],
                                   blank = True,
                                   unique=True)
    
    aadhar      = models.CharField(unique = True, 
                                    max_length=18,
                                    null=True,
                                    blank=True)
    # This will be modified to any Unique Num from ID card for citizens of other countries
    # Or We will give a drop down to select what kind of ID they are using 
    # Example - Voter ID , Aadhar , PAN etc

    address     = models.CharField(max_length=500,blank=True)
    postal_code = models.CharField(max_length=6 , 
                                   blank = True)

    created     = models.DateTimeField(auto_now_add=True)
    updated     = models.DateTimeField(blank=True, null=True)
    profile_pic = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    aadhar_pic  = models.ImageField(upload_to='aadhar_cards/', blank=True, null=True)
    

    date_joined = models.DateTimeField(default=timezone.now, editable=False)
    last_login  = models.DateTimeField(blank=True,null=True)

    is_active           =   models.BooleanField(default=True)
    is_staff            =   models.BooleanField(default=False)
    #Special --
    is_doctor           =  models.BooleanField(default=False) 
    is_receptionist     =  models.BooleanField(default=False) 

    registration_number      = models.CharField(unique = True, 
                                    max_length=18,
                                    null=True,
                                    blank=True)
    qualification      = models.CharField(max_length=250,blank=True,null=True)
    
    # fee                 =  models.CharField(max_length=4 ,    blank = True)
    gender              =  models.CharField(
                                        max_length  =   2,
                                        choices     =   [(gender.value, gender.name) for gender in GENDER_TYPES],
                                        default     =   'ML', # For Initial Appointment
                                    ) 
    age = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    date_of_birth = models.DateField(null=True)
    # new_user = models.BooleanField(default=True)

    # New Consultation fee , FollowUp, 

    objects = UserAccountManager()

    USERNAME_FIELD  = 'phone_number'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def __str__(self):
        return self.first_name
    
    def save(self, *args, **kwargs):
        if not self.id:  # If the user is being created for the first time
            self.date_joined = timezone.now()
        super().save(*args, **kwargs)


# from django.contrib.auth.signals import user_logged_in
# from django.dispatch import receiver

# @receiver(user_logged_in)
# def set_new_user_false(sender, request, user, **kwargs):
#     if user.new_user:  # Check if the flag is True
#         user.new_user = False
#         user.save()