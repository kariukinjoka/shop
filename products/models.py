from django.db import models

# Create your models here.

class ItemMaster(models.Model):
    ITEM_CODE = models.CharField(max_length=50)
    ITEM_NAME = models.CharField(max_length=255)
    ITEM_IG_CODE = models.CharField(max_length=50)
    ITEM_UOM_CODE = models.CharField(max_length=50)
    ITEM_STK_NONSTK = models.CharField(max_length=10)
    CLASSIFICATION = models.CharField(max_length=50)
    PRODUCT_TYPE = models.CharField(max_length=50)
    BRAND = models.CharField(max_length=50)
    BRAND_CODE2 = models.CharField(max_length=50)
    CATEGORY = models.CharField(max_length=50)
    SPECIFICATION = models.CharField(max_length=255)
    SECTION_WIDTH = models.CharField(max_length=10)
    PROFILE = models.CharField(max_length=10)
    RIM_SIZE = models.CharField(max_length=10)
    PATTERN = models.CharField(max_length=50)
    PLAY_RATING = models.CharField(max_length=10)
    OTHER = models.CharField(max_length=255)
    VAT = models.CharField(max_length=50)

    def __str__(self):
        return self.ITEM_NAME
