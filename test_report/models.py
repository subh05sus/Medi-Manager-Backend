from django.db import models
from user.models  import User
from appointment.models import Appointment

import os
from django.core.files import File
from django.core.files.base import ContentFile

# Create your models here.

class TestReport(models.Model):
    id                  = models.AutoField(primary_key=True)
    user_id             = models.ForeignKey(User, on_delete=models.PROTECT)
    appointment_id      = models.ForeignKey(Appointment, 
                                            on_delete=models.PROTECT,
                                            blank=True)
    document_label      = models.CharField(max_length = 100, blank=True,null=True)
    # ^ This upper one will be used to store name of the Document
    document_path       = models.FileField(upload_to='test_reports',blank=True)

    def __str__(self):
        return f'Test Report: {self.document_label} (Appointment ID: {self.appointment_id_id})'
    class Meta:
        unique_together = ['user_id', 'appointment_id','document_label']

    def save_pdf(self, pdf_content):
        # Save PDF file to a specific location
        file_path = os.path.join('document', 'pdf_reports', f'report_{self.id}.pdf') 
        with open(file_path, 'wb') as f:
            f.write(pdf_content)

        # Save the document path to the model
        self.document_path = file_path
        self.save()

    def save_rx_pdf(self, pdf_content):
        try:
            if not self.appointment_id:
                raise ValueError("Appointment ID is required to save the PDF.")

            file_name = f'Rx_{self.appointment_id.id}.pdf'  # Using appointment_id from self

            pdf_file = ContentFile(pdf_content)

            # Save the file to the FileField
            self.document_path.save(file_name, pdf_file, save=True)

            # Save the document label and appointment_id
            self.document_label = "prescription"
            self.save()

            # Return the full path to the saved file
            return os.path.join(self.document_path.path, file_name)
        except Exception as e:
            # Handle exceptions, e.g., log the error
            print(f"Error saving PDF file: {e}")
            return None
