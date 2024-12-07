from django.db import models

class BaseModel(models.Model):
    # Ortak alanlar
    created_at = models.DateTimeField(auto_now_add=True)  # Oluşturulma zamanı
    updated_at = models.DateTimeField(auto_now=True)      # Güncellenme zamanı

    class Meta:
        abstract = True  # Bu model soyut bir modeldir, yani veritabanında bir tablo oluşturmaz.
