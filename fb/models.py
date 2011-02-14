from django.db import models



class User(models.Model):
    
    last_modified = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True




class FbUser(User):
    
    user_id = models.IntegerField(unique=True)



class LocalUser(User):
    
    pass