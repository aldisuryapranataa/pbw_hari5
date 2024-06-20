from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ContentForm, AddressForm,LoginForm, PenggunaForm, SearchPenggunaByStateForm, KelompokForm
from .models import Pengguna,Kelompok,Content
from django.http import JsonResponse


def set_login(request):
    form = LoginForm()
    context ={
        'form' : form,
    }
    return render(request, 'data_entry/login.html' , context)

def set_pengguna(request):
    if request.method == "POST":
        form = PenggunaForm(request.POST)
        if form.is_valid():
            form.save()
            list_pengguna = Pengguna.objects.all().order_by('-id')
            context = {
              "form": form, 
              "list_pengguna": list_pengguna
              }
            return render('data_entry/input_data_1.html', context)
        else:
            list_pengguna = Pengguna.objects.all().order_by('-id')
            context = {
              "form": form, 
              "list_pengguna": list_pengguna
              }
            return render(request, "data_entry/input_data_1.html", context)
    else:
        form = PenggunaForm(None)
        list_pengguna = Pengguna.objects.all().order_by('-id')
        context = {"form": form, "list_pengguna": list_pengguna}
        return render(request, "data_entry/input_data_1.html", context)

def view_pengguna(request):
    pass

def view_pengguna(request, id):
  try:
    pengguna = Pengguna.objects.get(pk=id)
    return render(request, 'data_entry/pengguna_detail.html', {'user_id': pengguna.id})
  except Pengguna.DoesNotExist:
    return JsonResponse({'error' : 'user not found '}, status = 404)

def get_pengguna_detail_api(request, user_id):
  try :
    pengguna = Pengguna.objects.get(pk=user_id)
    data = {
      'email' : pengguna.email,
      'address_1' : pengguna.address_1,
      'address_2' : pengguna.address_2,
      'city' : pengguna.city,
      'state' : pengguna.state,
      'zip_code' : pengguna.zip_code,
      'tanggal_join' : pengguna.tanggal_join.strftime('%Y-%m-%d'),
    }
    return JsonResponse(data)
  except Pengguna.DoesNotExist:
    return JsonResponse({'error' : 'user not found'}, status=404)


from django.http import HttpResponse
from django.shortcuts import render
from .forms import AddressForm, PenggunaForm, ContentForm, IcreationForm
from .models import Pengguna
from .models import Content
from .models import Icreation
from django.http import JsonResponse


def set_data_entry(request):
    list_pengguna = Pengguna.objects.all().order_by('-id')
    form = AddressForm()
    context = {'form': form, 'list_pengguna': list_pengguna}
    return render(request, 'data_entry/input_data_1.html', context)

def set_pengguna(request):
    list_pengguna = Pengguna.objects.all().order_by('-id')
    context = None
    form = PenggunaForm(None)
    email_p = None
    if request.method == "POST":
        form = PenggunaForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            request.sesion['email'] = email
            request.sesion.modified = True
            form.save()
            list_pengguna = Pengguna.objects.all().order_by('-id')
            email_p = request.session['email']
            context = {
              "form": form, 
              "list_pengguna": list_pengguna,
              'email_p' : email_p,
              }
            return render('data_entry/input_data_1.html', context)
        else:
            list_pengguna = Pengguna.objects.all().order_by('-id')
            context = {
              "form": form, 
              "list_pengguna": list_pengguna
              }
            return render(request, "data_entry/input_data_1.html", context)
    else:
        form = PenggunaForm(None)
        list_pengguna = Pengguna.objects.all().order_by('-id')
        context = {"form": form, "list_pengguna": list_pengguna}
        return render(request, "data_entry/input_data_1.html", context)

def view_pengguna(request):
    pass

def view_pengguna(request, id):
  try:
    pengguna = Pengguna.objects.get(pk=id)
    return render(request, 'data_entry/pengguna_detail.html', {'user_id': pengguna.id})
  except Pengguna.DoesNotExist:
    return JsonResponse({'error' : 'user not found '}, status = 404)

def get_pengguna_detail_api(request, user_id):
  try :
    pengguna = Pengguna.objects.get(pk=user_id)
    data = {
      'email' : pengguna.email,
      'address_1' : pengguna.address_1,
      'address_2' : pengguna.address_2,
      'city' : pengguna.city,
      'state' : pengguna.state,
      'zip_code' : pengguna.zip_code,
      'tanggal_join' : pengguna.tanggal_join.strftime('%Y-%m-%d'),
    }
    return JsonResponse(data)
  except Pengguna.DoesNotExist:
    return JsonResponse({'error' : 'user not found'}, status=404)

def set_content(request):
  form  = ContentForm(None)
  context = None
  pengguna = None
  
  if request.session.get("email",None):
    email = request.session.get("email", None)
    pengguna = Pengguna.objects.get(email = email) 
    initial_data = {"author" : pengguna}
    form = ContentForm(initial=initial_data)
    
    if request.method == 'POST':
      form = ContentForm(request.POST)
      if form.is_valid():
        form.save()
        context = {
          'form' : form,
        }
        return render(request, 'data_entry/content.html', context)
      else:
        context = {
          'form' : form,
          "pengguna": pengguna,
          'email' : email,
        }
    return render(request, 'data_entry/content.html', context)

def set_kelompok(request):
    if request.method == "POST":
        form = KelompokForm(request.POST)
        if form.is_valid():
            form.save()
            list_kelompok = Kelompok.objects.all().order_by('-id')
            context = {
              "form": form, 
              "list_kelompok": list_kelompok
              }
            return render(request,'data_entry/kelompok.html', context)
        else:
            list_kelompok = Kelompok.objects.all().order_by('-id')
            context = {
              "form": form, 
              "list_creation": list_creation
              }
            return render(request, "data_entry/kelompok.html", context)
    else:
        form = KelompokForm(None)
        list_kelompok = Kelompok.objects.all().order_by('-id')
        context = {"form": form, "list_kelompok": list_kelompok}
        return render(request, "data_entry/kelompok.html", context)

def set_icreation(request):
    icreation = Icreation.objects.all()
    return render(request, 'data_entry/icreation_list.html', {'icreation': icreation})

def icreation_list(request):
    if request.method == 'POST':
        form = IcreationForm(request.POST)
        if form.is_valid():
            form.save()
        # Ambil ulang daftar objek setelah menyimpan
        icreation_list = Icreation.objects.all().order_by('-id')
        context = {
            "form": form,
            "icreation_list": icreation_list
        }
        return render(request, 'data_entry/icreation_form.html', context)
    else:
        form = IcreationForm()
        icreation_list = Icreation.objects.all().order_by('-id')
        context = {
            "form": form,
            "icreation_list": icreation_list
        }
        return render(request, 'data_entry/icreation_form.html', context)
      


def search_pengguna_by_state(request):
    pesan = None
    tampil = None
    form = None
    listpengguna = None
    status = None  # Define status variable
    if request.method == "POST":
        form = SearchPenggunaByStateForm(request.POST)
        if form.is_valid():
            state = form.cleaned_data['state']
            listpengguna = Pengguna.objects.filter(state=state)
            if not listpengguna:
                pesan = "Data Pengguna tidak ditemukan"
                status = True  # Assign a value to status
            else:
                tampil = True
    else:
        form = SearchPenggunaByStateForm()
    
    context = {
        'form': form,
        'tampil': tampil,
        'pesan': pesan,
        'listpengguna': listpengguna,
        'status': status,  # Include status in the context
    }
    return render(request, 'data_entry/list_pengguna.html', context=context)

def set_landing(request):
    return render(request, 'data_entry/landingPage.html')
  
def set_home(request):
  return render(request, 'data_entry/homepage.html')

def penggunal_ist(request):
  pengguna = Penguna.object.all()
  serializers = PenggunaSerializers(pengguna, many=True)
  