from django.db import models

class HeroSection(models.Model):
    title = models.CharField(max_length=200, default="Hello, I'm SunnyCode")
    subtitle = models.CharField(max_length=200, default="Software Engineer & DevOps Specialist")
    background_image = models.ImageField(upload_to='hero/', blank=True, null=True)
    
    def __str__(self):
        return "Hero Section Settings"

    class Meta:
        verbose_name_plural = "Hero Section"

class AboutSection(models.Model):
    bio = models.TextField()
    profile_image = models.ImageField(upload_to='about/', blank=True, null=True)
    cv_file = models.FileField(upload_to='cv/', blank=True, null=True)
    
    def __str__(self):
        return "About Section Settings"

    class Meta:
        verbose_name_plural = "About Section"

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.name} - {self.subject}"
