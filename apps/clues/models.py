from django.db import models
from passlib.hash import pbkdf2_sha256
# Create your models here.


class Clue(models.Model):
    clue_no = models.IntegerField(default=0)
    question = models.TextField()
    ans1 = models.CharField(max_length=300)
    ans2 = models.CharField(max_length=300, null='True')

    def __str__(self):
        return str(self.clue_no)

    # Case insensitive verification
    def verify(self, ans):
        if(ans == self.ans1.lower() or ans == self.ans2.lower()):
            return True

    # Case sensitive verification
    # def verify(self, ans):
    #     if(pbkdf2_sha256.verify(ans,self.ans1) or pbkdf2_sha256.verify(ans,self.ans2)):
    #         return True


#STEM-ED-Hackathon Code - Anything below this line

#Model for a descriptive question
class DescQtn(models.Model): 
    q_no = models.IntegerField(default=0)
    q_heading = models.CharField(max_length=300, null=True, blank=True)
    question = models.TextField()

    def __str__(self):
        return str(self.q_no)
