from django.db import models

class tbl_stud(models.Model):
    

    Name=models.CharField(max_length=100)
    Place=models.CharField(max_length=80)
    Age=models.IntegerField()
    Mark=models.IntegerField()
    class Meta:
       db_table="tbl_stud" 
