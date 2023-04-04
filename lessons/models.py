from django.db import models
from django.core.validators import FileExtensionValidator



class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'


class Book(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100, null=True, blank=True)
    published_date = models.DateField(null=True, blank=True)
    publisher = models.CharField(max_length=100, null=True, blank=True)
    in_print = models.BooleanField(default=True)
    
    file = models.FileField(upload_to='books/', null=True, blank=True, validators=[FileExtensionValidator(allowed_extensions=['pdf', 'epub', 'mobi', 'azw3'])])

    def __str__(self):
        return self.title
    
    def get_file(self):
        return self.file.url
    
    def get_info(self):
        return f'{self.title} by {self.author}'
    
    def get_category(self):
        return self.category.name
    

class BookImage(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/books/', null=True, blank=True)

    def __str__(self):
        return self.book.title
    
class Archive(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100, null=True, blank=True)
    published_date = models.DateField(null=True, blank=True)
    publisher = models.CharField(max_length=100, null=True, blank=True)
    archive = models.FileField(upload_to='archives/', null=True, blank=True, validators=[FileExtensionValidator(allowed_extensions=['zip', 'rar', '7z'])])
    
    def __str__(self):
        return self.title
    
    def get_file(self):
        return self.archive.url
    
class ArchiveImage(models.Model):
    archive = models.ForeignKey(Archive, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/archives/', null=True, blank=True)

    def __str__(self):
        return self.archive.title
    

class Topic(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='images/topics/', null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

        
    def __str__(self):
        return self.title
    
    def get_info(self):
        return f'{self.title} - {self.description}'
    
    def get_category(self):
        return self.category.name
    

class TopicImage(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/topics/', null=True, blank=True)

    def __str__(self):
        return self.image.url if self.image else 'No image'
    


