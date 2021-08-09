from django.db import models

#------------------------------------------------------------------
class Pr0001(models.Model):
    author=models.ForeignKey("auth.User",on_delete=models.CASCADE,verbose_name="KULLANICI")
    title1=models.CharField(max_length=50,verbose_name="PROJE NO")
    title2=models.CharField(max_length=50,verbose_name="PROJE ADI")
    title3=models.CharField(max_length=50,verbose_name="MÜŞTERİ ADI")
    title4=models.CharField(max_length=50,verbose_name="SİPARİŞ ADETİ")
    title5=models.CharField(max_length=50,verbose_name="BAŞLAMA TARİHİ")
    title6=models.CharField(max_length=50,verbose_name="BİTİŞ TARİHİ")
    title7=models.CharField(max_length=50,verbose_name="PROJE SORUMLUSU")
    title8=models.CharField(max_length=50,verbose_name="İRTİBAT NUMARASI")
    content=models.TextField(verbose_name="AÇIKLAMA")
    created_date=models.DateTimeField(auto_now_add=True,verbose_name="OLUŞTURULMA TARİHİ")
    #Article ana sayfasıda ttle bilgisi vermek için.
    def __str__(self):
        return self.title1