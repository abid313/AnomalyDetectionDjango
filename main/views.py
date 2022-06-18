from django.shortcuts import render
from .forms import Result
from .anomalydata import AnomalyData

# Create your views here.
def home(response):
    form = Result()
    return render(response, 'main/home.html', {"form" : form})

def result(response):
    if response.method == "POST":
        form = Result(response.POST)

        if form.is_valid():
            epsilon = float(form.cleaned_data['num1'])
            minsamples = int(form.cleaned_data['num2'])
            nocluster = int(form.cleaned_data['num3'])
            count = AnomalyData(epsilon, minsamples, nocluster)

            return render(response, 'main/result.html', {"result" : count})

    else:
        form = Result()

    return render(response, 'main/result.html', {"form" : form})
