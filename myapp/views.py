from django.shortcuts import render
# Create your views here.
# views.py
import pandas as pd
from django.shortcuts import render

from .forms import ExcelUploadForm

def upload_excel(request):
    if request.method == 'POST':
        form = ExcelUploadForm(request.POST, request.FILES)
        if form.is_valid():
            excel_file = request.FILES['excel_file']
            if excel_file.name.endswith('.xls') or excel_file.name.endswith('.xlsx'):
                df = pd.read_excel(excel_file)
                # Process the data in df as needed
                # Map each Excel column to the corresponding model field
                mylist = [{'name': row['Name'], 'email':row['Email'], 'age':row['Age'], 'index':index+1} for index, row in df.iterrows()]
                return render(request, 'myapp/success.html', {'data': df.to_html(), 'mylist': mylist})
            else:
                return render(request, 'myapp/error.html', {'error_message': 'Invalid file format. Please upload an Excel file.'})
    else:
        form = ExcelUploadForm()
    
    return render(request, 'myapp/upload_excel.html', {'form': form})
