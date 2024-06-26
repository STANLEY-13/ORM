# Ex02 Django ORM Web Application
## Date: 28/02/2024

## AIM
To develop a Django application to store and retrieve data from a Book database using Object Relational Mapping(ORM).

## Entity Relationship Diagram
![er diagram1](https://github.com/STANLEY-13/ORM/assets/148198816/cfa59c14-fc03-4b01-b30f-9f1e1232b462)



## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM
```
admin.py

from django.contrib import admin
from .models import books_DB,books_DBAdmin
admin.site.register(books_DB,books_DBAdmin)

models.py 

from django.db import models 
from django.contrib import admin 
class books_DB(models.Model): 
    refno=models.IntegerField(primary_key="refno");
    bookname=models.CharField(max_length=20); 
    email=models.EmailField();
    Doissued=models.DateField();
    reviews=models.CharField(max_length=20);
class books_DBAdmin(admin.ModelAdmin):
    list_display=("refno", "bookname", "email", "Doissued", "reviews");
```

## OUTPUT
![image](https://github.com/STANLEY-13/ORM/assets/148198816/f4faf57c-af36-49af-ad6b-a22cd32e38d3)

## RESULT
Thus the program for creating a database using ORM hass been executed successfully
