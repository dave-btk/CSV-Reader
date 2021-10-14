import csv
import io

from django.shortcuts import render, redirect, HttpResponseRedirect, HttpResponse
from .models import Product
from django.contrib import messages


# Create your views here.

def upload_file(request):
    if request.method == "POST":
        csvdata = request.FILES['file']
        if not csvdata.name.endswith('.csv'):
            messages.error(request, "THIS is not a CSV file!")
            return HttpResponseRedirect('/upload/')
        data = csvdata.read().decode('UTF-8')
        stringdata = io.StringIO(data)
        next(stringdata)
        for filedata in csv.reader(stringdata, delimiter=',', quotechar="|"):
            save = Product.objects.create(
                product_id=filedata[0],
                product_name=filedata[1],
                product_price=filedata[2],
                purchase_date=filedata[3],
            )
        fm = Product.objects.all()
        messages.success(request, "File Saved")
    else:
        fm = Product.objects.all()
    return render(request, 'uploadcsv.html', {'form': fm})
