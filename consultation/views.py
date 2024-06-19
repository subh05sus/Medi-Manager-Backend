from django.conf import settings
from .models import Consultation
from appointment.models import Appointment
from .serializers import ConsultationSerializer
from rest_framework import viewsets # new
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import FileResponse
from rest_framework import viewsets, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
import pdfkit
from weasyprint import HTML, CSS

import logging
from jinja2 import Environment, FileSystemLoader

from .serializers import MetaConsultationSerializer , ConsultationSerializer , MinimalConsultationSerializer
from consultation_instruction.models import ConsultationInstruction

from rest_framework import viewsets
from consultation_instruction.models import ConsultationInstruction
from consultation_instruction.serializers import ConsultationInstructionSerializer
from consultation_investigation.models import ConsultationInvestigation
from consultation_investigation.serializers import ConsultationInvestigationSerializer
from consultation_symptom.models import ConsultationSymptom
from consultation_medicine.models import ConsultationMedicine

from .utils import ConsultationSymptomSerializer , ConsultationMedicineSerializer


from django.shortcuts import get_object_or_404
from saved_note.models import SavedNote
from prescription_setting.models import PrescriptionSetting
from prescription_setting.serializers import PrescriptionSettingSerializer
from user.models import User
from saved_note.serializers import SavedNoteSerializer
from test_report.models import TestReport
from .utils import GetFindingSerializer
from xhtml2pdf import pisa

# Create your views here.


def url_to_pdf(url, output_path, css_path=None):
    html = HTML(url)
    if css_path:
        css = CSS(css_path)
        html.write_pdf(output_path, stylesheets=[css])
    else:
        html.write_pdf(output_path)



class ConsultationViewSet(viewsets.ModelViewSet): 
    queryset = Consultation.objects.all()
    serializer_class = MinimalConsultationSerializer
    def get_queryset(self):
        doctor = self.request.user
        queryset = Consultation.objects.all()
        appointment_id = self.request.query_params.get('appointment_id')
        if appointment_id:
            try:
                consultation = Consultation.objects.get(appointment_id=appointment_id)
                queryset = queryset.filter(id=consultation.id)
            except Consultation.DoesNotExist:
                # Handle case where no consultation is found for the provided appointment ID
                queryset = Consultation.objects.none()
        else:
            queryset = queryset.filter(doctor_id=doctor.id)

        return queryset
    
class ConsultationFindingViewSet(viewsets.ModelViewSet): 
    queryset = Consultation.objects.all()
    serializer_class = GetFindingSerializer
    def get_queryset(self):
        queryset = Consultation.objects.all()
        appointment_id = self.request.query_params.get('appointment_id')
        
        if appointment_id:
            try:
                consultation = Consultation.objects.get(appointment_id=appointment_id)
                queryset = queryset.filter(id=consultation.id)
            except Consultation.DoesNotExist:
                # Handle case where no consultation is found for the provided appointment ID
                queryset = ConsultationMedicine.objects.none()
        return queryset.order_by('-id')

class ConsultationAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = MetaConsultationSerializer(data=request.data)
        if serializer.is_valid():
            consultation = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ConsultationCreateView(APIView):
    def post(self, request):
        print('----------------')
        appointment_id = request.data.get('appointment_id')
        if not appointment_id:
            return Response({"error": "Appointment ID is required"}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            appointment = Appointment.objects.get(id=appointment_id)
        except Appointment.DoesNotExist:
            # Handle case where Appointment does not exist
            return Response({"error": "Appointment not found"}, status=status.HTTP_404_NOT_FOUND)

        # Now use the Appointment instance to check/create Consultation
        consultation, created = Consultation.objects.get_or_create(
            appointment_id=appointment,  
            doctor_id = appointment.doctor_id.id,
            # created_by = appointment.doctor_id.id, 
        )
        finding = request.data.get('finding')
        
        if finding:
            consultation.finding = finding
            consultation.save()

            if request.data.get('is_saved'): 
                #if "is_saved" is present in as a key in the PAYLOAD
                doctor = User.objects.get(id=appointment.doctor_id.id)
                finding_note, _ = SavedNote.objects.get_or_create(
                                                        user_id     = doctor,
                                                        consultation_id=consultation,  
                                                        title       = finding,
                                                        note_type   = 'FND',
                                                        note        = finding)

        diagnosis = request.data.get('diagnosis')
        if diagnosis:
            print(diagnosis)
            consultation.diagnosis = diagnosis
            consultation.save()

            if request.data.get('is_saved'):
                doctor = User.objects.get(id=appointment.doctor_id.id)
                diagnosis_note, _ = SavedNote.objects.get_or_create(
                                                        user_id         = doctor,
                                                        consultation_id =consultation,  
                                                        title           = diagnosis,
                                                        note_type       = 'DGN',
                                                        note            = diagnosis)

        consultation_status  = request.data.get('status')
        if consultation_status:
            consultation.status = consultation_status #  CLOSED   = "CL"
            consultation.save()

        # Serialize the consultation instance
        serializer = ConsultationSerializer(consultation)
        return Response(serializer.data, status=status.HTTP_200_OK if not created else status.HTTP_201_CREATED)





class ConsultationPrescriptionViewSet(viewsets.ViewSet): 

    def list(self, request):
        appointment_id = self.request.query_params.get('appointment_id')
        if not appointment_id:
            return Response({'error': 'appointment_id parameter is required'}, status=status.HTTP_400_BAD_REQUEST)
        
        

        consultation    =   get_object_or_404(Consultation, appointment_id=appointment_id)
        consultation_id =   consultation.id

        consultation_instructions   = ConsultationInstruction.objects.filter(consultation_id=consultation_id)
        instructions_serializer     = ConsultationInstructionSerializer(consultation_instructions, many=True)
        consultation_investigations = ConsultationInvestigation.objects.filter(consultation_id=consultation_id)
        investigations_serializer   = ConsultationInvestigationSerializer(consultation_investigations, many=True)
        symptoms                = ConsultationSymptom.objects.filter(consultation_id=consultation_id)
        serialized_symptoms     = ConsultationSymptomSerializer(symptoms, many=True)
        medicines               = ConsultationMedicine.objects.filter(consultation_id=consultation_id)
        serialized_medicines    = ConsultationMedicineSerializer(medicines, many=True)

        
        response_data = {
            'consultation'  : consultation.id,
            'finding'       : consultation.finding,
            'diagnosis'     : consultation.diagnosis,
        
            'investigations': investigations_serializer.data ,
            'symptoms'      : serialized_symptoms.data,
            'medicines'     : serialized_medicines.data,
            'instructions'  : instructions_serializer.data ,
            # 'vital_signs' : vital_signs
        }

        return Response(response_data)


import pdfkit

from django.db import IntegrityError
from datetime import datetime
import os

class PrescriptionPrintView(viewsets.ViewSet):
    """
    Given an appointment ID, obtain all consultation workflow data,
    combine it with the doctor's custom prescription setting,
    and create a PDF.
    """

    def create(self, request):
        appointment_id = request.query_params.get('appointment_id')
        refer_doctor = request.data.get('refer_doctor')  # Get refer doctor from the request body
        follow_up_date = request.data.get('follow_up_date')  # Get follow-up date from the request body
        height = request.data.get('height')  # Get refer doctor from the request body
        weight = request.data.get('weight')  # Get follow-up date from the request body
        specialitization = request.data.get('specialitization')  # Get follow-up date from the request body
        height = height if height is not None else "NA"
        weight = weight if weight is not None else "NA"

        bmi = "NA" if weight == "NA" or height == "NA" else f"{round((float(weight) / ((float(height) / 100) ** 2)), 2)}"



        clinicName = request.data.get('clinicName')  
        clinicAddress = request.data.get('clinicAddress')  
        clinicPhone = request.data.get('clinicPhone')  
        timing = request.data.get('timing')  



        if not appointment_id:
            return Response({'error': 'appointment_id parameter is required'}, status=status.HTTP_400_BAD_REQUEST)
        appointment = get_object_or_404(Appointment, id=appointment_id)
        patient = appointment.patient_id
        doctor = appointment.doctor_id
        registration_number=doctor.registration_number
        doctor_specialization = doctor.qualification
        print(doctor.get_full_name())
        doctor_name = doctor.get_full_name()
        patient_info = {
            "full_name": patient.get_full_name(),
            "phone_number": patient.phone_number,
            "sex": patient.gender,
            "age": int(patient.age),
            "address": patient.address,
            # "height": appointment.height,
            # "weight": appointment.weight,
        }
        print("Patient info:",patient_info)
        print(patient.address)

        consultation = get_object_or_404(Consultation, appointment_id=appointment_id)
        consultation_id = consultation.id

        consultation_instructions = ConsultationInstruction.objects.filter(consultation_id=consultation_id)
        instructions_serializer = ConsultationInstructionSerializer(consultation_instructions, many=True)
        consultation_investigations = ConsultationInvestigation.objects.filter(consultation_id=consultation_id)
        investigations_serializer = ConsultationInvestigationSerializer(consultation_investigations, many=True)
        symptoms = ConsultationSymptom.objects.filter(consultation_id=consultation_id)
        serialized_symptoms = ConsultationSymptomSerializer(symptoms, many=True)
        medicines = ConsultationMedicine.objects.filter(consultation_id=consultation_id)
        serialized_medicines = ConsultationMedicineSerializer(medicines, many=True)
        prescription_setting = PrescriptionSetting.objects.filter(doctor_id=doctor)
        serialized_prescription_setting = PrescriptionSettingSerializer(prescription_setting, many=True)
        data = {

            'consultation': consultation.id,
            'finding': consultation.finding,
            'diagnosis': consultation.diagnosis,
            'investigations': investigations_serializer.data,
            'symptoms': serialized_symptoms.data,
            'medicines': serialized_medicines.data,
            'instructions': instructions_serializer.data,
        }
        patient_vitals = [
            {'height': 165},
            {'height': 165},
            {'height': 165},
        ]
        env = Environment(loader=FileSystemLoader('consultation/prescription_templates'))
        print(data['symptoms'])

        if not prescription_setting:
            template = env.get_template('template2.html')
            html_output = template.render(
                patient_id = appointment_id,
                patient_name = patient_info["full_name"],
                age_sex = f"{str(int(patient_info['age']))} - {patient_info['sex']}",
                date_time = datetime.now(),
                mobile_no = patient_info['phone_number'],
                address = patient_info['address'],
                doctor_name = doctor_name,
                refer_to=refer_doctor, 
                follow_up_date=follow_up_date, 
                patient_weight = weight,
                patient_height = height,
                specialitization= specialitization,
                doctor_specialization=doctor_specialization,
                registration_number=registration_number,
                # bmi = "20",
                # bmi = f"{round((float(weight)/((float(height)/100)**2)), 2)}",
                bmi = bmi,
                symptoms=[dict(item) for item in data['symptoms']],
                finding=consultation.finding,
                diagnosis=consultation.diagnosis,
                medicines=[dict(item) for item in data['medicines']],
                instructions=[dict(item) for item in data['instructions']],

                clinicName=clinicName,
                clinicAddress=clinicAddress,
                clinicPhone=clinicPhone,
                timing=timing,
            )
        else:
            doctor_rx_conf = serialized_prescription_setting.data[0]
            template = env.get_template('template2.html')
            html_output = template.render(
                symptoms=[dict(item) for item in data['symptoms']],
                finding=consultation.finding,
                diagnosis=consultation.diagnosis,
                medicines=[dict(item) for item in data['medicines']],
                instructions=[dict(item) for item in data['instructions']],
                patient_details=patient_info,
                doctor_prescription_settings=doctor_rx_conf,
                vital_signs=patient_vitals
            )
        filled_html_file_path = 'consultation/prescription_templates/filled_html.html'
        with open(filled_html_file_path, 'w') as file:
            file.write(html_output)

        try:
            # # Update the path to the wkhtmltopdf executable
            # # config = pdfkit.configuration(wkhtmltopdf='C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe')  # Update the path as necessary

            # pdf = pdfkit.from_string(html_output, False)
            
            # # Save the PDF to the Downloads folder
            # downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")
            # downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")
            # pdf_file_path = os.path.join(downloads_path, f'prescription_{appointment_id}.pdf')

            # with open(pdf_file_path, 'wb') as f:
            #     f.write(pdf)
            
            
            # # HTML(filled_html_file_path).write_pdf("examplee.pdf")
            # url_to_pdf(filled_html_file_path, f"prescriptions/prescription_{appointment_id}.pdf", "consultation/prescription_templates/pdf.css")


            # response = HttpResponse(pdf, content_type='application/pdf')
            # response['Content-Disposition'] = f'attachment; filename="prescription_{appointment_id}.pdf"'
            # return response
             
            url_to_pdf(filled_html_file_path, f"prescriptions/prescription_{appointment_id}.pdf", "consultation/prescription_templates/pdf.css")
            with open(f"prescriptions/prescription_{appointment_id}.pdf", 'rb') as pdf_file:
                response = HttpResponse(pdf_file.read(), content_type='application/pdf')
                response['Content-Disposition'] = f'attachment; filename="prescription_{appointment_id}.pdf"'
                print(response)
                return response
            
        except Exception as e:
            logging.error(f"An error occurred when generating the PDF: {e}")
            return Response({'error': 'An error occurred when generating the PDF'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


def get_prescription_pdf(request, appointment_id):
    pdf_path = os.path.join(settings.BASE_DIR, f'prescriptions\prescription_{appointment_id}.pdf')
    if os.path.exists(pdf_path):
        with open(pdf_path, 'rb') as pdf_file:
            response = HttpResponse(pdf_file.read(), content_type='application/pdf')
            response['Content-Disposition'] = f'attachment; filename="prescription_{appointment_id}.pdf"'
            return response
    else:
        return HttpResponse("No Records Found", status=404)