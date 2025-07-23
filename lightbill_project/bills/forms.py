from django import forms
from .models import Bill

class BillForm(forms.ModelForm):
    bill_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'})
    )

    class Meta:
        model = Bill
        fields = ['apartment_number', 'resident_name', 'units_consumed', 'bill_date']
