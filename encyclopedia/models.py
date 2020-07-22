from django.db import models

# Create your models here.
class entries(models.Model):
    """A typical class defining a model, derived from the Model class."""

    # Fields
    title = models.CharField(max_length=20)
    entry = models.TextField(max_length=200)

    # Metadata
    class Meta: 
        ordering = ['title']

    # Methods
     #def get_absolute_url(self):
      #   """Returns the url to access a particular instance of MyModelName."""
       #  return reverse('entry', args=[str(self.id)])
    
    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.title