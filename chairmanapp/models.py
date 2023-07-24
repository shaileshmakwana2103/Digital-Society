from django.db import models
from django.utils import timezone
import math

# Create your models here.

class User(models.Model):
    email = models.EmailField(unique=True,max_length=30,blank=False)
    password = models.CharField(max_length=20)
    role = models.CharField(max_length=30)
    is_active = models.BooleanField(default=False)
    is_verify = models.BooleanField(default=False)
    otp = models.IntegerField(default=456)
    created_at = models.DateTimeField(auto_now_add=True,blank=True,null=True)

    def __str__(self):
        return self.email

class Chairman(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    contact_no = models.CharField(max_length=30)
    pic = models.FileField(upload_to="media/upload",default="media/chairman.png")

    def __str__(self):
        return self.firstname

class Societymember(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    firstname = models.CharField(max_length=30,blank=True,null=True)
    lastname = models.CharField(max_length=30,blank=True,null=True)
    email = models.CharField(max_length=30,blank=True,null=True)
    contact_no = models.CharField(max_length=30,blank=True,null=True)
    occupation = models.CharField(max_length=30,blank=True,null=True)
    block_no = models.CharField(max_length=10,blank=True,null=True)
    No_of_familymembers = models.CharField(max_length=20,blank=True,null=True)
    dob = models.DateField(max_length=20,blank=True,null=True)
    vehical_details = models.CharField(max_length=30,blank=True,null=True)
    blood_group = models.CharField(max_length=10,blank=True,null=True)
    House_ownership = models.CharField(max_length=20,blank=True,null=True)
    City = models.CharField(max_length=20,blank=True,null=True)
    pic = models.FileField(upload_to="media/upload",default="media/default.png")

    def __str__(self):
        return self.firstname


class Notice(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True) 

    
    def count_view(self):
        ncount = NoticeViewDetails.objects.filter(notice_id = self.id).count()

        return ncount      


    def whenpublished(self):


        now = timezone.now()

        diff = now - self.created_at

        if diff.days == 0 and diff.seconds >= 0 and diff.seconds < 60:
            seconds = diff.seconds

            if seconds == 1:
                return str(seconds) + "second ago"
            
            else:
                return str(seconds) + "seconds ago"
        
        if diff.days == 0 and diff.seconds >= 60 and diff.seconds < 3600:
            minutes = math.floor(diff.seconds/60)

            if minutes == 1:
                return str(minutes) + "minutes ago"
            
            else:
                return str(minutes) + "minutes ago"
        
        if diff.days == 0 and diff.seconds >= 3600 and diff.seconds < 86400:
            hours = math.floor(diff.seconds/3600)

            if hours == 1:
                return str(hours) + "hours ago"
            else:
                return str(hours) + "hours ago"
            
        # 1 day to 30 days 
        if diff.days >= 1 and diff.days < 30:
            days = diff.days

            if days == 1:
                return str(days) + "days ago"
            else:
                return str(days) + "days ago"
            
        if diff.days >= 30 and diff.days < 365:
            months = math.floor(diff.days/30)

            if months == 1:
                return str(months) + "month ago"
            else:
                return str(months) + "month ago"
            
        if diff.days >= 365:
            years = math.floor(diff.days/365)

            if years == 1:
                return str(years) + "year ago"
            else:
                return str(years) + "year ago"



class NoticeViewDetails(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    notice_id = models.ForeignKey(Notice,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)   

class Events(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True) 


    def count_view(self):
        ecount = EventsViewDetails.objects.filter(event_id = self.id).count()

        return ecount      
    
    def whenpublished(self):


        now = timezone.now()

        diff = now - self.created_at

        if diff.days == 0 and diff.seconds >= 0 and diff.seconds < 60:
            seconds = diff.seconds

            if seconds == 1:
                return str(seconds) + "second ago"
            
            else:
                return str(seconds) + "seconds ago"
        
        if diff.days == 0 and diff.seconds >= 60 and diff.seconds < 3600:
            minutes = math.floor(diff.seconds/60)

            if minutes == 1:
                return str(minutes) + "minutes ago"
            
            else:
                return str(minutes) + "minutes ago"
        
        if diff.days == 0 and diff.seconds >= 3600 and diff.seconds < 86400:
            hours = math.floor(diff.seconds/3600)

            if hours == 1:
                return str(hours) + "hours ago"
            else:
                return str(hours) + "hours ago"
            
        # 1 day to 30 days 
        if diff.days >= 1 and diff.days < 30:
            days = diff.days

            if days == 1:
                return str(days) + "days ago"
            else:
                return str(days) + "days ago"
            
        if diff.days >= 30 and diff.days < 365:
            months = math.floor(diff.days/30)

            if months == 1:
                return str(months) + "month ago"
            else:
                return str(months) + "month ago"
            
        if diff.days >= 365:
            years = math.floor(diff.days/365)

            if years == 1:
                return str(years) + "year ago"
            else:
                return str(years) + "year ago"
            
class EventsViewDetails(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    event_id = models.ForeignKey(Events,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True) 
    
     


class Complaints(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True) 


    def count_view(self):
        ccount = ComplaintsViewDetails.objects.filter(complaint_id = self.id).count()

        return ccount      
    
    def whenpublished(self):


        now = timezone.now()

        diff = now - self.created_at

        if diff.days == 0 and diff.seconds >= 0 and diff.seconds < 60:
            seconds = diff.seconds

            if seconds == 1:
                return str(seconds) + "second ago"
            
            else:
                return str(seconds) + "seconds ago"
        
        if diff.days == 0 and diff.seconds >= 60 and diff.seconds < 3600:
            minutes = math.floor(diff.seconds/60)

            if minutes == 1:
                return str(minutes) + "minutes ago"
            
            else:
                return str(minutes) + "minutes ago"
        
        if diff.days == 0 and diff.seconds >= 3600 and diff.seconds < 86400:
            hours = math.floor(diff.seconds/3600)

            if hours == 1:
                return str(hours) + "hours ago"
            else:
                return str(hours) + "hours ago"
            
        # 1 day to 30 days 
        if diff.days >= 1 and diff.days < 30:
            days = diff.days

            if days == 1:
                return str(days) + "days ago"
            else:
                return str(days) + "days ago"
            
        if diff.days >= 30 and diff.days < 365:
            months = math.floor(diff.days/30)

            if months == 1:
                return str(months) + "month ago"
            else:
                return str(months) + "month ago"
            
        if diff.days >= 365:
            years = math.floor(diff.days/365)

            if years == 1:
                return str(years) + "year ago"
            else:
                return str(years) + "year ago"
            
class ComplaintsViewDetails(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    complaint_id = models.ForeignKey(Complaints,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True) 

class Maintainance(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE) # Chairman
    member_id = models.ForeignKey(Societymember,on_delete=models.CASCADE) # Societymembers
    title = models.CharField(max_length=36)
    amount = models.CharField(max_length=36)
    duedate = models.DateField(max_length=36)
    status = models.CharField(max_length=36,default="PENDING")


    

