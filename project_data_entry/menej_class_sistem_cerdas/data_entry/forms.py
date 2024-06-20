from django import forms
from .models import Pengguna
from .models import Content
from .models import Icreation
from .models import Kelompok
STATES = (
    ('', 'Choose...'),
    ('DKI   ','Daerah khusus Ibu Kota'),
    ('DIY','Daerah Istimewa Yogyakarta'),
    ('JABAR','Jawa Barat'),
)

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder' : 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput())

    check_me_out = forms.BooleanField(required=False)

class SearchPenggunaByStateForm(forms.Form):
    state = forms.ChoiceField(choices = STATES)

class AddressForm(forms.Form):
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Email'}))
    password = forms.CharField(widget=forms.PasswordInput())
    address_1 = forms.CharField(
        label='Address',
        widget=forms.TextInput(attrs={'placeholder': '1234 Main St'})
    )
    address_2 = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Apartment, studio, or floor'})
    )
    city = forms.CharField()
    state = forms.ChoiceField(choices=STATES)
    zip_code = forms.CharField(label='Zip')
    check_me_out = forms.BooleanField(required=False)

class PenggunaForm(forms.ModelForm):
    state = forms.ChoiceField(choices=STATES)
    
    class Meta:
        model = Pengguna
        exclude = ["Tanggal join",]

class ContentForm(forms.ModelForm):
    class Meta :
        model = Content
        exclude = ["date_created"]

class KelompokForm(forms.ModelForm):
    class Meta :
        model = Kelompok
        exclude = [""]
        fields = "__all__"
        
class IcreationForm(forms.ModelForm):
    class Meta:
        model = Icreation
        fields = [
            'deskripsi_masalah',
            'deskripsi_fitur',
            'deskripsi_label',
            'kategori_masalah',
            'tanggal_mulai',
            'tanggal_selesai',
            'status_penyelesaian',
            'catatan_akhir'
        ]
        widgets = {
            'tanggal_mulai': forms.DateInput(attrs={'type': 'date'}),
            'tanggal_selesai': forms.DateInput(attrs={'type': 'date'}),
        }
