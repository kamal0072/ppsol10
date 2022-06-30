from django import forms
from .models import StudentModel
# STATE_CHOICES = (
#    ("AN","Andaman and Nicobar Islands"),
#    ("AP","Andhra Pradesh"),
#    ("AR","Arunachal Pradesh"),
#    ("AS","Assam"),
#    ("BR","Bihar"),
#    ("CG","Chhattisgarh"),
#    ("CH","Chandigarh"),
#    ("DN","Dadra and Nagar Haveli"),
#    ("DD","Daman and Diu"),
#    ("DL","Delhi"),
#    ("GA","Goa"),
#    ("GJ","Gujarat"),
#    ("HR","Haryana"),
#    ("HP","Himachal Pradesh"),
#    ("JK","Jammu and Kashmir"),
#    ("JH","Jharkhand"),
#    ("KA","Karnataka"),
#    ("KL","Kerala"),
#    ("LA","Ladakh"),
#    ("LD","Lakshadweep"),
#    ("MP","Madhya Pradesh"),
#    ("MH","Maharashtra"),
#    ("MN","Manipur"),
#    ("ML","Meghalaya"),
#    ("MZ","Mizoram"),
#    ("NL","Nagaland"),
#    ("OD","Odisha"),
#    ("PB","Punjab"),
#    ("PY","Pondicherry"),
#    ("RJ","Rajasthan"),
#    ("SK","Sikkim"),
#    ("TN","Tamil Nadu"),
#    ("TS","Telangana"),
#    ("TR","Tripura"),
#    ("UP","Uttar Pradesh"),
#    ("UK","Uttarakhand"),
#    ("WB","West Bengal")
# )

# class StudentForm(forms.Form):
#    name=forms.CharField(min_length=10,max_length=20,strip=True)
#    roll_no=forms.IntegerField(min_value=100,max_value=9999)
#    address=forms.CharField(error_messages={'required':'Correct Address is mandatory '})
#    email=forms.EmailField(min_length=15,max_length=40)
#    color=forms.BooleanField(required=False)
#    password=forms.CharField()
#    confirm_password=forms.CharField()

class StudentModelForm(forms.ModelForm):
   color=forms.BooleanField(required=False)
   state=forms.Select()
   class Meta:
      model=StudentModel
      fields="__all__"
      # fields=['id','name','roll_no','address','email']
      # exclude=['name','roll_no',]
      help_texts={
         "name":"Enter the student name",
         'roll_no':'enter roll number',
      }
      error_messages={
         'name':{'required':'Name is required!!!'},
         "roll_no":{"required":'Enter valid Roll number'}
      }
      widgets={
         "name":forms.TextInput(attrs={'placeholder':'Enter student name...'}),
         "roll_no":forms.NumberInput(attrs={'placeholder':'Enter student roll number...'}),
         "address":forms.Textarea(attrs={'placeholder':'Enter student correct address..','rows':20,"cols":40}),
         "pwd1":forms.PasswordInput(),
         "pwd2":forms.PasswordInput(),
         # 'state':forms.RadioSelect(),
         # 'state':forms.CheckboxSelectMultiple(),
         'state':forms.Select(),
      }