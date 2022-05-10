import email
from email.utils import localtime
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Ordering(models.Model):
    STYLES = (
			('HARVARD', 'HARVARD'),
			('APA', 'APA'),
			('MLA', 'MLA'),
            ('CHICAGO', 'CHICAGO'),
            ('Any Other ', 'Any Other'),
			)
    topic= models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(max_length=200, null=True, blank=True)
    pages = models.FloatField(null=True, blank=True)
    style = models.CharField(max_length=200, null=True, blank=True, choices=STYLES, default='Select')
    deadline = models.DateTimeField(null=True, blank=True)
    files = models.FileField( upload_to="Upload_files/%Y%m%d/" , max_length=255,  blank=True, null=True,)
    budget=models.FloatField(null=False, blank=False, default=10)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return f"{self.topic}"  f"{self.deadline}" f"{self.budget}"


class Task(models.Model):
    STYLES = (
			('HARVARD', 'HARVARD'),
			('APA', 'APA'),
			('MLA', 'MLA'),
            ('CHICAGO', 'CHICAGO'),
            ('Other ', 'Other'),
			)
    PROGRESS = (
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
    )

    SPACING = (
        ('Single', 'Single'),
        ('1.5 lines', '1.5 lines'),
        ('Doudle', 'Double'),
        
       
    )

    FONTS = (
        ('Times New Roman', 'Times New Roman'),
        ('Arial', 'Arial'),
        ('Calibri', 'Calibri'),
       
    )


  
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    topic= models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(max_length=1000, null=True, blank=True)
    pages = models.FloatField(null=True, blank=True)
    font_family = models.CharField(max_length=200, null=True, blank=True, choices=FONTS, default='Select')
    line_spacing = models.CharField(max_length=200, null=True, blank=True, choices=SPACING, default='Select')
    style = models.CharField(max_length=200, null=True, blank=True, choices=STYLES, default='Select')
    time = models.DateTimeField("Deadline: Must be Formated> Y-D-M Hr:Min:Sec ",   default= localtime,  null=True, blank=True)
    files = models.FileField( upload_to="Upload_files/%Y%m%d/" , max_length=255,  blank=True, null=True,)
    budget=models.FloatField(null=False, blank=False, default=10)
    created = models.DateField(auto_now=True, null=True, blank=True)
    answer = models.FileField( upload_to="Answers/%Y%m%d/" , max_length=255,  blank=True, null=True)
    progress= models.BooleanField("Mark as Complete", default=False )
    paid = models.BooleanField(default=False )
    invoice= models.CharField(max_length=200, null=True, blank=True)
    
    def __str__(self):
        return self.topic

    class Meta:
        order_with_respect_to = 'user'


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    phone_number= models.IntegerField(blank=True, null=True)
    email= models.EmailField(blank=True, null= True)

    def __str__(self):
        return f'{self.user.username} Profile'