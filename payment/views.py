from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings

def pay_view(request):
    if request.method == 'POST':
        ad_soyad = request.POST.get('adSoyad')
        telefon = request.POST.get('telefon')
        eposta = request.POST.get('eposta')
        notlar = request.POST.get('notlar')

        subject = f"Yeni Randevu Talebi: {ad_soyad}"
        message = f"""
        Web sitesinden yeni bir randevu talebi aldınız!

        KİŞİSEL BİLGİLER:
        -----------------
        Ad Soyad: {ad_soyad}
        Telefon: {telefon}
        E-posta: {eposta}
        
        EK NOTLAR:
        ----------
        {notlar if notlar else 'Belirtilmedi'}
        """
        
        try:
            send_mail(
                subject,
                message,
                settings.DEFAULT_FROM_EMAIL,
                ['elifnihan.psk@gmail.com'], # Form doldurulunca mailin kime gideceği
                fail_silently=False,
            )
            messages.success(request, 'Randevu talebiniz başarıyla alındı! Size en kısa sürede dönüş yapacağız.')
            return redirect('payment:pay') 
            
        except Exception as e:
            messages.error(request, 'Mesajınız gönderilirken bir hata oluştu. Lütfen daha sonra tekrar deneyin.')
            print(f"Mail hatası: {e}") 

    # Eğer form gönderilmediyse sayfayı normal bir şekilde yükle
    return render(request, 'payment/pay.html')
