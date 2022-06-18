from django import forms

class Result(forms.Form):
    num1 = forms.CharField(label='Epsilon', max_length=200)
    num2 = forms.CharField(label='Minimum Samples', max_length=200)
    num3 = forms.CharField(label='Masukkan nomor cluster', max_length=200) 

