
# Create your views here.
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import CustomerForm
from .models import CustomerInfo,mydb
from django.db import connection
import os
from django.http import JsonResponse


def get_values_view(request):
    file_name = request.GET.get('file_name', '')
    file_name_without_ext = os.path.splitext(file_name)[0]
    
    # Query the secondary database
    records = mydb.objects.using('secondary').filter(formid__startswith=file_name_without_ext)
    
    # Prepare the data to return
    data = {record.field_name: record.OCR_value for record in records}
    print(data)
    return JsonResponse(data)


def update_origdb(file_name,customer_info):
    og_db = [
    "Customer_full_name",
    "BankName",
    "Zipcode",
    "State",
    "Phone_number",
    "Account_number",
    ]
    ui_db = [
        "full_name",
        "bank_name",
        "zip_code",
        "state",
        "phone_number",
        "account_number",
    ]
    file_name_without_ext = os.path.splitext(file_name)[0]
    print(file_name_without_ext)
    orig_records = mydb.objects.using('secondary').filter(formid__startswith=file_name_without_ext)
    for orig_record in orig_records:
        print(orig_record.field_name)  
        if orig_record.field_name in og_db:
            index = og_db.index(orig_record.field_name)
            print(index)
            new_value = getattr(customer_info, ui_db[index], None)
            print(f"New value for {orig_record.field_name}: {new_value}")
            if orig_record.OCR_value != new_value:
               orig_record.Edited_value = new_value
               orig_record.save(using='secondary')
               print(f"Updated {orig_record.field_name} from {orig_record.OCR_value} to {new_value}")

def customer_form_view(request):     
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            customer_info = CustomerInfo(
                full_name=form.cleaned_data['full_name'],
                bank_name=form.cleaned_data['bank_name'],
                zip_code=form.cleaned_data['zip_code'],
                state=form.cleaned_data['state'],
                country_code = form.cleaned_data['country_code'],
                phone_number=form.cleaned_data['phone_number'],
                account_number=form.cleaned_data['account_number'],
                file_name = form.cleaned_data['file_name']
            )
            customer_info.save()
            file_name = form.cleaned_data['file_name']
            update_origdb(file_name,customer_info)
                       
    else:
        form = CustomerForm()
    return render(request,'customer_form.html',{'form':form})