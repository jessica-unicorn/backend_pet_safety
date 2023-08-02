from django.db import models

class ProductDetail(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    image_name = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name
