from django.db import models

class ShowManager(models.Manager):

    def basic_validator(self, post_data):
        errors = {}
        if len(post_data['title']) < 1:
            errors['title'] = "Title must be at least one character long."
        if len(post_data['title']) > 50:
            errors['name'] = "Name must be less than fifty characters long."
        if len(post_data['desc']) < 1:
            errors['desc'] = "Description must be at least one character long."
        if len(post_data['desc']) > 250:
            errors['desc'] = "Description must be less than 250 characters long."
        return errors

class Show(models.Model):
   title = models.CharField(max_length = 50)
   network = models.CharField(max_length = 50)
   release_date = models.DateField()
   desc = models.TextField()
   created_at = models.DateTimeField(auto_now_add = True)
   updated_at = models.DateTimeField(auto_now = True)
   objects = ShowManager()