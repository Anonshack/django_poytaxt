from django.db import models


class HomePage(models.Model):
    name_uz = models.CharField(max_length=200);
    description_uz = models.TextField(null=True);

    name_en = models.CharField(max_length=200);
    description_en = models.TextField(null=True);

    name_ru = models.CharField(max_length=200);
    description_ru = models.TextField(null=True);

# country_uz = models.CharField(max_length=255)
#     capital_uz = models.CharField(max_length=255)