from django.db import models
from poste import models as posteModels
from user import models as userModels
# Create your models here.
class reaction(models.Model):
    comment = models.CharField(max_length=512)
    like = models.BooleanField(default=False)
    post = models.ForeignKey(posteModels.Post, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(userModels.User, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return f"comment: {self.comment} like: {self.like}"