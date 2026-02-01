from django.db import models

class Pizza (models.Model):
    """Hold the name values"""
    name = models.CharField(max_length=100)
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        """Return a string representation of the model."""
        return self.name
    
class Topping(models.Model):
    """Return pizza name and type"""
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    date_added = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'toppings'
        
    def __str__(self):
        """Return a string representation of the topping."""
        return f"{self.name} on {self.pizza}"