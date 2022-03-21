import pdb
from statistics import mode
from django.db import models
import secrets
from openpyxl import Workbook

# Create your models here.
class AttendanceURLToken(models.Model):
    url_token = models.CharField(max_length=100, blank=False, null=False, unique=True, editable=False, primary_key=True)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.url_token
    
    def save(self, *args, **kwargs):
        token = secrets.token_urlsafe(8)
        self.url_token = token
        wb = Workbook()
        wb.save(filename=f"apps/attendance/static/attendance/{token}.xlsx")
        
        super().save(*args, **kwargs)
            

        