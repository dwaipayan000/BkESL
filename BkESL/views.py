from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.http import request
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView

from .models import Consumption, Billed_unit, Eht_consumer_unit, Vigilance_data, Image
from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import Sum, Count
import pandas as pd
import numpy as np

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class HomePageView(TemplateView):
    template_name = 'login.html'

@csrf_exempt
def search(request):
    global z
    if request.method == 'POST':

        name = request.POST.get('name')
        z = name

        return render(request, "homepage.html")
    else:
        return render(request, "search.html")


def consumption(request):
    global z

    SDO = Consumption.objects.filter(month=z).values_list('sdo', flat=True)
    SHARING = Consumption.objects.filter(month=z).values_list('sharing', flat=True)
    GSS = Consumption.objects.filter(month=z).values_list('gss', flat=True)
    FEEDER = Consumption.objects.filter(month=z).values_list('feeder', flat=True)
    KWH = Consumption.objects.filter(month=z).values_list('kwh', flat=True)

    context = {}
    context = {'sdo': SDO, 'sharing': SHARING, 'gss': GSS, 'feeder': FEEDER, 'kwh': KWH, }

    return render(request, 'consumption.html', context)


def consumption_d2(request):
    global z
    SDO = Consumption.objects.filter(month=z).values_list('sdo', flat=True).filter(sdo='2')
    SHARING = Consumption.objects.filter(month=z).values_list('sharing', flat=True).filter(sdo='2')
    GSS = Consumption.objects.filter(month=z).values_list('gss', flat=True).filter(sdo='2')
    FEEDER = Consumption.objects.filter(month=z).values_list('feeder', flat=True).filter(sdo='2')
    KWH = Consumption.objects.filter(month=z).values_list('kwh', flat=True).filter(sdo='2')

    context = {}
    context = {'sdo': SDO, 'sharing': SHARING, 'gss': GSS, 'feeder': FEEDER, 'kwh': KWH}
    return render(request, 'consumptionD2.html', context)


def consumption_d1(request):
    global z
    SDO = Consumption.objects.filter(month=z).values_list('sdo', flat=True).filter(sdo='1')
    SHARING = Consumption.objects.filter(month=z).values_list('sharing', flat=True).filter(sdo='1')
    GSS = Consumption.objects.filter(month=z).values_list('gss', flat=True).filter(sdo='1')
    FEEDER = Consumption.objects.filter(month=z).values_list('feeder', flat=True).filter(sdo='1')
    KWH = Consumption.objects.filter(month=z).values_list('kwh', flat=True).filter(sdo='1')

    context = {}
    context = {'sdo': SDO, 'sharing': SHARING, 'gss': GSS, 'feeder': FEEDER, 'kwh': KWH}
    return render(request, 'consumptionD1.html', context)


def consumption_d3(request):
    global z
    SDO = Consumption.objects.filter(month=z).values_list('sdo', flat=True).filter(sdo='3')
    SHARING = Consumption.objects.filter(month=z).values_list('sharing', flat=True).filter(sdo='3')
    GSS = Consumption.objects.filter(month=z).values_list('gss', flat=True).filter(sdo='3')
    FEEDER = Consumption.objects.filter(month=z).values_list('feeder', flat=True).filter(sdo='3')
    KWH = Consumption.objects.filter(month=z).values_list('kwh', flat=True).filter(sdo='3')

    context = {}
    context = {'sdo': SDO, 'sharing': SHARING, 'gss': GSS, 'feeder': FEEDER, 'kwh': KWH}
    return render(request, 'consumptionD3.html', context)


def consumption_d4(request):
    global z
    SDO = Consumption.objects.filter(month=z).values_list('sdo', flat=True).filter(sdo='4')
    SHARING = Consumption.objects.filter(month=z).values_list('sharing', flat=True).filter(sdo='4')
    GSS = Consumption.objects.filter(month=z).values_list('gss', flat=True).filter(sdo='4')
    FEEDER = Consumption.objects.filter(month=z).values_list('feeder', flat=True).filter(sdo='4')
    KWH = Consumption.objects.filter(month=z).values_list('kwh', flat=True).filter(sdo='4')

    context = {}
    context = {'sdo': SDO, 'sharing': SHARING, 'gss': GSS, 'feeder': FEEDER, 'kwh': KWH}
    return render(request, 'consumptionD4.html', context)


def consumption_d5(request):
    global z
    SDO = Consumption.objects.filter(month=z).values_list('sdo', flat=True).filter(sdo='5')
    SHARING = Consumption.objects.filter(month=z).values_list('sharing', flat=True).filter(sdo='5')
    GSS = Consumption.objects.filter(month=z).values_list('gss', flat=True).filter(sdo='5')
    FEEDER = Consumption.objects.filter(month=z).values_list('feeder', flat=True).filter(sdo='5')
    KWH = Consumption.objects.filter(month=z).values_list('kwh', flat=True).filter(sdo='5')

    context = {}
    context = {'sdo': SDO, 'sharing': SHARING, 'gss': GSS, 'feeder': FEEDER, 'kwh': KWH}
    return render(request, 'consumptionD5.html', context)


def consumption_d6(request):
    global z
    SDO = Consumption.objects.filter(month=z).values_list('sdo', flat=True).filter(sdo='6 & 9')
    SHARING = Consumption.objects.filter(month=z).values_list('sharing', flat=True).filter(sdo='6 & 9')
    GSS = Consumption.objects.filter(month=z).values_list('gss', flat=True).filter(sdo='6 & 9')
    FEEDER = Consumption.objects.filter(month=z).values_list('feeder', flat=True).filter(sdo='6 & 9')
    KWH = Consumption.objects.filter(month=z).values_list('kwh', flat=True).filter(sdo='6 & 9')

    context = {}
    context = {'sdo': SDO, 'sharing': SHARING, 'gss': GSS, 'feeder': FEEDER, 'kwh': KWH}
    return render(request, 'consumptionD6.html', context)


def consumption_d7(request):
    global z
    SDO = Consumption.objects.filter(month=z).values_list('sdo', flat=True).filter(sdo='7')
    SHARING = Consumption.objects.filter(month=z).values_list('sharing', flat=True).filter(sdo='7')
    GSS = Consumption.objects.filter(month=z).values_list('gss', flat=True).filter(sdo='7')
    FEEDER = Consumption.objects.filter(month=z).values_list('feeder', flat=True).filter(sdo='7')
    KWH = Consumption.objects.filter(month=z).values_list('kwh', flat=True).filter(sdo='7')

    context = {}
    context = {'sdo': SDO, 'sharing': SHARING, 'gss': GSS, 'feeder': FEEDER, 'kwh': KWH}
    return render(request, 'consumptionD7.html', context)


def consumption_d8(request):
    global z
    SDO = Consumption.objects.filter(month=z).values_list('sdo', flat=True).filter(sdo='8')
    SHARING = Consumption.objects.filter(month=z).values_list('sharing', flat=True).filter(sdo='8')
    GSS = Consumption.objects.filter(month=z).values_list('gss', flat=True).filter(sdo='8')
    FEEDER = Consumption.objects.filter(month=z).values_list('feeder', flat=True).filter(sdo='8')
    KWH = Consumption.objects.filter(month=z).values_list('kwh', flat=True).filter(sdo='8')

    context = {}
    context = {'sdo': SDO, 'sharing': SHARING, 'gss': GSS, 'feeder': FEEDER, 'kwh': KWH}
    return render(request, 'consumptionD8.html', context)


def sale(request):
    global z
    SDO = Billed_unit.objects.filter(month=z).values_list('sdo', flat=True)
    HT_SALE = Billed_unit.objects.filter(month=z).values_list('ht', flat=True)
    LT_SALE = Billed_unit.objects.filter(month=z).values_list('lt', flat=True)
    TOTAL_SALE = Billed_unit.objects.filter(month=z).values_list('total', flat=True)

    context = {}
    context = {'sdo': SDO, 'ht': HT_SALE, 'lt': LT_SALE, 'total': TOTAL_SALE}
    return render(request, 'sale.html', context)


def EHT(request):
    global z
    SDO = Eht_consumer_unit.objects.filter(month=z).values_list('sdo', flat=True)
    Consumer_name = Eht_consumer_unit.objects.filter(month=z).values_list('consumer_name', flat=True)
    billed_unit = Eht_consumer_unit.objects.filter(month=z).values_list('billed_unit', flat=True)

    context = {}
    context = {'sdo': SDO, 'consumer_name': Consumer_name, 'billed_unit': billed_unit}

    return render(request, 'EHT.html', context)


def Vigilance(request):
    global z
    SDO = Vigilance_data.objects.filter(month=z).values_list('sdo', flat=True)
    UNIT = Vigilance_data.objects.filter(month=z).values_list('unit', flat=True)
    context = {}
    context = {'sdo': SDO, 'unit': UNIT}
    return render(request, 'vigilance.html', context)


def loss(request):
    global z


    ##overall loss calculation for SDO-1##
    P1 = Consumption.objects.filter(month=z).filter(sdo='1').aggregate(Sum('kwh'))['kwh__sum']
    P1 = P1 / 1000000
    P1 = round(P1, 2)

    Q1 = Billed_unit.objects.filter(month=z).filter(sdo='1').aggregate(Sum('total'))['total__sum']
    Q1 = Q1 / 1000000
    Q1 = round(Q1, 2)

    S1 = Vigilance_data.objects.filter(month=z).filter(sdo='1').aggregate(Sum('unit'))['unit__sum']
    S1 = S1 / 1000000
    S1 = round(S1, 2)

    r1 = ((P1 - (Q1 + S1)) / P1) * 100
    r1 = round(r1, 2)

    ##overall loss calculation for SDO-2##
    P2 = Consumption.objects.filter(month=z).filter(sdo='2').aggregate(Sum('kwh'))['kwh__sum']
    P2 = P2 / 1000000
    P2 = round(P2, 2)

    R2 = Eht_consumer_unit.objects.filter(month=z).filter(sdo='2').aggregate(Sum('billed_unit'))['billed_unit__sum']
    R2 = R2 / 1000000
    R2 = round(R2, 2)
    P2 = P2 + R2

    Q2 = Billed_unit.objects.filter(month=z).filter(sdo='2').aggregate(Sum('total'))['total__sum']
    Q2 = Q2 / 1000000
    Q2 = round(Q2, 2)

    S2 = Vigilance_data.objects.filter(month=z).filter(sdo='2').aggregate(Sum('unit'))['unit__sum']
    S2 = S2 / 1000000
    S2 = round(S2, 2)

    r2 = (((P2) - (Q2 + S2)) / (P2)) * 100
    r2 = round(r2, 2)

    ##overall loss calculation for SDO-3##
    P3 = Consumption.objects.filter(month=z).filter(sdo='3').aggregate(Sum('kwh'))['kwh__sum']
    P3 = P3 / 1000000
    P3 = round(P3, 2)

    Q3 = Billed_unit.objects.filter(month=z).filter(sdo='3').aggregate(Sum('total'))['total__sum']
    Q3 = Q3 / 1000000
    Q3 = round(Q3, 2)

    S3 = Vigilance_data.objects.filter(month=z).filter(sdo='3').aggregate(Sum('unit'))['unit__sum']
    S3 = S3 / 1000000
    S3 = round(S3, 2)

    r3 = (((P3) - (Q3 + S3)) / (P3)) * 100
    r3 = round(r3, 2)

    ##overall loss calculation for SDO-4##
    P4 = Consumption.objects.filter(month=z).filter(sdo='4').aggregate(Sum('kwh'))['kwh__sum']
    P4 = P4 / 1000000
    P4 = round(P4, 2)

    Q4 = Billed_unit.objects.filter(month=z).filter(sdo='4').aggregate(Sum('total'))['total__sum']
    Q4 = Q4 / 1000000
    Q4 = round(Q4, 2)

    S4 = Vigilance_data.objects.filter(month=z).filter(sdo='4').aggregate(Sum('unit'))['unit__sum']
    S4 = S4 / 1000000
    S4 = round(S4, 2)

    r4 = (((P4) - (Q4 + S4)) / (P4)) * 100
    r4 = round(r4, 2)

    ##overall loss calculation for SDO-5##
    P5 = Consumption.objects.filter(month=z).filter(sdo='5').aggregate(Sum('kwh'))['kwh__sum']
    P5 = P5 / 1000000
    P5 = round(P5, 2)

    R5 = Eht_consumer_unit.objects.filter(month=z).filter(sdo='5').aggregate(Sum('billed_unit'))['billed_unit__sum']
    R5 = R5 / 1000000
    R5 = round(R5, 2)

    P5 = P5 + R5
    P5 = round(P5, 2)

    Q5 = Billed_unit.objects.filter(month=z).filter(sdo='5').aggregate(Sum('total'))['total__sum']
    Q5 = Q5 / 1000000
    Q5 = round(Q5, 2)

    S5 = Vigilance_data.objects.filter(month=z).filter(sdo='5').aggregate(Sum('unit'))['unit__sum']
    S5 = S5 / 1000000
    S5 = round(S5, 2)

    r5 = (((P5) - (Q5 + S5)) / (P5)) * 100
    r5 = round(r5, 2)

    ##overall loss calculation for SDO-6 & 9##
    P6 = Consumption.objects.filter(month=z).filter(sdo='6 & 9').aggregate(Sum('kwh'))['kwh__sum']
    P6 = P6 / 1000000
    P6 = round(P6, 2)

    R6 = Eht_consumer_unit.objects.filter(month=z).filter(sdo='6 & 9').aggregate(Sum('billed_unit'))['billed_unit__sum']
    R6 = R6 / 1000000
    R6 = round(R6, 2)

    P6 = P6 + R6
    P6 = round(P6, 2)

    Q6 = Billed_unit.objects.filter(month=z).filter(sdo='6 & 9').aggregate(Sum('total'))['total__sum']
    Q6 = Q6 / 1000000
    Q6 = round(Q6, 2)

    S6 = Vigilance_data.objects.filter(month=z).filter(sdo='6 & 9').aggregate(Sum('unit'))['unit__sum']
    S6 = S6 / 1000000
    S6 = round(S6, 2)

    r6 = ((P6 - (Q6 + S6)) / (P6)) * 100
    r6 = round(r6, 2)

    ##overall loss calculation for SDO-7##
    P7 = Consumption.objects.filter(month=z).filter(sdo='7').aggregate(Sum('kwh'))['kwh__sum']
    P7 = P7 / 1000000
    P7 = round(P7, 2)

    R7 = Eht_consumer_unit.objects.filter(month=z).filter(sdo='7').aggregate(Sum('billed_unit'))['billed_unit__sum']
    R7 = R7 / 1000000
    R7 = round(R7, 2)

    P7 = P7 + R7
    P7 = round(P7, 2)

    Q7 = Billed_unit.objects.filter(month=z).filter(sdo='7').aggregate(Sum('total'))['total__sum']
    Q7 = Q7 / 1000000
    Q7 = round(Q7, 2)

    S7 = Vigilance_data.objects.filter(month=z).filter(sdo='7').aggregate(Sum('unit'))['unit__sum']
    S7 = S7 / 1000000
    S7 = round(S7, 2)

    r7 = (((P7) - (Q7 + S7)) / (P7)) * 100
    r7 = round(r7, 2)

    ##overall loss calculation for SDO-8##
    P8 = Consumption.objects.filter(month=z).filter(sdo='8').aggregate(Sum('kwh'))['kwh__sum']
    P8 = P8 / 1000000
    P8 = round(P8, 2)

    Q8 = Billed_unit.objects.filter(month=z).filter(sdo='8').aggregate(Sum('total'))['total__sum']
    Q8 = Q8 / 1000000
    Q8 = round(Q8, 2)

    S8 = Vigilance_data.objects.filter(month=z).filter(sdo='8').aggregate(Sum('unit'))['unit__sum']
    S8 = S8 / 1000000
    S8 - round(S8, 2)

    r8 = (((P8) - (Q8 + S8)) / (P8)) * 100
    r8 = round(r8, 2)

    ##only LT loss calculation for SDO-1##

    A1 = Consumption.objects.filter(month=z).filter(sdo='1').aggregate(Sum('kwh'))['kwh__sum']
    B1 = Billed_unit.objects.filter(month=z).filter(sdo='1').aggregate(Sum('ht'))['ht__sum']
    C1 = Billed_unit.objects.filter(month=z).filter(sdo='1').aggregate(Sum('lt'))['lt__sum']
    E1 = Vigilance_data.objects.filter(month=z).filter(sdo='1').aggregate(Sum('unit'))['unit__sum']
    A1 = A1 / 1000000
    A1 = round(A1, 2)
    B1 = B1 / 1000000
    B1 = round(B1, 2)
    C1 = C1 / 1000000
    C1 = round(C1, 2)
    E1 = E1 / 1000000
    E1 = round(E1, 2)
    A1 = A1 - B1
    A1 = round(A1, 2)
    e1 = ((A1 - (C1 + E1)) / A1) * 100
    e1 = round(e1, 2)

    ##only LT loss calculation for SDO-2##

    A2 = Consumption.objects.filter(month=z).filter(sdo='2').aggregate(Sum('kwh'))['kwh__sum']
    B2 = Billed_unit.objects.filter(month=z).filter(sdo='2').aggregate(Sum('ht'))['ht__sum']
    C2 = Billed_unit.objects.filter(month=z).filter(sdo='2').aggregate(Sum('lt'))['lt__sum']
    D2 = Eht_consumer_unit.objects.filter(month=z).filter(sdo='2').aggregate(Sum('billed_unit'))['billed_unit__sum']
    E2 = Vigilance_data.objects.filter(month=z).filter(sdo='2').aggregate(Sum('unit'))['unit__sum']
    A2 = A2 / 1000000
    A2 = round(A2, 2)
    B2 = B2 / 1000000
    B2 = round(B2, 2)
    C2 = C2 / 1000000
    C2 = round(C2, 2)
    D2 = D2 / 1000000
    D2 = round(D2, 2)
    A2 = (A2 - (B2 - D2))
    A2 = round(A2, 2)
    E2 = E2 / 1000000
    E2 = round(E2, 2)
    e2 = ((A2 - (C2 + E2)) / A2) * 100
    e2 = round(e2, 2)

    ##only LT loss calculation for SDO-3##

    A3 = Consumption.objects.filter(month=z).filter(sdo='3').aggregate(Sum('kwh'))['kwh__sum']
    B3 = Billed_unit.objects.filter(month=z).filter(sdo='3').aggregate(Sum('ht'))['ht__sum']
    C3 = Billed_unit.objects.filter(month=z).filter(sdo='3').aggregate(Sum('lt'))['lt__sum']
    E3 = Vigilance_data.objects.filter(month=z).filter(sdo='3').aggregate(Sum('unit'))['unit__sum']
    A3 = A3 / 1000000
    A3 = round(A3, 2)
    B3 = B3 / 1000000
    B3 = round(B3, 2)
    C3 = C3 / 1000000
    C3 = round(C3, 2)
    A3 = (A3 - B3)
    A3 = round(A3, 2)
    E3 = E3 / 1000000
    E3 = round(E3, 2)
    e3 = ((A3 - (C3 + E3)) / A3) * 100
    e3 = round(e3, 2)

    ##only LT loss calculation for SDO-4##

    A4 = Consumption.objects.filter(month=z).filter(sdo='4').aggregate(Sum('kwh'))['kwh__sum']
    B4 = Billed_unit.objects.filter(month=z).filter(sdo='4').aggregate(Sum('ht'))['ht__sum']
    C4 = Billed_unit.objects.filter(month=z).filter(sdo='4').aggregate(Sum('lt'))['lt__sum']
    E4 = Vigilance_data.objects.filter(month=z).filter(sdo='4').aggregate(Sum('unit'))['unit__sum']
    A4 = A4 / 1000000
    A4 = round(A4, 2)
    B4 = B4 / 1000000
    B4 = round(B4, 2)
    C4 = C4 / 1000000
    C4 = round(C4, 2)
    E4 = E4 / 1000000
    E4 = round(E4, 2)
    A4 = (A4 - B4)
    A4 = round(A4, 2)

    e4 = ((A4 - (C4 + E4)) / A4) * 100
    e4 = round(e4, 2)

    ##only LT loss calculation for SDO-5##

    A5 = Consumption.objects.filter(month=z).filter(sdo='5').aggregate(Sum('kwh'))['kwh__sum']
    B5 = Billed_unit.objects.filter(month=z).filter(sdo='5').aggregate(Sum('ht'))['ht__sum']
    C5 = Billed_unit.objects.filter(month=z).filter(sdo='5').aggregate(Sum('lt'))['lt__sum']
    D5 = Eht_consumer_unit.objects.filter(month=z).filter(sdo='5').aggregate(Sum('billed_unit'))['billed_unit__sum']
    E5 = Vigilance_data.objects.filter(month=z).filter(sdo='5').aggregate(Sum('unit'))['unit__sum']
    A5 = A5 / 1000000
    A5 = round(A5, 2)
    B5 = B5 / 1000000
    B5 = round(B5, 2)
    C5 = C5 / 1000000
    C5 = round(C5, 2)
    D5 = D5 / 1000000
    D5 = round(D5, 2)
    A5 = (A5 - (B5 - D5))
    A5 = round(A5, 2)
    E5 = E5 / 1000000
    E5 = round(E5, 2)
    e5 = ((A5 - (C5 + E5)) / A5) * 100
    e5 = round(e5, 2)

    ##only LT loss calculation for SDO-6-9##

    A6 = Consumption.objects.filter(month=z).filter(sdo='6 & 9').aggregate(Sum('kwh'))['kwh__sum']

    B6 = Billed_unit.objects.filter(month=z).filter(sdo='6 & 9').aggregate(Sum('ht'))['ht__sum']
    C6 = Billed_unit.objects.filter(month=z).filter(sdo='6 & 9').aggregate(Sum('lt'))['lt__sum']
    D6 = Eht_consumer_unit.objects.filter(month=z).filter(sdo='6 & 9').aggregate(Sum('billed_unit'))['billed_unit__sum']
    E6 = Vigilance_data.objects.filter(month=z).filter(sdo='6 & 9').aggregate(Sum('unit'))['unit__sum']

    A6 = A6 / 1000000
    A6 = round(A6, 2)
    B6 = B6 / 1000000
    B6 = round(B6, 2)
    C6 = C6 / 1000000
    C6 = round(C6, 2)
    D6 = D6 / 1000000
    D6 = round(D6, 2)

    A6 = (A6 - (B6 - D6))
    A6 = round(A6, 2)
    E6 = E6 / 1000000
    E6 = round(E6, 2)
    e6 = ((A6 - (C6 + E6)) / A6) * 100
    e6 = round(e6, 2)

    ##only LT loss calculation for SDO-7##

    A7 = Consumption.objects.filter(month=z).filter(sdo='7').aggregate(Sum('kwh'))['kwh__sum']
    B7 = Billed_unit.objects.filter(month=z).filter(sdo='7').aggregate(Sum('ht'))['ht__sum']
    C7 = Billed_unit.objects.filter(month=z).filter(sdo='7').aggregate(Sum('lt'))['lt__sum']
    D7 = Eht_consumer_unit.objects.filter(month=z).filter(sdo='7').aggregate(Sum('billed_unit'))['billed_unit__sum']
    E7 = Vigilance_data.objects.filter(month=z).filter(sdo='7').aggregate(Sum('unit'))['unit__sum']
    E7 = E7 / 1000000
    E7 = round(E7, 2)
    A7 = A7 / 1000000
    A7 = round(A7, 2)
    B7 = B7 / 1000000
    B7 = round(B7, 2)
    C7 = C7 / 1000000
    C7 = round(C7, 2)
    D7 = D7 / 1000000
    D7 = round(D7, 2)

    A7 = (A7 - (B7 - D7))
    A7 = round(A7, 2)
    e7 = ((A7 - (E7 + C7)) / A7) * 100
    e7 = round(e7, 2)

    ##only LT loss calculation for SDO-8##

    A8 = Consumption.objects.filter(month=z).filter(sdo='8').aggregate(Sum('kwh'))['kwh__sum']
    B8 = Billed_unit.objects.filter(month=z).filter(sdo='8').aggregate(Sum('ht'))['ht__sum']
    C8 = Billed_unit.objects.filter(month=z).filter(sdo='8').aggregate(Sum('lt'))['lt__sum']
    E8 = Vigilance_data.objects.filter(month=z).filter(sdo='8').aggregate(Sum('unit'))['unit__sum']
    E8 = E8 / 1000000
    E8 = round(E8, 2)
    A8 = A8 / 1000000
    A8 = round(A8, 2)
    B8 = B8 / 1000000
    B8 = round(B8, 2)
    C8 = C8 / 1000000
    C8 = round(C8, 2)
    A8 = (A8 - B8)
    A8 = round(A8, 2)
    e8 = ((A8 - (C8 + E8)) / A8) * 100
    e8 = round(e8, 2)

    P10 = P1 + P2 + P3 + P4 + P5 + P6 + P7 + P8
    P10 = round(P10, 2)
    Q10 = Q1 + Q2 + Q3 + Q4 + Q5 + Q6 + Q7 + Q8
    Q10 = round(Q10, 2)
    r10 = ((P10 - Q10) / P10) * 100
    r10 = round(r10, 2)
    P = np.array([P1, P2, P3, P4, P5, P6, P7, P8, P10])

    Q = np.array([Q1, Q2, Q3, Q4, Q5, Q6, Q7, Q8, Q10])
    r = np.array([r1, r2, r3, r4, r5, r6, r7, r8, r10])
    SDO = Vigilance_data.objects.filter(month=z).values_list('sdo', flat=True)
    A10 = A1 + A2 + A3 + A4 + A5 + A6 + A7 + A8
    A10 = round(A10, 2)
    C10 = C1 + C2 + C3 + C4 + C5 + C6 + C7 + C8
    C10 = round(C10, 2)
    e10 = ((A10 - C10) / A10) * 100
    e10 = round(e10, 2)

    A = np.array([A1, A2, A3, A4, A5, A6, A7, A8, A10])

    C = np.array([C1, C2, C3, C4, C5, C6, C7, C8, C10])
    e = np.array([e1, e2, e3, e4, e5, e6, e7, e8, e10])
    MONTH = Vigilance_data.objects.filter(month=z).values_list('month', flat=True)

    context = {'month': MONTH, 'sdo': SDO, 'consumption': P, 'sale': Q, 'loss': r, 'consumption1': A, 'sale1': C,
               'loss1': e}
    return render(request, 'loss.html', context)


## Cumulative loss calculation ##

def cumulative(request):
    global z
    P = Consumption.objects.filter(month=z).aggregate(Sum('sl_no'))['sl_no__sum']
    Q = Consumption.objects.filter(month=z).aggregate(Count('sl_no'))['sl_no__count']
    R = P / Q
    P1 = Consumption.objects.filter(sl_no__gte=0, sl_no__lte=R).filter(sdo='1').aggregate(Sum('kwh'))['kwh__sum']
    P1 = P1 / 1000000
    P1 = round(P1, 2)

    Q1 = Billed_unit.objects.filter(sl_no__gte=0, sl_no__lte=R).filter(sdo='1').aggregate(Sum('total'))['total__sum']
    Q1 = Q1 / 1000000
    Q1 = round(Q1, 2)

    S1 = Vigilance_data.objects.filter(sl_no__gte=0, sl_no__lte=R).filter(sdo='1').aggregate(Sum('unit'))['unit__sum']
    S1 = S1 / 1000000
    S1 = round(S1, 2)

    r1 = (((P1) - (Q1 + S1)) / (P1)) * 100
    r1 = round(r1, 2)

    ##overall loss calculation for SDO-2##
    P2 = Consumption.objects.filter(sl_no__gte=0, sl_no__lte=R).filter(sdo='2').aggregate(Sum('kwh'))['kwh__sum']
    P2 = P2 / 1000000
    P2 = round(P2, 2)

    R2 = Eht_consumer_unit.objects.filter(sl_no__gte=0, sl_no__lte=R).filter(sdo='2').aggregate(Sum('billed_unit'))[
        'billed_unit__sum']
    R2 = R2 / 1000000
    R2 = round(R2, 2)
    P2 = P2 + R2
    P2 = round(P2, 2)

    Q2 = Billed_unit.objects.filter(sl_no__gte=0, sl_no__lte=R).filter(sdo='2').aggregate(Sum('total'))['total__sum']
    Q2 = Q2 / 1000000
    Q2 = round(Q2, 2)

    S2 = Vigilance_data.objects.filter(sl_no__gte=0, sl_no__lte=R).filter(sdo='2').aggregate(Sum('unit'))['unit__sum']
    S2 = S2 / 1000000
    S2 = round(S2, 2)

    r2 = (((P2) - (Q2 + S2)) / (P2)) * 100
    r2 = round(r2, 2)

    ##overall loss calculation for SDO-3##
    P3 = Consumption.objects.filter(sl_no__gte=0, sl_no__lte=R).filter(sdo='3').aggregate(Sum('kwh'))['kwh__sum']
    P3 = P3 / 1000000
    P3 = round(P3, 2)

    Q3 = Billed_unit.objects.filter(sl_no__gte=0, sl_no__lte=R).filter(sdo='3').aggregate(Sum('total'))['total__sum']
    Q3 = Q3 / 1000000
    Q3 = round(Q3, 2)

    S3 = Vigilance_data.objects.filter(sl_no__gte=0, sl_no__lte=R).filter(sdo='3').aggregate(Sum('unit'))['unit__sum']
    S3 = S3 / 1000000
    S3 = round(S3, 2)

    r3 = (((P3) - (Q3 + S3)) / (P3)) * 100
    r3 = round(r3, 2)

    ##overall loss calculation for SDO-4##
    P4 = Consumption.objects.filter(sl_no__gte=0, sl_no__lte=R).filter(sdo='4').aggregate(Sum('kwh'))['kwh__sum']
    P4 = P4 / 1000000
    P4 = round(P4, 2)

    Q4 = Billed_unit.objects.filter(sl_no__gte=0, sl_no__lte=R).filter(sdo='4').aggregate(Sum('total'))['total__sum']
    Q4 = Q4 / 1000000
    Q4 = round(Q4, 2)

    S4 = Vigilance_data.objects.filter(sl_no__gte=0, sl_no__lte=R).filter(sdo='4').aggregate(Sum('unit'))['unit__sum']
    S4 = S4 / 1000000
    S4 = round(S4, 2)

    r4 = (((P4) - (Q4 + S4)) / (P4)) * 100
    r4 = round(r4, 2)

    ##overall loss calculation for SDO-5##
    P5 = Consumption.objects.filter(sl_no__gte=0, sl_no__lte=R).filter(sdo='5').aggregate(Sum('kwh'))['kwh__sum']
    P5 = P5 / 1000000
    P5 = round(P5, 2)

    R5 = Eht_consumer_unit.objects.filter(sl_no__gte=0, sl_no__lte=R).filter(sdo='5').aggregate(Sum('billed_unit'))[
        'billed_unit__sum']
    R5 = R5 / 1000000
    R5 = round(R5, 2)

    P5 = P5 + R5
    P5 = round(P5, 2)

    Q5 = Billed_unit.objects.filter(sl_no__gte=0, sl_no__lte=R).filter(sdo='5').aggregate(Sum('total'))['total__sum']
    Q5 = Q5 / 1000000
    Q5 = round(Q5, 2)

    S5 = Vigilance_data.objects.filter(sl_no__gte=0, sl_no__lte=R).filter(sdo='5').aggregate(Sum('unit'))['unit__sum']
    S5 = S5 / 1000000
    S5 = round(S5, 2)

    r5 = (((P5) - (Q5 + S5)) / (P5)) * 100
    r5 = round(r5, 2)

    ##overall loss calculation for SDO-6 & 9##
    P6 = Consumption.objects.filter(sl_no__gte=0, sl_no__lte=R).filter(sdo='6 & 9').aggregate(Sum('kwh'))['kwh__sum']
    P6 = P6 / 1000000
    P6 = round(P6, 2)

    R6 = Eht_consumer_unit.objects.filter(sl_no__gte=0, sl_no__lte=R).filter(sdo='6 & 9').aggregate(Sum('billed_unit'))[
        'billed_unit__sum']
    R6 = R6 / 1000000
    R6 = round(R6, 2)

    P6 = P6 + R6
    P6 = round(P6, 2)

    Q6 = Billed_unit.objects.filter(sl_no__gte=0, sl_no__lte=R).filter(sdo='6 & 9').aggregate(Sum('total'))[
        'total__sum']
    Q6 = Q6 / 1000000
    Q6 = round(Q6, 2)

    S6 = Vigilance_data.objects.filter(sl_no__gte=0, sl_no__lte=R).filter(sdo='6 & 9').aggregate(Sum('unit'))[
        'unit__sum']
    S6 = S6 / 1000000
    S6 = round(S6, 2)

    r6 = ((P6 - (Q6 + S6)) / (P6)) * 100
    r6 = round(r6, 2)

    ##overall loss calculation for SDO-7##
    P7 = Consumption.objects.filter(sl_no__gte=0, sl_no__lte=R).filter(sdo='7').aggregate(Sum('kwh'))['kwh__sum']
    P7 = P7 / 1000000
    P7 = round(P7, 2)

    R7 = Eht_consumer_unit.objects.filter(sl_no__gte=0, sl_no__lte=R).filter(sdo='7').aggregate(Sum('billed_unit'))[
        'billed_unit__sum']
    R7 = R7 / 1000000
    R7 = round(R7, 2)

    P7 = P7 + R7
    P7 = round(P7, 2)

    Q7 = Billed_unit.objects.filter(sl_no__gte=0, sl_no__lte=R).filter(sdo='7').aggregate(Sum('total'))['total__sum']
    Q7 = Q7 / 1000000
    Q7 = round(Q7, 2)

    S7 = Vigilance_data.objects.filter(sl_no__gte=0, sl_no__lte=R).filter(sdo='7').aggregate(Sum('unit'))['unit__sum']
    S7 = S7 / 1000000
    S7 = round(S7, 2)

    r7 = (((P7) - (Q7 + S7)) / (P7)) * 100
    r7 = round(r7, 2)

    ##overall loss calculation for SDO-8##
    P8 = Consumption.objects.filter(sl_no__gte=0, sl_no__lte=R).filter(sdo='8').aggregate(Sum('kwh'))['kwh__sum']
    P8 = P8 / 1000000
    P8 = round(P8, 2)

    Q8 = Billed_unit.objects.filter(sl_no__gte=0, sl_no__lte=R).filter(sdo='8').aggregate(Sum('total'))['total__sum']
    Q8 = Q8 / 1000000
    Q8 = round(Q8, 2)

    S8 = Vigilance_data.objects.filter(sl_no__gte=0, sl_no__lte=R).filter(sdo='8').aggregate(Sum('unit'))['unit__sum']
    S8 = S8 / 1000000
    S8 - round(S8, 2)

    r8 = (((P8) - (Q8 + S8)) / (P8)) * 100
    r8 = round(r8, 2)

    ##only LT loss calculation for SDO-1##

    A1 = Consumption.objects.filter(sl_no__gte=0, sl_no__lte=R).filter(sdo='1').aggregate(Sum('kwh'))['kwh__sum']
    B1 = Billed_unit.objects.filter(sl_no__gte=0, sl_no__lte=R).filter(sdo='1').aggregate(Sum('ht'))['ht__sum']
    C1 = Billed_unit.objects.filter(sl_no__gte=0, sl_no__lte=R).filter(sdo='1').aggregate(Sum('lt'))['lt__sum']
    E1 = Vigilance_data.objects.filter(sl_no__gte=0, sl_no__lte=R).filter(sdo='1').aggregate(Sum('unit'))['unit__sum']
    A1 = A1 / 1000000
    A1 = round(A1, 2)
    B1 = B1 / 1000000
    B1 = round(B1, 2)
    C1 = C1 / 1000000
    C1 = round(C1, 2)
    E1 = E1 / 1000000
    E1 = round(E1, 2)
    A1 = A1 - B1
    A1 = round(A1, 2)
    e1 = ((A1 - (C1 + E1)) / A1) * 100
    e1 = round(e1, 2)

    ##only LT loss calculation for SDO-2##

    A2 = Consumption.objects.filter(sl_no__gte=0, sl_no__lte=R).filter(sdo='2').aggregate(Sum('kwh'))['kwh__sum']
    B2 = Billed_unit.objects.filter(sl_no__gte=0, sl_no__lte=R).filter(sdo='2').aggregate(Sum('ht'))['ht__sum']
    C2 = Billed_unit.objects.filter(sl_no__gte=0, sl_no__lte=R).filter(sdo='2').aggregate(Sum('lt'))['lt__sum']
    D2 = Eht_consumer_unit.objects.filter(sl_no__gte=0, sl_no__lte=R).filter(sdo='2').aggregate(Sum('billed_unit'))[
        'billed_unit__sum']
    E2 = Vigilance_data.objects.filter(sl_no__gte=0, sl_no__lte=R).filter(sdo='2').aggregate(Sum('unit'))['unit__sum']
    A2 = A2 / 1000000
    A2 = round(A2, 2)
    B2 = B2 / 1000000
    B2 = round(B2, 2)
    C2 = C2 / 1000000
    C2 = round(C2, 2)
    D2 = D2 / 1000000
    D2 = round(D2, 2)
    A2 = (A2 - (B2 - D2))
    A2 = round(A2, 2)
    E2 = E2 / 1000000
    E2 = round(E2, 2)
    e2 = ((A2 - (C2 + E2)) / A2) * 100
    e2 = round(e2, 2)

    ##only LT loss calculation for SDO-3##

    A3 = Consumption.objects.filter(sl_no__gte=0, sl_no__lte=R).filter(sdo='3').aggregate(Sum('kwh'))['kwh__sum']
    B3 = Billed_unit.objects.filter(sl_no__gte=0, sl_no__lte=R).filter(sdo='3').aggregate(Sum('ht'))['ht__sum']
    C3 = Billed_unit.objects.filter(sl_no__gte=0, sl_no__lte=R).filter(sdo='3').aggregate(Sum('lt'))['lt__sum']
    E3 = Vigilance_data.objects.filter(sl_no__gte=0, sl_no__lte=R).filter(sdo='3').aggregate(Sum('unit'))['unit__sum']
    A3 = A3 / 1000000
    A3 = round(A3, 2)
    B3 = B3 / 1000000
    B3 = round(B3, 2)
    C3 = C3 / 1000000
    C3 = round(C3, 2)
    A3 = (A3 - B3)
    A3 = round(A3, 2)
    E3 = E3 / 1000000
    E3 = round(E3, 2)
    e3 = ((A3 - (C3 + E3)) / A3) * 100
    e3 = round(e3, 2)

    ##only LT loss calculation for SDO-4##

    A4 = Consumption.objects.filter(sl_no__gte=0, sl_no__lte=R).filter(sdo='4').aggregate(Sum('kwh'))['kwh__sum']
    B4 = Billed_unit.objects.filter(sl_no__gte=0, sl_no__lte=R).filter(sdo='4').aggregate(Sum('ht'))['ht__sum']
    C4 = Billed_unit.objects.filter(sl_no__gte=0, sl_no__lte=R).filter(sdo='4').aggregate(Sum('lt'))['lt__sum']
    E4 = Vigilance_data.objects.filter(sl_no__gte=0, sl_no__lte=R).filter(sdo='4').aggregate(Sum('unit'))['unit__sum']
    A4 = A4 / 1000000
    A4 = round(A4, 2)
    B4 = B4 / 1000000
    B4 = round(B4, 2)
    C4 = C4 / 1000000
    C4 = round(C4, 2)
    E4 = E4 / 1000000
    E4 = round(E4, 2)
    A4 = (A4 - B4)
    A4 = round(A4, 2)

    e4 = ((A4 - (C4 + E4)) / A4) * 100
    e4 = round(e4, 2)

    ##only LT loss calculation for SDO-5##

    A5 = Consumption.objects.filter(sl_no__gte=0, sl_no__lte=R).filter(sdo='5').aggregate(Sum('kwh'))['kwh__sum']
    B5 = Billed_unit.objects.filter(sl_no__gte=0, sl_no__lte=R).filter(sdo='5').aggregate(Sum('ht'))['ht__sum']
    C5 = Billed_unit.objects.filter(sl_no__gte=0, sl_no__lte=R).filter(sdo='5').aggregate(Sum('lt'))['lt__sum']
    D5 = Eht_consumer_unit.objects.filter(sl_no__gte=0, sl_no__lte=R).filter(sdo='5').aggregate(Sum('billed_unit'))[
        'billed_unit__sum']
    E5 = Vigilance_data.objects.filter(sl_no__gte=0, sl_no__lte=R).filter(sdo='5').aggregate(Sum('unit'))['unit__sum']
    A5 = A5 / 1000000
    A5 = round(A5, 2)
    B5 = B5 / 1000000
    B5 = round(B5, 2)
    C5 = C5 / 1000000
    C5 = round(C5, 2)
    D5 = D5 / 1000000
    D5 = round(D5, 2)
    A5 = (A5 - (B5 - D5))
    A5 = round(A5, 2)
    E5 = E5 / 1000000
    E5 = round(E5, 2)
    e5 = ((A5 - (C5 + E5)) / A5) * 100
    e5 = round(e5, 2)

    ##only LT loss calculation for SDO-6-9##

    A6 = Consumption.objects.filter(sl_no__gte=0, sl_no__lte=R).filter(sdo='6 & 9').aggregate(Sum('kwh'))['kwh__sum']

    B6 = Billed_unit.objects.filter(sl_no__gte=0, sl_no__lte=R).filter(sdo='6 & 9').aggregate(Sum('ht'))['ht__sum']
    C6 = Billed_unit.objects.filter(sl_no__gte=0, sl_no__lte=R).filter(sdo='6 & 9').aggregate(Sum('lt'))['lt__sum']
    D6 = Eht_consumer_unit.objects.filter(sl_no__gte=0, sl_no__lte=R).filter(sdo='6 & 9').aggregate(Sum('billed_unit'))[
        'billed_unit__sum']
    E6 = Vigilance_data.objects.filter(sl_no__gte=0, sl_no__lte=R).filter(sdo='6 & 9').aggregate(Sum('unit'))[
        'unit__sum']

    A6 = A6 / 1000000
    A6 = round(A6, 2)
    B6 = B6 / 1000000
    B6 = round(B6, 2)
    C6 = C6 / 1000000
    C6 = round(C6, 2)
    D6 = D6 / 1000000
    D6 = round(D6, 2)

    A6 = (A6 - (B6 - D6))
    A6 = round(A6, 2)
    E6 = E6 / 1000000
    E6 = round(E6, 2)
    e6 = ((A6 - (C6 + E6)) / A6) * 100
    e6 = round(e6, 2)

    ##only LT loss calculation for SDO-7##

    A7 = Consumption.objects.filter(sl_no__gte=0, sl_no__lte=R).filter(sdo='7').aggregate(Sum('kwh'))['kwh__sum']
    B7 = Billed_unit.objects.filter(sl_no__gte=0, sl_no__lte=R).filter(sdo='7').aggregate(Sum('ht'))['ht__sum']
    C7 = Billed_unit.objects.filter(sl_no__gte=0, sl_no__lte=R).filter(sdo='7').aggregate(Sum('lt'))['lt__sum']
    D7 = Eht_consumer_unit.objects.filter(sl_no__gte=0, sl_no__lte=R).filter(sdo='7').aggregate(Sum('billed_unit'))[
        'billed_unit__sum']
    E7 = Vigilance_data.objects.filter(sl_no__gte=0, sl_no__lte=R).filter(sdo='7').aggregate(Sum('unit'))['unit__sum']
    E7 = E7 / 1000000
    E7 = round(E7, 2)
    A7 = A7 / 1000000
    A7 = round(A7, 2)
    B7 = B7 / 1000000
    B7 = round(B7, 2)
    C7 = C7 / 1000000
    C7 = round(C7, 2)
    D7 = D7 / 1000000
    D7 = round(D7, 2)

    A7 = (A7 - (B7 - D7))
    A7 = round(A7, 2)
    e7 = ((A7 - (E7 + C7)) / A7) * 100
    e7 = round(e7, 2)

    ##only LT loss calculation for SDO-8##

    A8 = Consumption.objects.filter(sl_no__gte=0, sl_no__lte=R).filter(sdo='8').aggregate(Sum('kwh'))['kwh__sum']
    B8 = Billed_unit.objects.filter(sl_no__gte=0, sl_no__lte=R).filter(sdo='8').aggregate(Sum('ht'))['ht__sum']
    C8 = Billed_unit.objects.filter(sl_no__gte=0, sl_no__lte=R).filter(sdo='8').aggregate(Sum('lt'))['lt__sum']
    E8 = Vigilance_data.objects.filter(sl_no__gte=0, sl_no__lte=R).filter(sdo='8').aggregate(Sum('unit'))['unit__sum']
    E8 = E8 / 1000000
    E8 = round(E8, 2)
    A8 = A8 / 1000000
    A8 = round(A8, 2)
    B8 = B8 / 1000000
    B8 = round(B8, 2)
    C8 = C8 / 1000000
    C8 = round(C8, 2)
    A8 = (A8 - B8)
    A8 = round(A8, 2)
    e8 = ((A8 - (C8 + E8)) / A8) * 100
    e8 = round(e8, 2)

    P10 = P1 + P2 + P3 + P4 + P5 + P6 + P7 + P8
    P10 = round(P10, 2)
    Q10 = Q1 + Q2 + Q3 + Q4 + Q5 + Q6 + Q7 + Q8
    Q10 = round(Q10, 2)
    r10 = ((P10 - Q10) / P10) * 100
    r10 = round(r10, 2)
    P = np.array([P1, P2, P3, P4, P5, P6, P7, P8, P10])

    Q = np.array([Q1, Q2, Q3, Q4, Q5, Q6, Q7, Q8, Q10])
    r = np.array([r1, r2, r3, r4, r5, r6, r7, r8, r10])
    SDO = Vigilance_data.objects.filter(month=z).values_list('sdo', flat=True)
    A10 = A1 + A2 + A3 + A4 + A5 + A6 + A7 + A8
    A10 = round(A10, 2)
    C10 = C1 + C2 + C3 + C4 + C5 + C6 + C7 + C8
    C10 = round(C10, 2)
    e10 = ((A10 - C10) / A10) * 100
    e10 = round(e10, 2)

    A = np.array([A1, A2, A3, A4, A5, A6, A7, A8, A10])

    C = np.array([C1, C2, C3, C4, C5, C6, C7, C8, C10])
    e = np.array([e1, e2, e3, e4, e5, e6, e7, e8, e10])
    MONTH = Vigilance_data.objects.filter(month=z).values_list('month', flat=True)

    context = {'month': MONTH, 'sdo': SDO, 'consumption': P, 'sale': Q, 'loss': r, 'consumption1': A, 'sale1': C,
               'loss1': e}
    return render(request, 'cumulative.html', context)


def comparison(request):
    global z

    P = Consumption.objects.filter(month=z).aggregate(Sum('sl_no'))['sl_no__sum']
    Q = Consumption.objects.filter(month=z).aggregate(Count('sl_no'))['sl_no__count']
    R = P / Q
    R = round(R, 1)

    P1 = Consumption.objects.filter(month=z).filter(sdo='1').aggregate(Sum('kwh'))['kwh__sum']
    P1 = P1 / 1000000
    P1 = round(P1, 2)

    Q1 = Billed_unit.objects.filter(month=z).filter(sdo='1').aggregate(Sum('total'))['total__sum']
    Q1 = Q1 / 1000000
    Q1 = round(Q1, 2)

    S1 = Vigilance_data.objects.filter(month=z).filter(sdo='1').aggregate(Sum('unit'))['unit__sum']
    S1 = S1 / 1000000
    S1 = round(S1, 2)

    r1 = ((P1 - (Q1 + S1)) / P1) * 100
    r1 = round(r1, 2)

    P11 = Consumption.objects.filter(sl_no=R - 1).filter(sdo='1').aggregate(Sum('kwh'))['kwh__sum']
    P11 = P11 / 1000000
    P11 = round(P11, 2)

    Q11 = Billed_unit.objects.filter(sl_no=R - 1).filter(sdo='1').aggregate(Sum('total'))['total__sum']
    Q11 = Q11 / 1000000
    Q11 = round(Q11, 2)

    S11 = Vigilance_data.objects.filter(sl_no=R - 1).filter(sdo='1').aggregate(Sum('unit'))['unit__sum']
    S11 = S11 / 1000000
    S11 = round(S11, 2)

    r11 = (((P11) - (Q11 + S11)) / (P11)) * 100
    r11 = round(r11, 2)
    r111 = ((r1 - r11) / r1) * 100
    r111=round(r111,2)
    P111 = ((P1 - P11) / P1) * 100
    P111=round(P111,2)
    Q111 = ((Q1 - Q11) / Q1) * 100
    Q111=round(Q111,2)
    ##overall loss calculation for SDO-2##
    P22 = Consumption.objects.filter(sl_no=R - 1).filter(sdo='2').aggregate(Sum('kwh'))['kwh__sum']
    P22 = P22 / 1000000
    P22 = round(P22, 2)

    R22 = Eht_consumer_unit.objects.filter(sl_no=R - 1).filter(sdo='2').aggregate(Sum('billed_unit'))['billed_unit__sum']
    R22 = R22 / 1000000
    R22 = round(R22, 2)
    P22 = P22 + R22
    P22 = round(P22, 2)

    Q22 = Billed_unit.objects.filter(sl_no=R - 1).filter(sdo='2').aggregate(Sum('total'))['total__sum']
    Q22 = Q22 / 1000000
    Q22 = round(Q22, 2)

    S22 = Vigilance_data.objects.filter(sl_no=R - 1).filter(sdo='2').aggregate(Sum('unit'))['unit__sum']
    S22 = S22 / 1000000
    S22 = round(S22, 2)

    r22 = (((P22) - (Q22 + S22)) / (P22)) * 100
    r22 = round(r22, 2)
    P2 = Consumption.objects.filter(month=z).filter(sdo='2').aggregate(Sum('kwh'))['kwh__sum']
    P2 = P2 / 1000000
    P2 = round(P2, 2)

    R2 = Eht_consumer_unit.objects.filter(month=z).filter(sdo='2').aggregate(Sum('billed_unit'))['billed_unit__sum']
    R2 = R2 / 1000000
    R2 = round(R2, 2)
    P2 = P2 + R2

    Q2 = Billed_unit.objects.filter(month=z).filter(sdo='2').aggregate(Sum('total'))['total__sum']
    Q2 = Q2 / 1000000
    Q2 = round(Q2, 2)

    S2 = Vigilance_data.objects.filter(month=z).filter(sdo='2').aggregate(Sum('unit'))['unit__sum']
    S2 = S2 / 1000000
    S2 = round(S2, 2)

    r2 = (((P2) - (Q2 + S2)) / (P2)) * 100
    r2 = round(r2, 2)


    r222 = ((r2 - r22) / r2) * 100
    r222=round(r222,2)
    P222 = ((P2 - P22) / P2) * 100
    P222=round(P222,2)
    Q222 = ((Q2 - Q22) / Q2) * 100
    Q222=round(Q222,2)

    ##overall loss calculation for SDO-3##
    P33 = Consumption.objects.filter(sl_no=R - 1).filter(sdo='3').aggregate(Sum('kwh'))['kwh__sum']
    P33 = P33 / 1000000
    P33 = round(P33, 2)

    Q33 = Billed_unit.objects.filter(sl_no=R - 1).filter(sdo='3').aggregate(Sum('total'))['total__sum']
    Q33 = Q33 / 1000000
    Q33 = round(Q33, 2)

    S33 = Vigilance_data.objects.filter(sl_no=R - 1).filter(sdo='3').aggregate(Sum('unit'))['unit__sum']
    S33 = S33 / 1000000
    S33 = round(S33, 2)

    r33 = (((P33) - (Q33 + S33)) / (P33)) * 100
    r33 = round(r33, 2)
    P3 = Consumption.objects.filter(month=z).filter(sdo='3').aggregate(Sum('kwh'))['kwh__sum']
    P3 = P3 / 1000000
    P3 = round(P3, 2)

    Q3 = Billed_unit.objects.filter(month=z).filter(sdo='3').aggregate(Sum('total'))['total__sum']
    Q3 = Q3 / 1000000
    Q3 = round(Q3, 2)

    S3 = Vigilance_data.objects.filter(month=z).filter(sdo='3').aggregate(Sum('unit'))['unit__sum']
    S3 = S3 / 1000000
    S3 = round(S3, 2)

    r3 = (((P3) - (Q3 + S3)) / (P3)) * 100
    r3 = round(r3, 2)

    r333 = ((r3 - r33) / r3) * 100
    r333=round(r333,2)
    P333 = ((P33- P33) / P3) * 100
    P333=round(P333,2)
    Q333 = ((Q3 - Q33) / Q3) * 100
    Q333=round(Q333,2)

    ##overall loss calculation for SDO-4##
    P44 = Consumption.objects.filter(sl_no=R - 1).filter(sdo='4').aggregate(Sum('kwh'))['kwh__sum']
    P44 = P44 / 1000000
    P44 = round(P44, 2)

    Q44 = Billed_unit.objects.filter(sl_no=R - 1).filter(sdo='4').aggregate(Sum('total'))['total__sum']
    Q44 = Q44 / 1000000
    Q44 = round(Q44, 2)

    S44 = Vigilance_data.objects.filter(sl_no=R - 1).filter(sdo='4').aggregate(Sum('unit'))['unit__sum']
    S44 = S44 / 1000000
    S44 = round(S44, 2)

    r44 = (((P44) - (Q44 + S44)) / (P44)) * 100
    r44 = round(r44, 2)
    P4 = Consumption.objects.filter(month=z).filter(sdo='4').aggregate(Sum('kwh'))['kwh__sum']
    P4 = P4 / 1000000
    P4 = round(P4, 2)

    Q4 = Billed_unit.objects.filter(month=z).filter(sdo='4').aggregate(Sum('total'))['total__sum']
    Q4 = Q4 / 1000000
    Q4 = round(Q4, 2)

    S4 = Vigilance_data.objects.filter(month=z).filter(sdo='4').aggregate(Sum('unit'))['unit__sum']
    S4 = S4 / 1000000
    S4 = round(S4, 2)

    r4 = (((P4) - (Q4 + S4)) / (P4)) * 100
    r4 = round(r4, 2)

    r444 = ((r4 - r44) / r4) * 100
    r444=round(r444,2)
    P444 = ((P4 - P44) / P4) * 100
    P444=round(P444,2)
    Q444 = ((Q4 - Q44) / Q4) * 100
    Q444=round(Q444,2)

    ##overall loss calculation for SDO-5##
    P55 = Consumption.objects.filter(sl_no=R - 1).filter(sdo='5').aggregate(Sum('kwh'))['kwh__sum']
    P55 = P55 / 1000000
    P55 = round(P55, 2)

    R55 = Eht_consumer_unit.objects.filter(sl_no=R - 1).filter(sdo='5').aggregate(Sum('billed_unit'))[
        'billed_unit__sum']
    R55 = R55 / 1000000
    R55 = round(R55, 2)

    P55 = P55 + R55
    P55 = round(P55, 2)
    P5 = Consumption.objects.filter(month=z).filter(sdo='5').aggregate(Sum('kwh'))['kwh__sum']
    P5 = P5 / 1000000
    P5 = round(P5, 2)

    R5 = Eht_consumer_unit.objects.filter(month=z).filter(sdo='5').aggregate(Sum('billed_unit'))['billed_unit__sum']
    R5 = R5 / 1000000
    R5 = round(R5, 2)

    P5 = P5 + R5
    P5 = round(P5, 2)

    Q5 = Billed_unit.objects.filter(month=z).filter(sdo='5').aggregate(Sum('total'))['total__sum']
    Q5 = Q5 / 1000000
    Q5 = round(Q5, 2)

    S5 = Vigilance_data.objects.filter(month=z).filter(sdo='5').aggregate(Sum('unit'))['unit__sum']
    S5 = S5 / 1000000
    S5 = round(S5, 2)

    r5 = (((P5) - (Q5 + S5)) / (P5)) * 100
    r5 = round(r5, 2)

    Q55 = Billed_unit.objects.filter(sl_no=R - 1).filter(sdo='5').aggregate(Sum('total'))['total__sum']
    Q55 = Q55 / 1000000
    Q55 = round(Q55, 2)

    S55 = Vigilance_data.objects.filter(sl_no=R - 1).filter(sdo='5').aggregate(Sum('unit'))['unit__sum']
    S55 = S55 / 1000000
    S55 = round(S55, 2)

    r55 = (((P55) - (Q55 + S55)) / (P55)) * 100
    r55 = round(r55, 2)
    r555 = ((r55 - r5) / r55) * 100
    r555=round(r555,2)
    P555 = ((P55 - P5) / P55) * 100
    P555=round(P555,2)
    Q555 = ((Q55 - Q5) / Q55) * 100
    Q555=round(Q555,2)

    ##overall loss calculation for SDO-6 & 9##
    P66 = Consumption.objects.filter(sl_no=R - 1).filter(sdo='6 & 9').aggregate(Sum('kwh'))['kwh__sum']
    P66 = P66 / 1000000
    P66 = round(P66, 2)

    R66 = Eht_consumer_unit.objects.filter(sl_no=R - 1).filter(sdo='6 & 9').aggregate(Sum('billed_unit'))[
        'billed_unit__sum']
    R66 = R66 / 1000000
    R66 = round(R66, 2)

    P66 = P66 + R66
    P66 = round(P66, 2)

    Q66 = Billed_unit.objects.filter(sl_no=R - 1).filter(sdo='6 & 9').aggregate(Sum('total'))[
        'total__sum']
    Q66 = Q66 / 1000000
    Q66 = round(Q66, 2)

    S66 = Vigilance_data.objects.filter(sl_no=R - 1).filter(sdo='6 & 9').aggregate(Sum('unit'))[
        'unit__sum']
    S66 = S66 / 1000000
    S66 = round(S66, 2)

    r66 = ((P66 - (Q66 + S66)) / (P66)) * 100
    r66 = round(r66, 2)
    P6 = Consumption.objects.filter(month=z).filter(sdo='6 & 9').aggregate(Sum('kwh'))['kwh__sum']
    P6 = P6 / 1000000
    P6 = round(P6, 2)

    R6 = Eht_consumer_unit.objects.filter(month=z).filter(sdo='6 & 9').aggregate(Sum('billed_unit'))['billed_unit__sum']
    R6 = R6 / 1000000
    R6 = round(R6, 2)

    P6 = P6 + R6
    P6 = round(P6, 2)

    Q6 = Billed_unit.objects.filter(month=z).filter(sdo='6 & 9').aggregate(Sum('total'))['total__sum']
    Q6 = Q6 / 1000000
    Q6 = round(Q6, 2)

    S6 = Vigilance_data.objects.filter(month=z).filter(sdo='6 & 9').aggregate(Sum('unit'))['unit__sum']
    S6 = S6 / 1000000
    S6 = round(S6, 2)

    r6 = ((P6 - (Q6 + S6)) / (P6)) * 100
    r6 = round(r6, 2)

    r666 = ((r6 - r66) / r6) * 100
    r666=round(r666,2)
    P666 = ((P6 - P66) / P6) * 100
    P666=round(P666,2)
    Q666 = ((Q6 - Q66) / Q6) * 100
    Q666=round(Q666,2)

    ##overall loss calculation for SDO-7##
    P77 = Consumption.objects.filter(sl_no=R - 1).filter(sdo='7').aggregate(Sum('kwh'))['kwh__sum']
    P77 = P77 / 1000000
    P77 = round(P77, 2)

    R77 = Eht_consumer_unit.objects.filter(sl_no=R - 1).filter(sdo='7').aggregate(Sum('billed_unit'))[
        'billed_unit__sum']
    R77 = R77 / 1000000
    R77 = round(R77, 2)

    P77 = P77 + R77
    P77 = round(P77, 2)

    Q77 = Billed_unit.objects.filter(sl_no=R - 1).filter(sdo='7').aggregate(Sum('total'))['total__sum']
    Q77 = Q77 / 1000000
    Q77 = round(Q77, 2)

    S77 = Vigilance_data.objects.filter(sl_no=R - 1).filter(sdo='7').aggregate(Sum('unit'))['unit__sum']
    S77 = S77 / 1000000
    S77 = round(S77, 2)

    r77 = (((P77) - (Q77 + S77)) / (P77)) * 100
    r77 = round(r77, 2)
    P7 = Consumption.objects.filter(month=z).filter(sdo='7').aggregate(Sum('kwh'))['kwh__sum']
    P7 = P7 / 1000000
    P7 = round(P7, 2)

    R7 = Eht_consumer_unit.objects.filter(month=z).filter(sdo='7').aggregate(Sum('billed_unit'))['billed_unit__sum']
    R7 = R7 / 1000000
    R7 = round(R7, 2)

    P7 = P7 + R7
    P7 = round(P7, 2)

    Q7 = Billed_unit.objects.filter(month=z).filter(sdo='7').aggregate(Sum('total'))['total__sum']
    Q7 = Q7 / 1000000
    Q7 = round(Q7, 2)

    S7 = Vigilance_data.objects.filter(month=z).filter(sdo='7').aggregate(Sum('unit'))['unit__sum']
    S7 = S7 / 1000000
    S7 = round(S7, 2)

    r7 = (((P7) - (Q7 + S7)) / (P7)) * 100
    r7 = round(r7, 2)

    r777 = ((r7 - r77) / r7) * 100
    r777=round(r777,2)
    P777 = ((P7 - P77) / P7) * 100
    P777=round(P777,2)
    Q777 = ((Q7 - Q77) / Q7) * 100
    Q777=round(Q777,2)

    ##overall loss calculation for SDO-8##
    P88 = Consumption.objects.filter(sl_no=R - 1).filter(sdo='8').aggregate(Sum('kwh'))['kwh__sum']
    P88 = P88 / 1000000
    P88 = round(P88, 2)

    Q88 = Billed_unit.objects.filter(sl_no=R - 1).filter(sdo='8').aggregate(Sum('total'))['total__sum']
    Q88 = Q88 / 1000000
    Q88 = round(Q88, 2)

    S88 = Vigilance_data.objects.filter(sl_no=R - 1).filter(sdo='8').aggregate(Sum('unit'))['unit__sum']
    S88 = S88 / 1000000
    S88 - round(S88, 2)

    r88 = (((P88) - (Q88 + S88)) / (P88)) * 100
    r88 = round(r88, 2)
    P8 = Consumption.objects.filter(month=z).filter(sdo='8').aggregate(Sum('kwh'))['kwh__sum']
    P8 = P8 / 1000000
    P8 = round(P8, 2)

    Q8 = Billed_unit.objects.filter(month=z).filter(sdo='8').aggregate(Sum('total'))['total__sum']
    Q8 = Q8 / 1000000
    Q8 = round(Q8, 2)

    S8 = Vigilance_data.objects.filter(month=z).filter(sdo='8').aggregate(Sum('unit'))['unit__sum']
    S8 = S8 / 1000000
    S8 - round(S8, 2)

    r8 = (((P8) - (Q8 + S8)) / (P8)) * 100
    r8 = round(r8, 2)

    r888 = ((r8 - r88) / r8) * 100
    r888=round(r888,2)
    P888 = ((P8 - P88) / P8) * 100
    P888=round(P888,2)
    Q888 = ((Q8 - Q88) / Q8) * 100
    Q888=round(Q888,2)

    ##only LT loss calculation for SDO-1##

    A11 = Consumption.objects.filter(sl_no=R - 1).filter(sdo='1').aggregate(Sum('kwh'))['kwh__sum']
    B11 = Billed_unit.objects.filter(sl_no=R - 1).filter(sdo='1').aggregate(Sum('ht'))['ht__sum']
    C11 = Billed_unit.objects.filter(sl_no=R - 1).filter(sdo='1').aggregate(Sum('lt'))['lt__sum']
    E11 = Vigilance_data.objects.filter(sl_no=R - 1).filter(sdo='1').aggregate(Sum('unit'))['unit__sum']
    A11 = A11 / 1000000
    A11 = round(A11, 2)
    B11 = B11 / 1000000
    B11 = round(B11, 2)
    C11 = C11 / 1000000
    C11 = round(C11, 2)
    E11 = E11 / 1000000
    E11 = round(E11, 2)
    A11 = A11 - B11
    A11 = round(A11, 2)
    e11 = ((A11 - (C11 + E11)) / A11) * 100
    e11 = round(e11, 2)
    A1 = Consumption.objects.filter(month=z).filter(sdo='1').aggregate(Sum('kwh'))['kwh__sum']
    B1 = Billed_unit.objects.filter(month=z).filter(sdo='1').aggregate(Sum('ht'))['ht__sum']
    C1 = Billed_unit.objects.filter(month=z).filter(sdo='1').aggregate(Sum('lt'))['lt__sum']
    E1 = Vigilance_data.objects.filter(month=z).filter(sdo='1').aggregate(Sum('unit'))['unit__sum']
    A1 = A1 / 1000000
    A1 = round(A1, 2)
    B1 = B1 / 1000000
    B1 = round(B1, 2)
    C1 = C1 / 1000000
    C1 = round(C1, 2)
    E1 = E1 / 1000000
    E1 = round(E1, 2)
    A1 = A1 - B1
    A1 = round(A1, 2)
    e1 = ((A1 - (C1 + E1)) / A1) * 100
    e1 = round(e1, 2)

    e111 = ((e1 - e11) / e1) * 100
    e111=round(e111,2)
    A111 = ((A1 - A11) / A1) * 100
    A111=round(A111,2)
    C111 = ((C1 - C11) / C1) * 100
    C111=round(C111,2)

    ##only LT loss calculation for SDO-2##

    A22 = Consumption.objects.filter(sl_no=R - 1).filter(sdo='2').aggregate(Sum('kwh'))['kwh__sum']
    B22 = Billed_unit.objects.filter(sl_no=R - 1).filter(sdo='2').aggregate(Sum('ht'))['ht__sum']
    C22 = Billed_unit.objects.filter(sl_no=R - 1).filter(sdo='2').aggregate(Sum('lt'))['lt__sum']
    D22 = Eht_consumer_unit.objects.filter(sl_no=R - 1).filter(sdo='2').aggregate(Sum('billed_unit'))[
        'billed_unit__sum']
    E22 = Vigilance_data.objects.filter(sl_no=R - 1).filter(sdo='2').aggregate(Sum('unit'))['unit__sum']
    A22 = A22 / 1000000
    A22 = round(A22, 2)
    B22 = B22 / 1000000
    B22 = round(B22, 2)
    C22 = C22 / 1000000
    C22 = round(C22, 2)
    D22 = D22 / 1000000
    D22 = round(D22, 2)
    A22 = (A22 - (B22 - D22))
    A22 = round(A22, 2)
    E22 = E22 / 1000000
    E22 = round(E22, 2)
    e22 = ((A22 - (C22 + E22)) / A22) * 100
    e22 = round(e22, 2)
    A2 = Consumption.objects.filter(month=z).filter(sdo='2').aggregate(Sum('kwh'))['kwh__sum']
    B2 = Billed_unit.objects.filter(month=z).filter(sdo='2').aggregate(Sum('ht'))['ht__sum']
    C2 = Billed_unit.objects.filter(month=z).filter(sdo='2').aggregate(Sum('lt'))['lt__sum']
    D2 = Eht_consumer_unit.objects.filter(month=z).filter(sdo='2').aggregate(Sum('billed_unit'))['billed_unit__sum']
    E2 = Vigilance_data.objects.filter(month=z).filter(sdo='2').aggregate(Sum('unit'))['unit__sum']
    A2 = A2 / 1000000
    A2 = round(A2, 2)
    B2 = B2 / 1000000
    B2 = round(B2, 2)
    C2 = C2 / 1000000
    C2 = round(C2, 2)
    D2 = D2 / 1000000
    D2 = round(D2, 2)
    A2 = (A2 - (B2 - D2))
    A2 = round(A2, 2)
    E2 = E2 / 1000000
    E2 = round(E2, 2)
    e2 = ((A2 - (C2 + E2)) / A2) * 100
    e2 = round(e2, 2)


    e222 = ((e2 - e22) / e2) * 100
    e222=round(e222,2)
    A222 = ((A2 - A22) / A2) * 100
    A222=round(A222,2)
    C222 = ((C2 - C22) / C2) * 100
    C222=round(C222,2)

    ##only LT loss calculation for SDO-3##

    A33 = Consumption.objects.filter(sl_no=R - 1).filter(sdo='3').aggregate(Sum('kwh'))['kwh__sum']
    B33 = Billed_unit.objects.filter(sl_no=R - 1).filter(sdo='3').aggregate(Sum('ht'))['ht__sum']
    C33 = Billed_unit.objects.filter(sl_no=R - 1).filter(sdo='3').aggregate(Sum('lt'))['lt__sum']
    E33 = Vigilance_data.objects.filter(sl_no=R - 1).filter(sdo='3').aggregate(Sum('unit'))['unit__sum']
    A33 = A33 / 1000000
    A33 = round(A33, 2)
    B33 = B33 / 1000000
    B33 = round(B33, 2)
    C33 = C33 / 1000000
    C33 = round(C33, 2)
    A33 = (A33 - B33)
    A33 = round(A33, 2)
    E33 = E33 / 1000000
    E33 = round(E33, 2)
    e33 = ((A33 - (C33 + E33)) / A33) * 100
    e33 = round(e33, 2)
    A3 = Consumption.objects.filter(month=z).filter(sdo='3').aggregate(Sum('kwh'))['kwh__sum']
    B3 = Billed_unit.objects.filter(month=z).filter(sdo='3').aggregate(Sum('ht'))['ht__sum']
    C3 = Billed_unit.objects.filter(month=z).filter(sdo='3').aggregate(Sum('lt'))['lt__sum']
    E3 = Vigilance_data.objects.filter(month=z).filter(sdo='3').aggregate(Sum('unit'))['unit__sum']
    A3 = A3 / 1000000
    A3 = round(A3, 2)
    B3 = B3 / 1000000
    B3 = round(B3, 2)
    C3 = C3 / 1000000
    C3 = round(C3, 2)
    A3 = (A3 - B3)
    A3 = round(A3, 2)
    E3 = E3 / 1000000
    E3 = round(E3, 2)
    e3 = ((A3 - (C3 + E3)) / A3) * 100
    e3 = round(e3, 2)

    e333 = ((e3 - e33) / e3) * 100
    e333=round(e333,2)
    A333 = ((A3 - A33) / A3) * 100
    A333=round(A333,2)
    C333 = ((C3 - C33) / C3) * 100
    C333=round(C333,2)

    ##only LT loss calculation for SDO-4##

    A44 = Consumption.objects.filter(sl_no=R - 1).filter(sdo='4').aggregate(Sum('kwh'))['kwh__sum']
    B44 = Billed_unit.objects.filter(sl_no=R - 1).filter(sdo='4').aggregate(Sum('ht'))['ht__sum']
    C44 = Billed_unit.objects.filter(sl_no=R - 1).filter(sdo='4').aggregate(Sum('lt'))['lt__sum']
    E44 = Vigilance_data.objects.filter(sl_no=R - 1).filter(sdo='4').aggregate(Sum('unit'))['unit__sum']
    A44 = A44 / 1000000
    A44 = round(A44, 2)
    B44 = B44 / 1000000
    B44 = round(B44, 2)
    C44 = C44 / 1000000
    C44 = round(C44, 2)
    E44 = E44 / 1000000
    E44 = round(E44, 2)
    A44 = (A44 - B44)
    A44 = round(A44, 2)
    A4 = Consumption.objects.filter(month=z).filter(sdo='4').aggregate(Sum('kwh'))['kwh__sum']
    B4 = Billed_unit.objects.filter(month=z).filter(sdo='4').aggregate(Sum('ht'))['ht__sum']
    C4 = Billed_unit.objects.filter(month=z).filter(sdo='4').aggregate(Sum('lt'))['lt__sum']
    E4 = Vigilance_data.objects.filter(month=z).filter(sdo='4').aggregate(Sum('unit'))['unit__sum']
    A4 = A4 / 1000000
    A4 = round(A4, 2)
    B4 = B4 / 1000000
    B4 = round(B4, 2)
    C4 = C4 / 1000000
    C4 = round(C4, 2)
    E4 = E4 / 1000000
    E4 = round(E4, 2)
    A4 = (A4 - B4)
    A4 = round(A4, 2)

    e4 = ((A4 - (C4 + E4)) / A4) * 100
    e4 = round(e4, 2)


    e44 = ((A44 - (C44 + E44)) / A44) * 100
    e44 = round(e44, 2)
    e444 = ((e4 - e44) / e4) * 100
    e444=round(e444,2)
    A444 = ((A4 - A44) / A4) * 100
    A444=round(A444,2)
    C444 = ((C4 - C44) / C4) * 100
    C444=round(C444,2)

    ##only LT loss calculation for SDO-5##

    A55 = Consumption.objects.filter(sl_no=R - 1).filter(sdo='5').aggregate(Sum('kwh'))['kwh__sum']
    B55 = Billed_unit.objects.filter(sl_no=R - 1).filter(sdo='5').aggregate(Sum('ht'))['ht__sum']
    C55 = Billed_unit.objects.filter(sl_no=R - 1).filter(sdo='5').aggregate(Sum('lt'))['lt__sum']
    D55 = Eht_consumer_unit.objects.filter(sl_no=R - 1).filter(sdo='5').aggregate(Sum('billed_unit'))[
        'billed_unit__sum']
    E55 = Vigilance_data.objects.filter(sl_no=R - 1).filter(sdo='5').aggregate(Sum('unit'))['unit__sum']
    A55 = A55 / 1000000
    A55 = round(A55, 2)
    B55 = B55 / 1000000
    B55 = round(B55, 2)
    C55 = C55 / 1000000
    C55 = round(C55, 2)
    D55 = D55 / 1000000
    D55 = round(D55, 2)
    A55 = (A55 - (B55 - D55))
    A55 = round(A55, 2)
    E55 = E55 / 1000000
    E55 = round(E55, 2)
    e55 = ((A55 - (C55 + E55)) / A55) * 100
    e55 = round(e55, 2)

    A5 = Consumption.objects.filter(month=z).filter(sdo='5').aggregate(Sum('kwh'))['kwh__sum']
    B5 = Billed_unit.objects.filter(month=z).filter(sdo='5').aggregate(Sum('ht'))['ht__sum']
    C5 = Billed_unit.objects.filter(month=z).filter(sdo='5').aggregate(Sum('lt'))['lt__sum']
    D5 = Eht_consumer_unit.objects.filter(month=z).filter(sdo='5').aggregate(Sum('billed_unit'))['billed_unit__sum']
    E5 = Vigilance_data.objects.filter(month=z).filter(sdo='5').aggregate(Sum('unit'))['unit__sum']
    A5 = A5 / 1000000
    A5 = round(A5, 2)
    B5 = B5 / 1000000
    B5 = round(B5, 2)
    C5 = C5 / 1000000
    C5 = round(C5, 2)
    D5 = D5 / 1000000
    D5 = round(D5, 2)
    A5 = (A5 - (B5 - D5))
    A5 = round(A5, 2)
    E5 = E5 / 1000000
    E5 = round(E5, 2)
    e5 = ((A5 - (C5 + E5)) / A5) * 100
    e5 = round(e5, 2)

    e555 = ((e5 - e55) / e5) * 100
    e555=round(e555,2)
    A555 = ((A5 - A55) / A5) * 100
    A555=round(A555,2)
    C555 = ((C5 - C55) / C5) * 100
    C555=round(C555,2)

    ##only LT loss calculation for SDO-6-9##

    A66 = Consumption.objects.filter(sl_no=R - 1).filter(sdo='6 & 9').aggregate(Sum('kwh'))['kwh__sum']

    B66 = Billed_unit.objects.filter(sl_no=R - 1).filter(sdo='6 & 9').aggregate(Sum('ht'))['ht__sum']
    C66 = Billed_unit.objects.filter(sl_no=R - 1).filter(sdo='6 & 9').aggregate(Sum('lt'))['lt__sum']
    D66 = Eht_consumer_unit.objects.filter(sl_no=R - 1).filter(sdo='6 & 9').aggregate(Sum('billed_unit'))[
        'billed_unit__sum']
    E66 = Vigilance_data.objects.filter(sl_no=R - 1).filter(sdo='6 & 9').aggregate(Sum('unit'))[
        'unit__sum']

    A66 = A66 / 1000000
    A66 = round(A66, 2)
    B66 = B66 / 1000000
    B66 = round(B66, 2)
    C66 = C66 / 1000000
    C66 = round(C66, 2)
    D66 = D66 / 1000000
    D66 = round(D66, 2)

    A66 = (A66 - (B66 - D66))
    A66 = round(A66, 2)
    E66 = E66 / 1000000
    E66 = round(E66, 2)
    e66 = ((A66 - (C66 + E66)) / A66) * 100
    e66 = round(e66, 2)
    A6 = Consumption.objects.filter(month=z).filter(sdo='6 & 9').aggregate(Sum('kwh'))['kwh__sum']

    B6 = Billed_unit.objects.filter(month=z).filter(sdo='6 & 9').aggregate(Sum('ht'))['ht__sum']
    C6 = Billed_unit.objects.filter(month=z).filter(sdo='6 & 9').aggregate(Sum('lt'))['lt__sum']
    D6 = Eht_consumer_unit.objects.filter(month=z).filter(sdo='6 & 9').aggregate(Sum('billed_unit'))['billed_unit__sum']
    E6 = Vigilance_data.objects.filter(month=z).filter(sdo='6 & 9').aggregate(Sum('unit'))['unit__sum']

    A6 = A6 / 1000000
    A6 = round(A6, 2)
    B6 = B6 / 1000000
    B6 = round(B6, 2)
    C6 = C6 / 1000000
    C6 = round(C6, 2)
    D6 = D6 / 1000000
    D6 = round(D6, 2)

    A6 = (A6 - (B6 - D6))
    A6 = round(A6, 2)
    E6 = E6 / 1000000
    E6 = round(E6, 2)
    e6 = ((A6 - (C6 + E6)) / A6) * 100
    e6 = round(e6, 2)

    e666 = ((e6 - e66) / e6) * 100
    e666=round(e666,2)
    A666 = ((A6 - A66) / A6) * 100
    A666=round(A666,2)
    C666 = ((C6 - C66) / C6) * 100
    C666=round(C666,2)

    ##only LT loss calculation for SDO-7##

    A77 = Consumption.objects.filter(sl_no=R - 1).filter(sdo='7').aggregate(Sum('kwh'))['kwh__sum']
    B77 = Billed_unit.objects.filter(sl_no=R - 1).filter(sdo='7').aggregate(Sum('ht'))['ht__sum']
    C77 = Billed_unit.objects.filter(sl_no=R - 1).filter(sdo='7').aggregate(Sum('lt'))['lt__sum']
    D77 = Eht_consumer_unit.objects.filter(sl_no=R - 1).filter(sdo='7').aggregate(Sum('billed_unit'))[
        'billed_unit__sum']
    E77 = Vigilance_data.objects.filter(sl_no=R - 1).filter(sdo='7').aggregate(Sum('unit'))['unit__sum']
    E77 = E77 / 1000000
    E77 = round(E77, 2)
    A77 = A77 / 1000000
    A77 = round(A77, 2)
    B77 = B77 / 1000000
    B77 = round(B77, 2)
    C77 = C77 / 1000000
    C77 = round(C77, 2)
    D77 = D77 / 1000000
    D77 = round(D77, 2)

    A77 = (A77 - (B77 - D77))
    A77 = round(A77, 2)
    e77 = ((A77 - (E77 + C77)) / A77) * 100
    e77 = round(e77, 2)
    A7 = Consumption.objects.filter(month=z).filter(sdo='7').aggregate(Sum('kwh'))['kwh__sum']
    B7 = Billed_unit.objects.filter(month=z).filter(sdo='7').aggregate(Sum('ht'))['ht__sum']
    C7 = Billed_unit.objects.filter(month=z).filter(sdo='7').aggregate(Sum('lt'))['lt__sum']
    D7 = Eht_consumer_unit.objects.filter(month=z).filter(sdo='7').aggregate(Sum('billed_unit'))['billed_unit__sum']
    E7 = Vigilance_data.objects.filter(month=z).filter(sdo='7').aggregate(Sum('unit'))['unit__sum']
    E7 = E7 / 1000000
    E7 = round(E7, 2)
    A7 = A7 / 1000000
    A7 = round(A7, 2)
    B7 = B7 / 1000000
    B7 = round(B7, 2)
    C7 = C7 / 1000000
    C7 = round(C7, 2)
    D7 = D7 / 1000000
    D7 = round(D7, 2)

    A7 = (A7 - (B7 - D7))
    A7 = round(A7, 2)
    e7 = ((A7 - (E7 + C7)) / A7) * 100
    e7 = round(e7, 2)

    e777 = ((e7 - e77) / e7) * 100
    e777=round(e777,2)
    A777 = ((A7 - A77) / A7) * 100
    A777=round(A777,2)
    C777 = ((C7 - C77) / C7) * 100
    C777=round(C777,2)

    ##only LT loss calculation for SDO-8##

    A88 = Consumption.objects.filter(sl_no=R - 1).filter(sdo='8').aggregate(Sum('kwh'))['kwh__sum']
    B88 = Billed_unit.objects.filter(sl_no=R - 1).filter(sdo='8').aggregate(Sum('ht'))['ht__sum']
    C88 = Billed_unit.objects.filter(sl_no=R - 1).filter(sdo='8').aggregate(Sum('lt'))['lt__sum']
    E88 = Vigilance_data.objects.filter(sl_no=R - 1).filter(sdo='8').aggregate(Sum('unit'))['unit__sum']
    E88 = E88 / 1000000
    E88 = round(E88, 2)
    A88 = A88 / 1000000
    A88 = round(A88, 2)
    B88 = B88 / 1000000
    B88 = round(B88, 2)
    C88 = C88 / 1000000
    C88 = round(C88, 2)
    A88 = (A88 - B88)
    A88 = round(A88, 2)
    e88 = ((A88 - (C88 + E88)) / A88) * 100
    e88 = round(e88, 2)

    A8 = Consumption.objects.filter(month=z).filter(sdo='8').aggregate(Sum('kwh'))['kwh__sum']
    B8 = Billed_unit.objects.filter(month=z).filter(sdo='8').aggregate(Sum('ht'))['ht__sum']
    C8 = Billed_unit.objects.filter(month=z).filter(sdo='8').aggregate(Sum('lt'))['lt__sum']
    E8 = Vigilance_data.objects.filter(month=z).filter(sdo='8').aggregate(Sum('unit'))['unit__sum']
    E8 = E8 / 1000000
    E8 = round(E8, 2)
    A8 = A8 / 1000000
    A8 = round(A8, 2)
    B8 = B8 / 1000000
    B8 = round(B8, 2)
    C8 = C8 / 1000000
    C8 = round(C8, 2)
    A8 = (A8 - B8)
    A8 = round(A8, 2)
    e8 = ((A8 - (C8 + E8)) / A8) * 100
    e8 = round(e8, 2)

    e888 = ((e8 - e88) / e8) * 100
    e888=round(e888,2)
    A888 = ((A8 - A88) / A8) * 100
    A888=round(A888,2)
    C888 = ((C8 - C88) / C8) * 100
    C888=round(C888,2)

    P101 = P11 + P22 + P33 + P44 + P55 + P66 + P77 + P88
    P101 = round(P101, 2)
    Q101 = Q11 + Q22 + Q33 + Q44 + Q55 + Q66 + Q77 + Q88
    Q101 = round(Q101, 2)
    r101 = ((P101 - Q101) / P101) * 100
    r101 = round(r101, 2)
    P10 = P1 + P2 + P3 + P4 + P5 + P6 + P7 + P8
    P10 = round(P10, 2)
    Q10 = Q1 + Q2 + Q3 + Q4 + Q5 + Q6 + Q7 + Q8
    Q10 = round(Q10, 2)
    r10 = ((P10 - Q10) / P10) * 100
    r10 = round(r10, 2)

    r1011 = ((r10 - r101) / r10) * 100
    r1011=round(r1011,2)
    P1011 = ((P10 - P101) / P10) * 100
    P1011=round(P1011,2)
    Q1011 = ((Q10 - Q101) / Q10) * 100
    Q1011=round(Q1011,2)
    P = np.array([P111, P222, P333, P444, P555, P666, P777, P888, P1011])

    Q = np.array([Q111, Q222, Q333, Q444, Q555, Q666, Q777, Q888, Q1011])
    r = np.array([r111, r222, r333, r444, r555, r666, r777, r888, r1011])
    SDO = Vigilance_data.objects.filter(month='July,20').values_list('sdo', flat=True)
    A101 = A11 + A22 + A33 + A44 + A55 + A66 + A77 + A88
    A101 = round(A101, 2)
    C101 = C11 + C22 + C33 + C44 + C55 + C66 + C77 + C88
    C101 = round(C101, 2)
    e101 = ((A101 - C101) / A101) * 100
    e101 = round(e101, 2)
    A10 = A1 + A2 + A3 + A4 + A5 + A6 + A7 + A8
    A10 = round(A10, 2)
    C10 = C1 + C2 + C3 + C4 + C5 + C6 + C7 + C8
    C10 = round(C10, 2)
    e10 = ((A10 - C10) / A10) * 100
    e10 = round(e10, 2)

    e1011 = ((e10 - e101) / e10) * 100
    e1011=round(e1011,2)
    A1011 = ((A10 - A101) / A10) * 100
    A1011=round(A1011,2)
    C1011 = ((C10 - C101) / C10) * 100
    C1011=round(C1011,2)


    A = np.array([A111, A222, A333, A444, A555, A666, A777, A888, A1011])

    C = np.array([C111, C222, C333, C444, C555, C666, C777, C888, C1011])
    e = np.array([e111, e222, e333, e444, e555, e666, e777, e888, e1011])
    MONTH = Vigilance_data.objects.filter(month=z).values_list('month', flat=True)

    context = {'sdo': SDO, 'consumption': P, 'sale': Q, 'loss': r, 'consumption1': A, 'sale1': C, 'loss1': e}
    return render(request, 'comparison.html', context)
