from django.db import models
from django.core.validators import RegexValidator
from datetime import datetime
from django.utils import timezone
print(timezone.now())


import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Create your models here.
class VisitorContact(models.Model):
    id = models.AutoField(primary_key=True)

    visitor_name    = models.CharField(max_length=100)
    email           = models.EmailField(null=True)
    phone_number    = models.CharField(max_length=10, 
                                   validators=[RegexValidator(regex   = '^[0-9]{10}$', 
                                                              message = 'Must be a 10-digit number', 
                                                              code    = 'invalid_number')],
                                   blank = True,
                                   null=True,
                                #    unique=True
                                   )
    country = models.CharField(max_length=100,null=True)
    state = models.CharField(max_length=100,null=True)

    def save(self, *args, **kwargs):
        super(VisitorContact, self).save(*args, **kwargs)  # Call the real save() method
        self.update_google_sheet()

    def update_google_sheet(self):
        # Define the scope of the application
        scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
        
        # Add the location of the JSON key file
        print('Reading the cred .. . .')
        creds = ServiceAccountCredentials.from_json_keyfile_name('contact_detail/medimanager-backend-6069ca28be90.json', scope)
        
        # Authorize the clientsheet 
        client = gspread.authorize(creds)
        
        # Open the spreadsheet by its title
        print('Opening the sheet .. . .')
        sheet = client.open('Visitors_ContactDetail').sheet1
        
        # Append a row to the sheet with new data
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Append a row to the sheet with new data including the timestamp
        sheet.append_row([
            self.visitor_name, self.email, self.phone_number, self.country, self.state, current_time
        ])

        return "Data entered to the sheet"

    