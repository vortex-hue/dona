from django.db import models

class CampaignCategory(models.Model):
    name = models.CharField(max_length=40)
    slug = models.SlugField()

    def __str__(self):
        return self.name

class CampaignModel(models.Model):
    category = models.ForeignKey(CampaignCategory, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    slug = models.SlugField()
    description = models.TextField()
    campaign_wallet = models.CharField(max_length=34)
    goal_amount = models.DecimalField(max_digits=10, decimal_places=2)
    current_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.title
    
    def calculate_percentage(self):
        if self.goal_amount > 0:
            return (self.current_amount / self.goal_amount) * 100
        else:
            return 0

class Donation(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    seed = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    message = models.TextField()
    campaign = models.ForeignKey(CampaignModel, on_delete=models.CASCADE)
     
    def __str__(self):
        return f"{self.name} donated to {self.campaign}"