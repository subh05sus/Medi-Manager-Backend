# MediManager-Backend-Auth

> First version Deployment to be done on Ram Navami
> April 17 - 2024

## Step1 

> Download this repo (or git clone it) to your device

> Delete Build folder present inside this Repo


![image](https://github.com/ehr66777/1st_deployment/assets/151137936/66f2b87e-4588-4413-a196-79b2704b16c3)


> Build react App - npm run build

> Copy and Paste the Build Folder (which contain static file)

> you can run by runserver
---




## ^_^




## Getting this repo

Create a file first in your pc by 

```
mkdir medimanager && cd medimanager
```


Copy and paste the following in your terminal while inside the "medimanager" file

```
git clone git@github.com:ehr66777/Medi-Manager-Backend.git
```

### Activating the virtual environment
The virtual environment in created as .env
activate that by running the following command :
```
source .env/bin/activate
```

or delete the .env file and recreate again

```
python3 -m venv .env
```
And then activate it again

### Installing dependencies

The requirements.txt file is added to this repo 
run it by running this :

```
pip install -r requirements.txt
```
## Adding Sample Data for Test Purposes

Adding the Specialization and User which will be required to create appointments
```
python3 manage.py load_specialization
                  load_user
                  load_appointment
                  &
                  load_medicine
                  load_symptom
                  &
                  load_investigation <<< NEW >>>
```



For adding some commonly used Medicines -- use this :


# Added Dummy users

```json
User_ID: 1, Email: superadmin@gmail.com
User_ID: 2, Email: patient1@example.com
User_ID: 3, Email: patient2@example.com
User_ID: 4, Email: patient3@example.com
User_ID: 5, Email: patient4@example.com
User_ID: 6, Email: patient5@example.com
User_ID: 7, Email: patient6@example.com
User_ID: 8, Email: patient7@example.com
User_ID: 9, Email: doctor1@example.com  << DOCTOR >>
User_ID: 10, Email: doctor2@example.com << DOCTOR >>
User_ID: 11, Email: doctor3@example.com << DOCTOR >>
```

# Login and Token Authentication from React Side :

## Registration/Sign-up Using Djoser

Just for now , email and password are required params for this SignUp process
(First Name and LastName , you can skip and empty string will be passed as default value.) <<NOT RECOMMENDED>>

The endpoint  to sign-up is here :
> POST : /auth/users/

```json
{
  "phone_number": "8888772200",
  "first_name": "first-name",
  "last_name": "last-name",
  "password": 'PASSWORD_PLACEHOLDER',
   "is_doctor" : true , << Send only if you want the user to enrolled as a Doctor - otherwise don't add this field to Payload
   "specialization_name" "Specialization name no 1" >>> Can add their specialization directly to profile
}
```
> Modified on 18 April to accomodate Specialization
> **GET** : api/v1/specialization/  

> ^ Use the upper one to bring lists of Specialization

## Log-in 

The Login request in react is here >>> 
PATH : auth/jwt/create

```json


{"email": "patient1@email.com", "password": "bigbang13"}


```

The Login output will be containing the "JWT-TOKEN" and coming like this >>>

```json
{
  "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcwNjY5NTUwNiwiaWF0IjoxNzA2NjA5MTA2LCJqdGkiOiJiOTAwNWUxNTg5ZTY0NmJjOWMyYmE1NTIxYTgyYTEyMiIsInVzZXJfaWQiOjZ9.h8DgGCTjgNkuZWAjrLekSv9gyBsNdKZ3Um2d6uT5K4M",
  "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzA2NjEyNzA2LCJpYXQiOjE3MDY2MDkxMDYsImp0aSI6ImY3YWVjNDdlZWJhODRjZTA5OGNjMjQwZGRlZWM1OGZkIiwidXNlcl9pZCI6Nn0._av7Umn3pJbtHIY1Usj7ujyh4EiLnHJKXHSVVZV-yao"
}
```

## Verifying JWT Token

- The Token coming from login-response will be used in the Payload now : "Token place_your_token_here"
```json
{
  "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzA2NjEyNzA2LCJpYXQiOjE3MDY2MDkxMDYsImp0aSI6ImY3YWVjNDdlZWJhODRjZTA5OGNjMjQwZGRlZWM1OGZkIiwidXNlcl9pZCI6Nn0._av7Umn3pJbtHIY1Usj7ujyh4EiLnHJKXHSVVZV-yao"
}
```

The output for this will be coming like this 200 RESPONSE

- The 'id' will be necessary we have to filer the alloted appointments for a user (Doctor).

```json
{ }
```

## Refreshing JWT Token

- The Refresh Token coming from login-response will be used in the Payload now : "place_your_token_here"
```node.js
const http = require("http");

const options = {
  "method": "POST",
  "hostname": "127.0.0.1",
  "port": "8000",
  "path": "/auth/jwt/refresh/",
  "headers": {
    "Accept": "*/*",
    "Content-Type": "application/json"
  }
};

const req = http.request(options, function (res) {
  const chunks = [];

  res.on("data", function (chunk) {
    chunks.push(chunk);
  });

  res.on("end", function () {
    const body = Buffer.concat(chunks);
    console.log(body.toString());
  });
});

req.write(JSON.stringify({
  refresh: 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcwNjY5NTUwNiwiaWF0IjoxNzA2NjA5MTA2LCJqdGkiOiJiOTAwNWUxNTg5ZTY0NmJjOWMyYmE1NTIxYTgyYTEyMiIsInVzZXJfaWQiOjZ9.h8DgGCTjgNkuZWAjrLekSv9gyBsNdKZ3Um2d6uT5K4M'
}));
req.end();

```

The output for this will be coming like this 200 RESPONSE

- The 'id' will be necessary we have to filer the alloted appointments for a user (Doctor).

```json

{
  "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzA2NjEzNDcyLCJpYXQiOjE3MDY2MDkxMDYsImp0aSI6ImUzYjI0MGM3YzgyMjRkNDViMjNjY2NjMThhMmFiYWE4IiwidXNlcl9pZCI6Nn0.Wd4erYmUnzTBbrrp6qM-2K2rlsCR-tAaBuop8ik9chs"
}

```
## Getting Current Session User 

The Login request in react is here >>> 
> POST : auth/users/me

> No need to pass anything in PAYLOAD

The output response will be containing the "user-id" , "full name" and coming like this >>>

```json
{
  "id": 38,
  "full_name": "Narendra Modi",
  "first_name": "Narendra",
  "last_name": "Modi",
  "profile_pic": null,
  "gender": "ML",
  "age": null,
  "aadhar": null,
  "registration_number": null,
  "address": "",
  "postal_code": "",
  "qualification": null,
  "is_doctor": true,
  "is_receptionist": false,
  "phone_number": "9999999902",
  "specializations": [
    {
      "specialization_name": "Political Leadership no 1"
    }
  ]
}
```
## Fetching Medicine Data using JWT token as auth-object

The format is over here :
> Authorization: JWT <token>

```json

{
  "token": "JWT eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzA2NjEzNDcyLCJpYXQiOjE3MDY2MDkxMDYsImp0aSI6ImUzYjI0MGM3YzgyMjRkNDViMjNjY2NjMThhMmFiYWE4IiwidXNlcl9pZCI6Nn0.Wd4erYmUnzTBbrrp6qM-2K2rlsCR-tAaBuop8ik9chs"
}
```



## Getting Session User Specific Appointments ( Doctor == Session User)
- This endpoint will work for doctor and Receptionist as well 
    - For Doctor it will fetch the appointment booked against him/her
    - for Receptionist , it will fetch all appointments booked with the doctor connected with him/her
- The API End point to use the session user detail to get appointment for him is here :

> GET : /api/v1/appointment/doctor_specific/?*type*=IA&*status*=CR&*appointment_datetime*=2024-03-22

The Upper one is filtering all appointment where TYPE : INITIAL_APPOINTMENT , STATUS : CREATED , and APPOINTMENT_DATETIME : 2024-03-22 .

The following options ofr Appointment_type and status are available :
```Python
class APPOINTMENT_STATUSES(Enum):
    CREATED     = "CR"
    IN_PROGRESS = "IP"
    CANCELLED   = "CN"
    POSTPONED   = "PP"
    CLOSED      = "CL"
    RESCHEDULED = "RC"
    
class APPOINTMENT_TYPES(Enum):
    INITIAL     = "IA"
    FOLLOWUP    = "FA"
    CLOSED      = "CA"
```

> GET : /api/v1/appointment/doctor_specific/

This Upper URL where no datetime is provided , will fetch all Appointments for today's Date

```Python
if appointment_datetime is None:
            # If no date is provided, filter against today's date
            today = datetime.now().date()
            return Appointment.objects.filter(doctor_id=user.id, appointment_datetime__date=today)
```


The output for this will be coming like this 200 RESPONSE

- Use the appointments - List and iterate through it to show all the appointments detail.

```json

{
  "user": {
    "id": 8,
    "full_name": "Buddhiraj Sahu",
  },

  "appointments": [
    {
      "id": 4,
      "type": "IA",
      "status": "CR",
      "patient_id": 25,
      "doctor_id": 8,
      "patient_name": "Patient1 Pt1",
      "patient_age": "20-8-28",
      "patient_gender": "ML"
    },
    {
      "id": 5,
      "type": "IA",
      "status": "CR",
      "patient_id": 2,
      "doctor_id": 8,
      "patient_name": "Patient2 Pt2_Lastname",
      "patient_age": "25-0-7",
      "patient_gender": "ML"
    },
    {
      "id": 6,
      "type": "IA",
      "status": "CR",
      "patient_id": 25,
      "doctor_id": 8,
      "patient_name": "Atiprad-patient lm",
      "patient_age": "20-8-28",
      "patient_gender": "ML"
    },

  ]
}

```
## Creating Consultation  

> *GET/POST* : /api/v1/consultation/


```json

 {
    "appointment_id": 3,
    "doctor_id"     : 9,
    "finding"       : "Big text field 00-0---------------------------099999",
    "diagnosis"     : "Big text field 00-0---------------------------099999"
  }
```

The output for this will be coming like this 200 RESPONSE

- Use the Consultation-id to create other 

```json

{
  "id": 3,
  "appointment_id": 3,
  "created"   : "2024-02-09T11:37:24.506494Z",
  "status"    : "CR",
  "doctor_id" : 9,
  "updated"   : "2024-02-09T11:37:24.506577Z",
  "updated_by": "",
  "fee"       : null,
  "fee_paid"  : false,
  "next_appointment": null,
  "finding"   : "Big text field 00-0---------------------------099999",
  "diagnosis" : "Big text field 00-0---------------------------099999"
}

```

## Checking and Creating Consultation via appointment-id


When the Doctor presses the < New Consultation> Button for a single appointment in Appointment-Queue View,
This API will be triggered which ,

- will check for existing consultation for given appointment_id
- if exist it will return that Consultation instance
else,
- it will create a fresh new Consultation using this appointment id and fetching the doctor_id from that appointment

> *GET* : /api/v1/consultation/create/


> Can also be used to update the Consultation status
> *POST* : /api/v1/consultation/create/ 

- I assume that both Finding and Diagnosis will not be passed at the same time.

```json
{
  "appointment_id": 5,
  "finding": "Text from Findings",        << OPTIONAL 
  "diagnosis": "New diagnosis --- TEXT",  << OPTIONAL
  "is_saved" : true                 # Look into the Python code below for more in-depth
  "status": "CL"    << WILL BE USED in case of Updating Value : )
  
}
```

> Note : the key = "is_saved" irrespective of it's value need to be sent in the PAYLOAD
> in order to save the findings or diagnosis to --> SAVED-NOTE

The Code sample is here :

Inspired by @Atiprad
Date : 22-03-2024


```Python

if request.data.get('is_saved'): #if "is_saved" is present in as a key in the PAYLOAD
                doctor = User.objects.get(id=appointment.doctor_id.id)
                finding_note, _ = SavedNote.objects.get_or_create(
                                                        user_id     = doctor,
                                                        consultation_id=consultation,  
                                                        title       = finding,
                                                        note_type   = 'FND',
                                                        note        = finding)

```

The Consultation-fields like "findings" and "diagnosis" can be pushed if needed in the same payload (mentioned above)
> Read this Python code if you want to get an gist of what is going inside the BOX :

```Python

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
  diagnosis = request.data.get('diagnosis')
  if diagnosis:
      consultation.diagnosis = diagnosis
      consultation.save()

```


The output for this will be coming like this 200 RESPONSE

- Use the Consultation-id to create other 

```json

{
  "id": 9,
  "appointment_id": 5,
  "status": "CR",
  "doctor_id": 10,    << Coming from appointment.doctor_id
  "updated": "2024-02-23T09:58:36.393799Z",
  "updated_by": "",
  "created_by": "10", << Coming from doctor_id
  "created": "2024-02-23T09:58:36.393710Z",
  "fee": null,
  "fee_paid": false,
  "next_appointment": null,
  "finding": null,
  "diagnosis": null
}

```

## Posting Consultation-Symptom 


> *POST* : /api/v1/consultation-symptom/add/
This Upper one will be used to PUSH complex data
> *GET* : /consultation-symptom/?consultation_id=1
This will be the URL pattern to get Consultation-Symptoms by filtering through consultation_id

The Payload Structure is here

```json
{
  "appointment_id": 10, <<< PUSH Appointment ID or Consultation ID
  "consultation_id": 2,
  "symptoms": [
    {
      "symptom_name": "Symptom99",
      "duration": "5 days",
      "severity": "MLD"
    },
    {
      "symptom_name": "fever",
      "duration": "3 days",
      "severity": "MED"
    },
    {
      "symptom_name": "Cold",
      "duration": "2 days",
      "severity": "SEV"
    }
  ]
}


```

The output for this will be coming like this 200 RESPONSE

- Use the appointments - List and iterate through it to show all the appointments detail.

```json

{
  "message": "Consultation symptoms added successfully."
}

```

- Filtering and getting a list of consultation-symptoms instances will come in this form :

```json

[
  {
    "id": 82,
    "consultation_id": 2,
    "symptom_id": 122,
    "duration": "3 days",
    "severity": "MED"
  },
  {
    "id": 83,
    "consultation_id": 2,
    "symptom_id": 7,
    "duration": "2 days",
    "severity": "SEV"
  }
]

```



## Posting Consultation-Medicine

> *GET* : /api/v1/consultation-medicine/add/

This Upper one will be used to PUSH list of medicine for Consultation-Medicine


The PAYLOAD Data will be in this format >>>

```json

{
  "appointment_id": 10, <<< PUSH Appointment ID or Consultation ID
  "consultation_id": 2,
  "medicines": [
    {
      "medicine_name": "MeDCine23",
      "dosage": "0.5",
      "timing": "Morning",   #"MN" #Modified to fill Free Text on 16th April as per @Kaibalya
      "modality": "AF", # 
      "duration": "5 days",
      "instruction": "Take after food"
    },
    {
      "medicine_name": "Ibuprofen",
      "dosage": "1.0",
      "timing": "EV",
      "modality": "BF",
      "duration": "3 days",
      "instruction": "Take before food"
    }
  ]
}


```

The output for this will be coming like this 200 RESPONSE


```json

{ }

```

## Posting Consultation-Investigation


> *GET* : /api/v1/consultation-investigation/add/
This Upper one will be used to PUSH complex data

> *GET* : /api/v1/consultation-investigation/?consultation_id=3 
This will be the URL pattern to get Consultation-Symptoms by filtering through consultation_id

The PAYLOAD Data will be in this format >>>

```json

{
  "appointment_id"  : 10, <<< PUSH Appointment ID or Consultation ID
  "consultation_id" : 3, <<< PLACEHOLDER_CONSULTATION_ID
  "investigations"  : [
    {
      "investigation_name": "Blood Glucose Test",
      "note"  : "ye karwa ke laana re baba!!"
    },
    {
      "investigation_name": "Complete Blood Count (CBC)",
      "note"  : "Dummy long text -----Yes!!"
    }
  ]
}

```

The output for this will be coming like this 200 RESPONSE


```json

{ }

```

## Posting Consultation-Instruction


> *POST* : /api/v1/consultation-instruction/
This Upper one will be used to PUSH  data
> *GET* : /consultation-instruction/?consultation_id=1
This will be the URL pattern to get Consultation-Symptoms by filtering through consultation_id

The PAYLOAD Data will be in this format >>>

```json
{
  "consultation_id": 3, <<< PLACEHOLDER_CONSULTATION_ID
   "instruction": "Take one tablet of [medicine_name] orally, with water, [timing]. Avoid taking on an empty stomach. If you miss a dose, take it as soon as you remember, but do not double the dose if it's almost time for the next dose"
}
```

The output for this will be coming like this -> 200 RESPONSE


```json

{
  "id": 2,
  "consultation_id": 2,
  "instruction": "Take one tablet of [medicine_name] orally, with water, [timing]. Avoid taking on an empty stomach. If you miss a dose, take it as soon as you remember, but do not double the dose if it's almost time for the next dose"
}

```

#### For Accessing Consultation-Instruction using Appointment-ID
To Get the Corresponding instance using appointment_id use below endpoint
> *GET* : /api/v1/consultation-instruction/?appointment_id=11

Nothing to give in the PAYLOAD
---
The End Point is : 
> *GET* : /api/v1/consultation-instruction/add/

- Add appointment_id or consultation_id , not both (NOTE)
The Payload format will be :-

```json
{
  "appointment_id"  : 10, <<< PUSH Appointment ID 
  "consultation_id" : 3, <<< PLACEHOLDER_CONSULTATION_ID
   "instruction"    : "Take one tablet of [medicine_name] orally, with water, [timing]. Avoid taking on an empty stomach. If you miss a dose, take it as soon as you remember, but do not double the dose if it's almost time for the next dose"
}
```

The Output will be this --
```json
{
  "instruction": "Take one tablet of [medicine_name] orally, with water, [timing]. Avoid taking on an empty stomach. If you miss a dose, take it as soon as you....."
}
```

# The REAL DEAL <<< COMPLEX-DATA-INSERTION>>>
## Posting Consultation-BULK Mode

- Hre we are posting 
a. Appointment-ID
b. List of Symptoms
c. Finding and Diagnosis



> *GET* : /api/v1/consultation/
This Upper one will be used to PUSH complex data
> *POST* : /api/v1/consultation/add/
This will be the URL pattern to get Consultation-Symptoms by filtering through consultation_id

The json payload for this will be having this format



```json

{
  "appointment_id": 9,
  "created_by": 6,
  "doctor_id": 6, << MANDATORY>>
  "symptoms": [
    {
      "symptom_name": "Headache",
      "duration": "5 days",
      "severity": "MED"
    },
    {
      "symptom_name": "SYMp1",
      "duration": "3 days",
      "severity": "SEV"
    },
    {
      "symptom_name": "SympTom2",
      "duration": "3 days",
      "severity": "MLD"
    }
  ],
  "finding": "Patient exhibits symptoms consistent with viral infection.",
  "diagnosis": "Suspected viral gastroenteritis."
}


```

- Filtering and getting a list of consultation-symptoms instances will come in this form :

```json

{
  "appointment_id": 3,
  "finding": "Patient exhibits symptoms consistent with viral infection.",
  "diagnosis": "Suspected viral gastroenteritis.",
  "consultation_id": 27,
  "symptoms": [
    {
      "symptom_name": "Headache",
      "duration": "5 days",
      "severity": "MED"
    },
    {
      "symptom_name": "Fever",
      "duration": "3 days",
      "severity": "SEV"
    },
    {
      "symptom_name": "Nausea",
      "duration": "2 days",
      "severity": "MLD"
    }
  ]
}

```

# Get All Consultation-Workflow Data via Appointment-id

## Consultation-Finding+Diagnosis
For Consultation-( Findings + Diagnosis ) for a particular consultation related to an appointment obj
refer this below >>
> *GET* : /api/v1/consultation/?appointment_id=1

#### Getting All Saved findings
> *GET* : /api/v1/consultation/query/
> ^ Use the upper one to get session-user speicfic all findings+diagnostics notes.
NOTE : The recent ones will be coming on top - as suggested by @Atiprad

```json
[
  {
    "id": 2,
    "finding": "New text",
    "diagnosis": "Simple Dignosis False"
  },
  {
    "id": 1,
    "finding": "Nothing in finding yet.",
    "diagnosis": "Ye hai ------ Diagnosis."
  }
]

```


The Output will come as a list of single Dicts - refer this below >>
```json

[
  {
    "id"            : 1,
    "appointment_id": 1,
    "status"        : "CR",
    "doctor_id"     : 1,
    "fee"           : "200.00",
    "fee_paid"      : true,
    "next_appointment": "2024-03-18T06:26:59Z",
    "finding"       : "Nothing in finding yet.",
    "diagnosis"     : "Ye hai ----------------------- Diagnosis."
  }
]

```
## Consultation-Symptoms

For Consultation-Symptoms for a particular consultation related to an appointment obj
refer this below >>
> *GET* : /api/v1/consultation-symptom/?appointment_id=10

The Output will come as a list of such Dicts - refer this below >>
```json
  {
    "id"              : 7,
    "consultation_id" : 10,
    "symptom_id"      : 1,
     "symptom_name"   : "Symptomp1",
    "duration"        : "5 days",
    "severity"        : "MLD" 
  }
```
## Consultation-Medicines
For Consultation-Medicine for a particular consultation related to an appointment obj
refer this below >>
> *GET* :  /api/v1/consultation-medicine/?appointment_id=10

The Output will come as a list of such Dicts
```json
  {
    "id"              : 1,
    "medicine_name"   : "Paracetamol",
    "medicine_id"     : 1,
    "medicine_dosage" : "2.0",
    "medicine_timing" : "MN",
    "medicine_modality"   : "AF",
    "medicine_duration"   : "1",
    "medicine_instruction": "None for now."
  }
```
## Consultation-Investigations
For Consultation-Investigation for a particular consultation related to an appointment obj
refer this below >>
> *GET* : /api/v1/consultation-investigation/?appointment_id=10

The Output will come as a list of such Dicts
```json
{
    "id"    : 1,
    "investigation_id"    : 1,
    "investigation_name"  : "Blood Glucose Test",
    "note"  : "Note for Blood Glucose test."
  },
```
----

## Consultation-Instructions
For Consultation-Instructions for a particular consultation related to an appointment obj
refer this below >>
> *GET* : /api/v1/consultation-instruction/?appointment_id=1

The Output will come as a list of such Dicts
```json
  {
    "id": 1,
    "consultation_id": 1,
    "instruction": "Instruction ye hai bhai ----------------------------------------- Instruction."
  }
```
----

## Getting Symptom-Fingerprint of a Consultation  

> *GET* : /api/v1/consultation-symptom/?appointment_id=10&fingerprint
This upper URL will be used to produce  the unique fingerprint for the JSON of consultation-symptoms given an appointment-id

This will also be sent to be stored in a Consultation model field 

The response will come like this
```json
{
  "symptom_fingerprint": "7ff59e708eda2a55bd0490a25f3821abce52b9d37173e0cf691d44803fe2f1f5"
}
```


## Saving Finding-Dignosis Note 
- Date - 29-02-2024

> *POST* : /api/v1/saved-note/add/
This Upper one will be used to Save a selected note (BOOKMARK FUNCTION)


The PAYLOAD Data will be in this format >>>

```Python
#if blank or no Note_title is sent from frontend , by default it will use the "note" in its place
if note_title is None:
                note_title = note_body
```

```json
{
  "user_id"       : 2,          << if not present session-user.id will be used
  "appointment_id": 20,         << Mandatory
  "note_type"     : "DGN",      << Note : "DGN" - Dignosis & "FND" - Finding (default value)
  "title"         : "Note Title 1", << 
  "note"          : "Note ------------------------- Note"
}
```
---

> *GET* : /api/v1/saved-note/?note_type=FND

This will be the URL pattern to get Saved Notes by filtering through Note Type = FN/DGN
And also, it will *filter using user_id = SESSION-USER*


> *GET* : /api/v1/saved-note/?appointment_id=1

This will be the URL pattern to get Saved Notes by filtering through appointment_id

The output for filtering with appointment_id will be coming like this -> 200 RESPONSE


```json
[
  {
    "id"        : 5,
    "user_id"   : 2,
    "consultation_id": 18,
    "note_type" : "DGN",
    "title"     : "note title 1",
    "note"      : "Note ---------------------- Note"
  }
]
```


## Creating Appointment From Receptionist App (Patient-Detail)
- Date 01-03-2024

> *POST* : /api/v1/appointment/add/

This Upper one will be used to create an appointment instance which 
- uses patient detail to create a patinet first
- then uses the patient is as foreignkey to create the appointment


The PAYLOAD Data will be in this format >>>

```json
{
  "appointment_datetime": "2024-03-01",
  "type": "IA",
  "doctor_id": 2, << No Need to send - it will get the Doctor id (from session user or receptionist_mapping)
  "specialization_id": 2, << Can be Omitted
  
  "patient_detail": {
      "phone_number": "1111111111", << Mandatory
      "email": "patient2@gmail.com", # Not Mandatory
      "first_name": "Mariz",
      "last_name": "last",
       "gender": "ML", # "FL" - Female , "OT" - Other
       "age"  : null,
       "date_of_birth" :  "2024-03-01" >>> give DOB or Age , one only
  },
  "slot_detail":  # Not Mandatory
          {
            "date"      : '2024-04-08', <<<< No Need to Pass this , will be taken from appointment_datetime
          "session"    : "evening", 
          "slot_number": 2}
}
```

![alt text](image-1.png)


The Output Response will be coming lke this -

```json
{
  "appointment_datetime": "2024-03-01T12:02:29.661752Z",
  "type": "IA",
  "doctor_id": 2,
  "specialization_id": 2
}

```


---
> *GET* : /api/v1/appointment/1/

This will be the URL pattern to get single appointment by filtering through appointment_id

The output for getting single appointment - instance will be coming like this -> 
[ 200 RESPONSE ]


```json
{
  "id"          : 1,
  "status"      : "CR",
  "appointment_datetime": "2024-03-01T10:00:00Z",
  "patient_id"  : 1,
  "doctor_id"   : 2,
  "specialization_id": 1,
  "created_by"  : "Admin",
  "updated_by"  : "Admin",
  "next_appointment": null,
  "created"     : "2024-03-01T10:51:53.035518Z",
  "updated"     : "2024-03-01T10:51:53.035530Z",
  "patient_name": "1234567890"
}
```
## Mapping Session-User to Selected Role
Created : Date 02-03-2024

> *POST* : /api/v1/user-role-mapping/add/

This Upper one will be used to create an user_role_mapping instance which 
- get the User from the request
- then uses the user-id and given role-id is as foreignkeys to create the instance


The PAYLOAD Data will be in this format >>>

```json
{
  "role_id": 1 << Will be selected from an Dropdown from the front end
}

```

The Output Response will be coming lke this -

```json
{
  "id": 1,
  "user_id": 19,
  "role_id": 1
}

```
## Mapping Doctor to Selected Receptionist
Created : Date 04-03-2024
> *GET* : /api/v1/receptionist/

The upper endpoint will be used to fetch a list of instances of the mapping

> **GET** : **/api/v1/receptionist/self/**

- This upper one to get receptionsts associated with session-user
```json
{
  "id"          : 2,
  "doctor_data" : 1,
  "receptionist_data": 15
}

```
> **POST** : /api/v1/receptionist/add/

This Upper one will be used to create an user_role_mapping instance which 
- get the 'Doctor' from the request (Session User)
- create or get instances of user, given the "Receptist Detail" --> receptionist-id
- then uses the doctor-id and created receptionist-id is as foreignkeys to create the 
doctor_receptionist_mapping instance


The PAYLOAD Data will be in this format >>>

```json
{
  "receptionist_detail": {
          "phone_number": "1111111122",
          "first_name"  : "newReceptionist",
          "last_name"   : "LstNaMe",
          "email"       : "newreceptionist1@gmail.com"
  }
}
```

The Output Response will be coming lke this -

```json
{
  "id"                : 5,
  "doctor_data"       : 1,
  "receptionist_data" : 16
}
```
## Final Step of Consultation -->
### PATCHING APPOINTMENT
Created : Date 19-03-2024
> **PATCH** : /api/v1/appointment/1/

> Note : Remeber the trailing slash.

The upper endpoint will be used to patch few more info to the APPOINTMENT.


PAYLOAD FORMAT :

```json
{
  "refer_doctor"        : "Doctor Panda __________", #Specialization can be placed there

  "follow_up_date"      : "2024-04-10"
}

```

The Response will come Like this -->

```json
{
  "id"      : 1,
  "type"    : "IA",
  "status"  : "IP",
  "appointment_datetime": "2024-03-01T09:01:10.775854Z",
  "patient_id"        : 23,
  "patient_name"      : "Atriprad",
  "doctor_id"         : 2,
  "specialization_id" : 3,
  "created_by"        : "",
  "updated_by"        : "",
  "next_appointment"  : null,
  "previous_appointment": null,
  "created"           : "2024-03-14T09:01:10.962249Z",
  "updated"           : "2024-03-19T17:19:42.994102Z",
  "refer_to"          : "Doctor Panda , Skin Specialist", # Note this
  "follow_up_date"    : "2024-04-10"
}
```


## Getting Data for Prescription Given an Appointment-ID
Created : Date 18-03-2024
> **GET** : /api/v1/consultation/rx/?appointment_id=1

The upper endpoint will be used to fetch bunch of data , from entire workflow of single consultation.


The response 
```json

{
  "consultation": 1,
  "finding"     : "Nothing in finding yet.",
  "diagnosis"   : "Ye hai ----------------------- Diagnosis.",
  "investigations": [
          {
            "id": 1,
            "consultation_id": 1,
            "investigation_id": 1,
            "note": "Note for Blood Glucose test."
          },
          {
            "id": 2,
            "consultation_id": 1,
            "investigation_id": 2,
            "note": "Need a complete fasting in the morning."
          }
  ],
  "symptoms": [
          {
            "symptom_name": "Symptomp1",
            "duration": "5 days",
            "severity": "MLD"
          },
          {
            "symptom_name": "Fever",
            "duration": "3 days",
            "severity": "MED"
          },
          {
            "symptom_name": "Cold",
            "duration": "2 days",
            "severity": "SEV"
          }
  ],
  "medicines": [
          {
            "id": 1,
            "medicine_name": "Paracetamol",
            "medicine_id": 1,
            "medicine_dosage": "2.0",
            "medicine_timing": "MN",
            "medicine_modality": "AF",
            "medicine_duration": "1",
            "medicine_instruction": "None for now."
          },
          {
            "id": 2,
            "medicine_name": "Cetirizine",
            "medicine_id": 14,
            "medicine_dosage": "1.0",
            "medicine_timing": "NT",
            "medicine_modality": "AF",
            "medicine_duration": "1",
            "medicine_instruction": "Continue for 3 days, or stop if recovered."
          }
       ],
  "instructions": [
          {
            "id": 1,
            "consultation_id": 1,
            "instruction": "Instruction ye hai bhai ------------------ Instruction."
          }
       ]
}

```
### Adding Vital for patient After Creation of Appointment
Created : Date 20-03-2024
> *POST* : /api/v1/patient-vital/

> Note : Remeber the trailing slash.

The upper endpoint will be used to POST few more info to the APPOINTMENT.


PAYLOAD FORMAT :

```json
 {
    "patient_id"        : 22, < COMING from the Created Appointment>
    "specialization_id" : 24, < Can be selected from a Dropdown >
    "appointment_id"    : 1,  < COMING from the Created Appointment>
    "vital_id"          : 2,  < Selected from DROPDOWN >
    "vital_value"       : 26
  }

```
Output will be coming like this -->

```json
{
  "id"          : 3,
  "patient_id"  : 22,
  "specialization_id": 24,
  "appointment_id": 1,
  "vital_id"    : 2,
  "vital_value" : 26.0
}
```

### Saving Collections (Medicines/Investigation) in Template master
@Grouping
Created : Date 22-03-2024
> *POST* : /api/v1/template-master/detail/

> Note : Remeber the trailing slash.

The upper endpoint will be used to add medicine or investigation grouping to user-profile.


PAYLOAD FORMAT :

```json
{
  "template_name": "General Fever Medicine-List",
  "user_id" : 1 , <<< No need to send - Session-User will be used
  "template_type": "MS", #MS - MedicineSet , IS - InvestigationSet , VS - VitalSet
  "medicine_sets": ['list of medicines, format provided below']
}

```
#### MedicineSet Format 

```json
"medicine_sets": [
      {
        "medicine_id": 1,
        "medicine_dosage": 1.0,
        "medicine_timing": "MN",
        "medicine_modality": "AF",
        "medicine_duration": "10 days",
        "medicine_instruction": "Take one tablet every morning after breakfast"
      },
      {
        "medicine_id": 2,
        "medicine_dosage": 0.5,
        "medicine_timing": "EV",
        "medicine_modality": "BF",
        "medicine_duration": "5 days",
        "medicine_instruction": "Take half a tablet every evening before dinner"
      }
  ]

```
```json
{

 "investigation_sets": [
            {
              "investigation_id": 1,
              "note": "Complete blood count (CBC) test. Fasting not required."
            },
            {
              "investigation_id": 2,
              "note": "Lipid profile test. Please fast for at least 12 hours before the test."
            }
          ]
}

```

#### For **GETTING** Template

1. To Get User Specific list of template 
> *GET* : /api/v1/template-master/

2. To get a Single Template instance with related medicine-set or investigation-set
> *GET* : /api/v1/template-master/2

3. To get all for an user, this will include *medicine-set* and *investigation-set*


> *GET* : api/v1/template-master/detail?template_type=MS

* USE THIS ONE ^

The output will come in this Format
```json
{
  "id": 2,
  "medicine_sets": [
                      {
                        "id": 2,
                        "medicine_name": "Paracetamol",
                        "medicine_id": 1,
                        "medicine_dosage": "1.0",
                        "medicine_timing": "MN",
                        "medicine_modality": "AF",
                        "medicine_duration": "10 days",
                        "medicine_instruction": "Take one tablet every morning after breakfast"
                      },
                      {
                        "id": 3,
                        "medicine_name": "Aspirin",
                        "medicine_id": 2,
                        "medicine_dosage": "0.5",
                        "medicine_timing": "EV",
                        "medicine_modality": "BF",
                        "medicine_duration": "5 days",
                        "medicine_instruction": "Take half a tablet every evening before dinner"
                      }
                    ],
  "template_name": "General Health Checkup",
  "template_type": "MS",
  "user_id": 1
}
```
## Saving and Getting Fee/Fee-Type for Doctor (Service Cost As Well)
- Date : 28-03-2024

> **GET** : /api/v1/fee-structure/?cost_type=DF

DF : DoctorFee

^ Use this to get all names of service cost (fee_type) from <-- MASTER DATA

```json
[
  {
    "id": 1,
    "name": "Registration Fee"
  },
  {
    "id": 2,
    "name": "Pre-Registration Fee"
  },
]
```

> **GET** : /api/v1/fee-structure/?cost_type=SC

^ Use this to get all names of service cost (fee_type) from <-- MASTER DATA

```json
[
  {
    "id": 4,
    "name": "Blood Sugar Checkup Fee"
  },
  {
    "id": 5,
    "name": "General  Checkup Fee"
  }
]
```
### Adding Bulk Use Fee Structure
> **POST** : /api/v1/fee-structure/add/

This Upper one will be used to Save a list of fee-type and it's amount in a Doctor's profile.

The PAYLOAD Data will be in this format >>>

```json
[
    {

      "fee_amount": 100,
      "fee_type_name": "New Consultation Fee Type 2",
      "cost_type" : "CS" >>> No need to mention for 'DF' , that will be added by default
    },
    {
      "fee_amount": 200,
      "fee_type_name": "Followup Fee Renewed",
       "cost_type" : "CS"
    }
  ]
```

Response will come like this :

```json
{
  "created": [
    {
      "id": 11,
      "user_id": 8,
      "fee_type": 8,
      "fee_amount": 100,
      "fee_type_name": "New Consultation Fee Type 2",
      "cost_type": "DF",
      "created": false
    },
    {
      "id": 12,
      "user_id": 8,
      "fee_type": 9,
      "fee_amount": 200,
      "fee_type_name": "Followup Fee Renewed",
      "cost_type": "DF",
      "created": false
    }
  ]
}
```
### Adding Single Service-Cost or User-Fee

> **POST** : /api/v1/fee-structure/self/

This Upper one will be used to Save a fee-type and it's amount in a Doctor's profile.
^ Same will be used to update amoutn as well.


The PAYLOAD Data will be in this format >>>

```json
{
  "fee_type_name": "Followup Fee"  , # using this as get_or_create mode
  "fee_amount": 500
}
```

Response will come like this :

```json
{
  "id": 8,
  "user_id": 8,
  "fee_type": 5,
  "fee_amount": "500.00",
  "fee_type_name": "Followup Fee"
}
```
---
> **PATCH** : /api/v1/fee-structure/update/6/


> Dont forget the final trailing slash '/'

Will fetch all listed Fee-Type and Amount for a Doctor in their profile

```json
{
  "fee_amount": 500,
  "fee_type_name": "CBC Test",
  "cost_type": "SC" >>> No need to pass if you want to enter as Doctor Fee : "DF"
}

```

Output will be this >>

```json
{
  "id": 13,
  "user_id": 8,
  "fee_type": 10,
  "fee_amount": "500.00",
  "fee_type_name": "CBC Test",
  "cost_type": "SC"
}

```

> **GET** : /api/v1/fee-structure/self/

Will fetch all listed Fee-Type and Amount for a Doctor in their profile

```json
[
  {
    "id": 5,
    "user_id": 8,
    "fee_type": 4,
    "fee_amount": "200.00",
    "fee_type_name": "Blood Sugar Checkup Fee",
    "cost_type": "SC"
  },
  {
    "id": 6,
    "user_id": 8,
    "fee_type": 6,
    "fee_amount": "500.00",
    "fee_type_name": "Followup Fee",
    "cost_type": "DF"
  },

]

```

---

## Saving and Getting User-Profile for Doctor 
- Date : 29-03-2024

> **GET** : /api/v1/user/
> 
This Upper one will be used to get all profile informations a Doctor's profile.


Response will come like this :

```json
{
  "id": 7,
  "user_id": 8,
  "gender": "ML",
  "age": null,
   "registration_number": null,
   "qualification" : "MS/MD.MBBS"

}
```
> **PATCH** : /auth/users/me/ -- Use the Djoser style to PATCH

```json
 {
    "age": 29,
     "registration_number": "MD/MS,BAMS"
  }
```

> **PATCH** : /api/v1/user/8/ -- session user-id : 8 (here)



The PAYLOAD Data will be in this format >>>

```json
{
  "id": 8,
  "full_name": "Doctor1 Dr1_Lastname",
  "first_name": "Doctor1",
  "last_name": "Dr1_Lastname",
  "profile_pic": "http://127.0.0.1:8000/media/profile_pics/doccc1111.jpeg",
  "gender": "ML",
  "age": 29,

  "aadhar": "1234123444444449",
  "registration_number":  null, 
  "address": "Doctor1 Address",
  "postal_code": "123456",
  "qualification":"MD/MS,BAMS",
  "is_doctor": true,
  "is_receptionist": false,
  "phone_number": "1111111111" <<< Not to be Updated
}
```
For profile pic you need to use this style :
Refer to the screenshot below (if using thunderclient to test) -

![alt text](image.png)

or the node.js code is pasted below :

```node.js
const fs = require('fs');
const request = require('request');

const options = {
  method: 'PATCH',
  url: 'http://127.0.0.1:8000/auth/users/me/',
  headers: {
    Accept: '*/*',
    'User-Agent': 'Thunder Client (https://www.thunderclient.com)',
    Authorization: 'JWT eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzEyMDUzNTMwLCJpYXQiOjE3MTIwNDE1MzAsImp0aSI6Ijc0MzQwZDM1ZjE5NzRkZThhOTQxM2M3Mzc3MDI4ZDE4IiwidXNlcl9pZCI6OH0.hwcKgxDF7aR55oy7uSByScPGRbwxlJEQhzScR9XkiU8',
    'content-type': 'multipart/form-data; boundary=---011000010111000001101001'
  },
  formData: {
    registration_number: 'registr_number118',
    profile_pic: {
      value: fs.createReadStream('/home/buddhiraj/Downloads/doccc1111.jpeg'),
      options: {filename: '/home/buddhiraj/Downloads/doccc1111.jpeg', contentType: null}
    }
  }
};

request(options, function (error, response, body) {
  if (error) throw new Error(error);

  console.log(body);
});
```


---

## Saving and Getting Specilization for Doctor
- Date : 01-04-2024

> **POST** : /api/v1/user-specialization-procedure/self/
This Upper one will be used to Save a new specilization in a Doctor's profile.

^ GETorCREATE MODE
- Session user id will be used

The PAYLOAD Data will be in this format >>>

```json
{
    "specialization_name": "New-Speciology"
}
```

Response will come like this :

```json
{
  "id": 4,
  "procedure_id": null,
  "specialization_id": 30,
  "user_id": 8 <<<>>>
}
```
---

> *GET* : /api/v1/user-specialization-procedure/self/

Will fetch all added Specilization for a Doctor in their profile

```json
[
  {
    "id"                : 6,
    "user_id"           : 8,
    "specialization_id" : 30,
    "specialization_name": "New-Speciology",
    "procedure_id"       : null -- Ignore it
  }
]
```


## Saving Entity and Mapping it for Doctor
- Date : 03-04-2024

> **POST** : /api/v1/user-entity-mapping/
This Upper one will be used to Save a new Entity in a Doctor's profile.

^ GETorCREATE MODE
- Session user id will be used

The PAYLOAD Data will be in this format >>>

```json
{
  "user_id": 1, 
  "entity_name": "Entity Two",  
  "is_active": true,
  "to_date": "2024-04-10" 
}
```

Response will come like this :

```json
{
  "id": 2,
  "user_id": 1,
  "entity_id": 2,
  "is_active": true,
  "from_date": "2024-04-03",
  "to_date": "2024-04-10",
  "updated": "2024-04-03"
}

```
---

<!-- > *GET* : /api/v1/user-specialization-procedure/self/

Will fetch all added Specilization for a Doctor in their profile

```json
[
  {
    "id"                : 6,
    "user_id"           : 8,
    "specialization_id" : 30,
    "specialization_name": "New-Speciology",
    "procedure_id"       : null -- Ignore it
  }
]
``` -->

## Saving Entity and Mapping it for Doctor
- Date : 03-04-2024

> **POST** : /api/v1/user-entity-mapping/
This Upper one will be used to Save a new Entity in a Doctor's profile.

^ GETorCREATE MODE
- Session user id will be used

The PAYLOAD Data will be in this format >>>

```json
{
  "user_id": 1, 
  "entity_name": "Entity Two",  
  "is_active": true,
  "to_date": "2024-04-10" 
}
```

Response will come like this :

```json
{
  "id": 2,
  "user_id": 1,
  "entity_id": 2,
  "is_active": true,
  "from_date": "2024-04-03",
  "to_date": "2024-04-10",
  "updated": "2024-04-03"
}

```

## Getting Aggregatred Appointment Report for Doctor
- Date : 03-04-2024

> **GET** : /api/v1/appointment/report/

This Upper one will be used to get data for patient-visit + revenue-earn in a Doctor's profile.


Response will come like this :

A list of this

```json
[
  {
    "date": "2024-03-22",
    "appointment_count": 5,
    "consultation_count": 2,
    "total_revenue": "200"
  }
]

```
## Saving SavedPatient for Selected Doctor
Created : Date 08-04-2024
> **GET** : /api/v1/saved-patient/self/

The upper endpoint will be used to fetch a list of instances of the mapping for session user as Doctor.

```json
[
  {
    "id"      : 1,
    "patient" : {
      "full_name": "Patient1 Pt1_Lastname",
      "age"   : null,
      "gender": "ML"
    },
    "tag": []
  },


  {
    "id": 3,
    "patient": {
      "full_name": "Patient5 Pt5_Lastname",
      "age": null,
      "gender": "ML"
    },
    "tag": [
      {
        "name": "jundice"
      },
      {
        "name": "migrane"
      }
    ]
  },
]
```



> **POST** : **/api/v1/saved-patient/add/**

This Upper one will be used to create an user_role_mapping instance which 
- get the 'Doctor' from the request (Session User)
- map it with patient_id 


The PAYLOAD Data will be in this format >>>

NOTE : Tag no need to add for now.

```json
{
  "patient_id": 4 

  //  "tag": [
  //       {"name": "covid"},
  //       {"name": "TB"}
  //   ]

}
```

The Output Response will be coming lke this -

```json
{
  "id": 5,
  "doctor_id": 8,
  "patient_id": 4,
  "tag": []
}
```

## Saving and Getting Leaves for Doctor
- Date : 12-04-2024

> **POST** : /api/v1/applied-leave/self/

This Upper one will be used to apply a leave  from Doctor's profile.And use 
the "start_date" & "end_date" to find any leae whic overlap with the days between **start_date** and **end_date**.

^ GETorCREATE MODE
- Session user id will be used

The PAYLOAD Data will be in this format >>>

```json
{
  "purpose"   : "2 Days Leave",
  "startDate" : "2024-04-17",
  "endDate"   : "2024-04-19"
}
```

Response will come like this :

```json
{
  "id"      : 4,
  "purpose" : "2 Days Leave",
  "user_id" : 8,
  "startDate" : "2024-04-17",
  "endDate"   : "2024-04-19"
}

```
---

> *GET* : /api/v1/applied-leave/self/?start_date=2024-04-18&end_date=2024-04-20

Will fetch all leaves applied for a Doctor in their profile

```json
[
  {
    "id": 1,
    "purpose": "Summer Holiday",
    "user_id": 8,
    "startDate" : "2024-04-12",
    "endDate"   : "2024-04-15"
  },
  {
    "id": 3,
    "purpose": "2 Days Leave",
    "user_id": 8,
    "startDate" : "2024-04-17",
    "endDate"   : "2024-04-19"
  }
]
```


## Saving and Getting Booking Slot Configuration for Weekdays -  for Doctor
- Date : 12-04-2024

> **POST** : /api/v1/booking-slot/self/

This Upper one will be used to apply a leave  from Doctor's profile.And use 
the "start_date" & "end_date" to find any leae whic overlap with the days between **start_date** and **end_date**.

^ GETorCREATE MODE
- Session user id will be used in Doctor_id

The PAYLOAD Data will be in this format >>>

```json
{
  "name"                : "Daygroup 1 for Doc2",
  "is_active"           : true ,  >>>> Send if its true , False is by-default
  "booking_config_list" : [
    {
      "day": "mon",
      "is_active": true,
      "morning_slots_is_active": true,
      "morning_start_time": "08:00:00",
      "morning_end_time": "11:00:00",
      "morning_slots": 10,
      "afternoon_slots_is_active": true,
      "afternoon_start_time": "13:00:00",
      "afternoon_end_time": "16:00:00",
      "afternoon_slots": 10,
      "evening_slots_is_active": true,
      "evening_start_time": "18:00:00",
      "evening_end_time": "21:00:00",
      "evening_slots": 10
    },
    {
      "day": "tue",
      "is_active": true,
      "morning_slots_is_active": true,
      "morning_start_time": "08:00:00",
      "morning_end_time": "11:00:00",
      "morning_slots": 10,
      "afternoon_slots_is_active": true,
      "afternoon_start_time": "13:00:00",
      "afternoon_end_time": "16:00:00",
      "afternoon_slots": 10,
      "evening_slots_is_active": true,
      "evening_start_time": "18:00:00",
      "evening_end_time": "21:00:00",
      "evening_slots": 10
    }
  ]
}
```

Response will come like this :

```json
  {
    "id": 3,
    "doctor_id": 8,
    "day": "mon",
    "is_active": true,
    "morning_slots_is_active": true,
    "morning_start_time": "08:00:00",
    "morning_end_time": "11:00:00",
    "morning_slots": 10,
    "afternoon_slots_is_active": true,
    "afternoon_start_time": "13:00:00",
    "afternoon_end_time": "16:00:00",
    "afternoon_slots": 10,
    "evening_slots_is_active": true,
    "evening_start_time": "18:00:00",
    "evening_end_time": "21:00:00",
    "evening_slots": 10
  },

```
---

> *GET* : /api/v1/booking-slot/self/

Will fetch all confugured booking slots for  applied for a Doctor in their profile for weekdays.


```json
[
  {
    "name": "DayGrouping Weekdays",
    "is_active": true,
    "booking_config_list": [
                              {
                                "day": "mon",
                                "is_active": true,
                                "morning_slots_is_active": true,
                                "morning_start_time": "08:00:00",
                                "morning_end_time": "11:00:00",
                                "morning_slots": 10,
                                "afternoon_slots_is_active": true,
                                "afternoon_start_time": "13:00:00",
                                "afternoon_end_time": "16:00:00",
                                "afternoon_slots": 10,
                                "evening_slots_is_active": true,
                                "evening_start_time": "18:00:00",
                                "evening_end_time": "21:00:00",
                                "evening_slots": 10
                              },
                              {},
                              {},
                              {},

    ]
  },
  {
    "name": "Weekend Grouping",
    "is_active": false,
    "booking_config_list": [
                              {
                                "day": "sat",
                                "is_active": true,
                                "morning_slots_is_active": true,
                                "morning_start_time": "07:00:00",
                                "morning_end_time": "12:00:00",
                                "morning_slots": 20,
                                "afternoon_slots_is_active": false,
                                "afternoon_start_time": null,
                                "afternoon_end_time": null,
                                "afternoon_slots": 0,
                                "evening_slots_is_active": false,
                                "evening_start_time": null,
                                "evening_end_time": null,
                                "evening_slots": 0
                              },
                              {
                                "day": "sun",
                                "is_active": true,
                                "morning_slots_is_active": true,
                                "morning_start_time": "08:00:00",
                                "morning_end_time": "11:00:00",
                                "morning_slots": 10,
                                "afternoon_slots_is_active": true,
                                "afternoon_start_time": "13:00:00",
                                "afternoon_end_time": "16:00:00",
                                "afternoon_slots": 10,
                                "evening_slots_is_active": true,
                                "evening_start_time": "18:00:00",
                                "evening_end_time": "21:00:00",
                                "evening_slots": 10
                              }
    ]
  }
]
```



## Saving and Getting Slots for an Appointment
- Date : 12-04-2024

> **GET** : /api/v1/booking-slot/**booked_slots**/?**date**=2024-04-08&**session**=morning

This Upper one will be used to check for bookes slots  Doctor's profile.
In the query input give -->
  date : *"the date on which you want to check already booked slots info"*
  session : ["morning"/"afternoon"/"evening"]


- Session user id will be used internally


Response will come like this :

```json
{
  "active_config": "DayGrouping Weekdays", >>> This is the name of activeConfigName for session-user
  "slot_config_id": 3, >>>> Will be kep in context and used to post new slot
  "total_slots": 10, >>>>> Will be used to diaplay small rectangular boxes slots numbered 1 - 10 
  "booked_slot_list": [ >>> These are already booked , so the squaeres will be marked red
    1,
    2,
    3,
    4
  ]
}

```
---

> *POST* : /api/v1/booking-slot/**book_slot**/

Will Book appointment for a slot given an Slot all leaves applied for a Doctor in their profile

```json
{
  "date": "2024-04-08",
  "session" : "morning", >> session : ["morning"/"afternoon"/"evening"]
  "slot_number" : 6
}
```

Response will come like this  :

```json
{
  "message": "The slot has been successfully booked.",
  "slot_id": 6  # Slot booking id not slot_number >> Will be filled in appointment
}
```

Error Message : if you try to book in already booked 
> (This will never occur as it will be constrained from the frontend.)
```json
{
  "error": "The slot is already booked."
}
```
---

## Saving Refer Doctor and Mapping it for Session-User
- Date : 16-04-2024

> **POST** : /api/v1/v1/refer-doc/self/
This Upper one will be used to Save a new ReferDoctor in a Doctor's profile.


- Session user id will be used
- Specialization Name will be pushed in Getorcreate Mode

The PAYLOAD Data will be in this format >>>

```json

{
  "doctor_name": "Dr Atiprad Mishra",
  "phone_number": "9931770045",
  "specialization_name": "Family Medicine"
}

```
> **GET** : /api/v1/v1/refer-doc/self/


Response obtained will look like this :

```json
[
  {
    "id": 1,
    "doctor_name": "Dr Anubhav Mohanty",
    "specialization_id": 6,
    "specialization_name": "Family Medicine",
    "phone_number": "9934570045"
  },
  {
    "id": 2,
    "doctor_name": "Dr Atiprad Mishra",
    "specialization_id": 6,
    "specialization_name": "Family Medicine",
    "phone_number": "9931770045"
  }
]

```
# Saving Visitor Details ( Public View API )
- Date : 20-04-2024

> **POST** : /api/v1/v1/visitor/
This Upper one will be used to Save a new Visitor detail.

The PAYLOAD Data will be in this format >>>

```json

{
  "visitor_name": "Test Visitor 1",
  "email"       : "gmail@example.com",
  "phone_number": "9950969023",
  "country"     : "India",    #NotMandatory
  "state"       : "Odisha"    #NotMandatory
}

```


## Saving and Getting Prescription Setting for Doctor
- Date : 24-04-2024

> **GET** : /api/v1/prescription-setting/

This Upper one will be used to save a setting for doctor.


- Session user id will be usedas doctor-id internally


Response will come like this :

```json
[
  {
    "id": 1,
    "doctor_id": 8,
    "doctor_info_is_visible": true,
    "doctor_info_alignment": "LT",
    "doctor_name": "Dr Anubhav Mohanty",
    "doctor_qualification": "MBBS , PG MD,",
    "registration_number": "2uu3437933gd83df",
    "phone_number": "1111111111",

    "entity_info_is_visible": true,
    "entity_info_alignment": "LT",
    "entity_name": "Bhagvati Clinic",
    "address": "AKSHYA TECH PARK, In front of Airtel Nextra",
    "entity_phone_number1": "8889998888",
    "entity_phone_number2": null,
    
    "entity_timing_is_visible": true,
    "entity_startime": "10:30:00",
    "entity_endtime": "18:00:00",
    "doctor_signature_is_visible": false,
    "doctor_signature_alignment": "LT",
    "signature_line_1": "",
    "signature_line_2": ""
  }
]

```
---

> *POST* : /api/v1/prescription-setting/

PAYLOAD Style

```json
  {

    "doctor_info_is_visible": true,
    "doctor_info_alignment": "LT",
    "doctor_name": "Dr Anubhav Mohanty",
    "doctor_qualification": "MBBS , PG MD,",
    "registration_number": "2uu3437933gd83df",
    "phone_number": "1111111111",

    "entity_info_is_visible": true,
    "entity_info_alignment": "LT",
    "entity_name": "Bhagvati Clinic",
    "address": "AKSHYA TECH PARK, In front of Airtel Nextra",
    "entity_phone_number1": "8889998888",
    "entity_phone_number2": null,
    
    "entity_timing_is_visible": true,
    "entity_startime": "10:30:00",
    "entity_endtime": "18:00:00",

    "doctor_signature_is_visible": false,
    "doctor_signature_alignment": "LT",
    "signature_line_1": "",
    "signature_line_2": ""
  }
```

## Getting Prescription PDF
- Date : 16-04-2024

> **POST** : /api/v1/consultation/rx-print/?appointment_id=1 

This will generate a PDF in the response.
Refer to this -image :

![alt text](assets/rx-print.png)
One Sample Pdf is here : assets/prescription_customized.pdf

The python code part to generate the reponse is here :

```Python
try:
    # Generate the PDF from the rendered HTMLz
    pdf = pdfkit.from_string(html_output, False)

    # Create an HTTP response with the PDF file
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="prescription.pdf"'
    return response
except Exception as e:
    logging.error(f"An error occurred when generating the PDF: {e}")
    return Response({'error': 'An error occurred when generating the PDF'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
```

### How to use the prescription PDF ??
Certainly! Here's how you can handle the file response in a React component:

```javascript
import React from 'react';
import axios from 'axios';

class PDFViewer extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            pdfData: null,
            loading: false,
            error: null
        };
    }

    componentDidMount() {
        // Make API call to fetch PDF file
        axios.get('/api/v1/consultation/rx-print/?appointment_id=1', {
            responseType: 'arraybuffer', // Ensure response is treated as binary data
        })
        .then(response => {
            // Create a Blob from the PDF data
            const pdfBlob = new Blob([response.data], { type: 'application/pdf' });
            const pdfUrl = URL.createObjectURL(pdfBlob);

            // Set the PDF data in state
            this.setState({ pdfData: pdfUrl, loading: false });
        })
        .catch(error => {
            // Handle error
            this.setState({ error: error.message, loading: false });
        });
    }

    render() {
        const { pdfData, loading, error } = this.state;

        if (loading) {
            return <div>Loading...</div>;
        }

        if (error) {
            return <div>Error: {error}</div>;
        }

        return (
            <div>
                {pdfData && (
                    <iframe
                        title="PDF Viewer"
                        src={pdfData}
                        width="100%"
                        height="500px"
                        style={{ border: 'none' }}
                    />
                )}
            </div>
        );
    }
}

export default PDFViewer;
```

In this React component:

1. We use Axios to make a GET request to your API endpoint that returns the PDF file.
2. We set the `responseType` to `arraybuffer` to ensure that Axios treats the response as binary data.
3. Upon successful response, we create a Blob from the received PDF data and generate a URL for it using `URL.createObjectURL()`.
4. We then set this PDF URL in the component state.
5. In the render method, we conditionally render an `<iframe>` element with the PDF URL as its `src`.

Replace `'your_api_endpoint_url'` with the actual URL of your API endpoint that returns the PDF file. You can then use this `PDFViewer` component in your React application to display the PDF file.

## Getting Latest Appointment(closed) Prescription PDF
- Date : 03-05-2024

> **GET** : /api/v1/appointment/patient-latest/?appointment_id=2

Response will come like this  :

```json

{
  "pdf_url": "http://127.0.0.1:8000/media/test_reports/Rx_1_c2ZV31e.pdf"
}

```
Now , How to implement this in React ???

Refer to this : https://colab.research.google.com/drive/102ydMqadMVoW5Tm6GLmcN6uH_lou_pIj?usp=sharing



# FINAL FINAL FINAL FINAL FINAL FINAL FINAL FINAL FINAL

## Basic Assumption we have made :
1 - Entity doesnt exist , for now - instead a single doctor runs the clinic with a single receptionist mapped to himself/herself
2 - doctor_receptionist_mapping




# To-Do :
- PostgreSQL 
- Simulation in real-time for Multiple User
- Automated testing 
- On or Before April-1 Find Alternate Cloud 
      - Alternate Platform Search - for Cloud and DB 
      - DB Migration Plan 
      - Cloud migration Strategy
  


### April First Week - After Product-Lunch
- Backup - chron-job [will be scheduled in Evening after working hour]


# TO Do :
> March 19th 2024

- [ ] (for unchecked checkbox)
- [x] (for checked checkbox)


| **Sl No.** | **Task**                                                                  | **Status** |
|------------|---------------------------------------------------------------------------|------------|
| 1          | Saving Vitals for an Appointment                                          | <input type="checkbox" style="margin-left: 5px"> |
| 2          | Consultation Fee in user Profile                                          | <input type="checkbox" style="margin-left: 5px" checked> |
| 3          | Patient Able to Select a Doctor and Book an Appointment in a date         | <input type="checkbox" style="margin-left: 5px"> |
| 4          | To upload a test-report for patient (Along With Submitting Document Name) | <input type="checkbox" style="margin-left: 5px"> |
| 5          | Adding a sample vital master                                              | <input type="checkbox" style="margin-left: 5px" checked> |
| 6          | Find and implement a Subscription Module for the Medi-Man                 | <input type="checkbox" style="margin-left: 5px"> |
| 7          | Created by Updated by Properly implement in Appointment – Consultation    | <input type="checkbox" style="margin-left: 5px"> |
| 8          |                                                                           | <input type="checkbox" style="margin-left: 5px"> |


# APIs to be used by Patient-Side App :
- Appointment Booking : Patient-Side
- Test-Report Upload

## Appointment Booking from Patient App

> **POST** : /api/v1/appointment/create/

The Payload format is here :

```json
{
  "appointment_datetime": "2024-03-01T09:01:10.775854Z", # Today or Selected Date
  "type"              : "IA", #Type will be initial/Follow-Up - DROPDOWN
  "patient_id"        : 23, << No need to give - Session_User.id
  "doctor_id"         : 2,
  "specialization_id" : 3, << If not selected 
  "created_by"        : "", << Session User - PATIENT - No need to Send
  "previous_appointment": null, << Selected from Dropdown if Any

}
```

## Uploading test Report Etc.  from Patient App

> **POST** : /api/v1/appointment/create/

The Payload format is here :

document_label --> can be selected from   the Investigation : DROPDOWN

```json
{
 "user_id"        : 1, #Coming from session-user 
  "appointment_id":1 , # Not Mandatory

  "document_label":, # Keep a name for the doc : ex - Haemoglobin test, CBC test 
  "document_path" : "/default-filepath", # No need to pass
}
```


