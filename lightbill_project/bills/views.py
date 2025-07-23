from django.shortcuts import render, redirect, get_object_or_404
from .models import Bill
from .forms import BillForm

def bill_list(request):
    bills = Bill.objects.all()
    return render(request, 'bills/bill_list.html', {'bills': bills})

def bill_create(request):
    form = BillForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('bill_list')
    return render(request, 'bills/bill_form.html', {'form': form})

def bill_update(request, pk):
    bill = get_object_or_404(Bill, pk=pk)
    form = BillForm(request.POST or None, instance=bill)
    if form.is_valid():
        form.save()
        return redirect('bill_list')
    return render(request, 'bills/bill_form.html', {'form': form})

def bill_delete(request, pk):
    bill = get_object_or_404(Bill, pk=pk)
    if request.method == 'POST':
        bill.delete()
        return redirect('bill_list')
    return render(request, 'bills/bill_delete.html', {'bill': bill})
