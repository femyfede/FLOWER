from django.shortcuts import render
from django.views.decorators.http import require_POST
from .models import IrisPredictor 

def predict(request):
    prediction = None
    if request.method == 'POST' :
        sepal_length = request.POST.get('sepal_length')
        sepal_width = request.POST.get('sepal_width')
        petal_length = request.POST.get('petal_length')
        petal_width = request.POST.get('petal_width')
        prediction = IrisPredictor.predict(sepal_length,sepal_width,petal_length,petal_width)
        
    return render(request, 'pages/index.html', {'prediction': prediction})