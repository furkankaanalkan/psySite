from django.shortcuts import render
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings

# Create your views here.

def pay(request):
    return render(request, 'payment/pay.html')

def pay_view (request):
  if request.method == 'POST':
    ad_soyad = request.POST.get('adSoyad')
    telefon = request.POST.get('telefon')
    eposta = request.POST.get('eposta')
    notlar = request.POST.get('notlar')

    subject = f"Yeni Randevu Talebi: {ad_soyad}"
    message = f"""

          KISISEL BILGILER:
        ---------------------
          
          Ad Soyad: {ad_soyad}
          Telefon: {telefon}
          E-posta: {eposta}
          
        =====================

          EK NOT:
        ---------------------


        {notlar if notlar else 'not belirtilmedi :)'}
    
    """
    try:
      send_mail(subject,massage,settings.DEFAULT_FROM_EMAIL,['furkankaanforpo@gmail.com'],fail_silently = False )
      massages.success(request, 'Randevu talebiniz basari ile olusturuldu')
      return redirect ('payment:pay')
      
    except Exception as e:
      messages.error('Mesajiniz gonderilirken sorun olstu tekrar deneyiniz')
      print (f"Mail gonderme hatasi: {e}")
      return render(request, 'pay.html')




    