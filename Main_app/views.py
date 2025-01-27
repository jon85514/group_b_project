from datetime import datetime, date

from django.db import connection
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.template import loader

from .models import LaborClass, SupplyClass, EquipmentClass
from .forms import NewLaborFormUsingModelForm, NewSupplyFormUsingModelForm, NewEquipmentFormUsingModelForm

# Create your views here.
def index(request):
    return render(request,"Main_app/index.html")


def showLaborCode(request):
    if request.method == "GET":
        labor = LaborClass.objects.all()
        #return a response to your template and add query_results to the context
        context = {
            "labor": labor
        }
        return render(request, 'Main_app/show_laborcode.html', context)


class AddNewLaborUsingModelForm(View):
    form_class = NewLaborFormUsingModelForm
    template_name = 'Main_app/new_labor_with_model_form.html'

    def get(self, request, *args, **kwargs):
        form = NewLaborFormUsingModelForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            # return HttpResponseRedirect(reverse("showLaborCode"))
            return redirect("../labor_code/")
        return render(request, self.template_name, {'form': form})


def update_labor(request, labor_class):
    mylabor = LaborClass.objects.get(labor_class=labor_class)
    template = loader.get_template('Main_app/update_labor.html')
    context = {
        "mylabor" : mylabor,
    }
    return HttpResponse(template.render(context, request))


def updaterecord(request, labor_class):
    # labor_class = request.POST['labor_class']
    billing_code = request.POST['billing_code']
    rates = request.POST['rates']
    active = request.POST['active']
    labor = LaborClass.objects.get(labor_class=labor_class)
    # labor.labor_class = labor_class
    labor.billing_code = billing_code
    labor.rates = rates
    labor.active = active
    labor.save()
    
    return redirect("../../")


def showSupplyCode(request):
    if request.method == "GET":
        supply = SupplyClass.objects.all()
        #return a response to your template and add query_results to the context
        context = {
            "supply": supply
        }
        return render(request, 'Main_app/show_supplycode.html', context)


class AddNewSupplyUsingModelForm(View):
    form_class = NewSupplyFormUsingModelForm
    template_name = 'Main_app/new_supply_with_model_form.html'

    def get(self, request, *args, **kwargs):
        form = NewSupplyFormUsingModelForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            # return HttpResponseRedirect(reverse("showLaborCode"))
            return redirect("../supply_code/")
        return render(request, self.template_name, {'form': form})



def showEquipmentCode(request):
    if request.method == "GET":
        equip = EquipmentClass.objects.all()
        #return a response to your template and add query_results to the context
        context = {
            "equipment": equip
        }
        return render(request, 'Main_app/show_equipmentcode.html', context)


class AddNewEquipmentUsingModelForm(View):
    form_class = NewEquipmentFormUsingModelForm
    template_name = 'Main_app/new_equipment_with_model_form.html'

    def get(self, request, *args, **kwargs):
        form = NewEquipmentFormUsingModelForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            # return HttpResponseRedirect(reverse("showLaborCode"))
            return redirect("../equipment_code/")
        return render(request, self.template_name, {'form': form})

