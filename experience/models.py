from django.db import models

class Job(models.Model):
    company = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    is_current = models.BooleanField(default=False)
    description = models.TextField()
    logo = models.ImageField(upload_to='company_logos/', blank=True, null=True)
    
    class Meta:
        ordering = ['-start_date']

    def __str__(self):
        return f"{self.role} at {self.company}"

class Skill(models.Model):
    CATEGORY_CHOICES = [
        ('WEB', 'Web Development'),
        ('TOOLS', 'Tools & DevOps'),
        ('OTHER', 'Other'),
    ]
    
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    icon = models.ImageField(upload_to='skills/', blank=True, null=True)
    proficiency = models.IntegerField(default=80, help_text="Percentage (0-100)")
    
    def __str__(self):
        return self.name
