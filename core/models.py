from django.db import models
from user.models import usermodel

# Create your models here.

class trackModel(models.Model):
    difficulty = [
        ('1','Easy'),
        ('2','Intermediate'),
        ('3','Hard'),
        ('4', 'Very Hard'),
        ('5', 'Expert')
    ]
    featured_image = models.ImageField(default='noimage.svg')
    track_name = models.CharField(max_length=200)
    track_difficulty = models.CharField(max_length=1, choices=difficulty, default='1')
    track_description = models.TextField()
    track_map_url = models.URLField(null=True)
    track_state= models.CharField(max_length=200, default='City')
    track_city= models.CharField(max_length=200, default='City')
    track_locality = models.CharField(max_length=200, default='City')
    track_location_extra = models.CharField(max_length=200)
    track_status = models.BooleanField(default=True)
    track_created = models.DateTimeField(auto_now_add=True, null=True)
    track_updated = models.DateTimeField(auto_now=True, null=True)
    

    def __str__(self):
        return self.track_name

class bookingModel(models.Model):
    time = [
    ('1', '09:00 - 12:00'),
    ('2', '12:00 - 15:00'),
    ('3', '15:00 - 18:00'),
    ]
    booking_user = models.ForeignKey(usermodel, on_delete=models.CASCADE)
    booking_date = models.DateField()
    booking_track = models.ForeignKey(trackModel, on_delete=models.PROTECT)
    booking_time = models.CharField(max_length=1, choices=time, null=True)
    booking_charge = models.CharField(max_length=200, default=0)
    booking_status = models.BooleanField(default=False)
    booking_created = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['booking_track','booking_date','booking_time'], name = 'uniq_track_date_time_slot'
            )
        ]

    def __str__(self):
        return self.booking_user.username
    
class eventModel(models.Model):
    featured_image = models.ImageField(default='noimage.svg', upload_to="eventposters/", null=True, blank=True)
    event_name = models.CharField(max_length=200)
    event_date = models.DateField()
    event_start = models.TimeField()
    event_end = models.TimeField()
    event_location = models.TextField()
    event_state= models.CharField(max_length=200)
    event_city= models.CharField(max_length=200)
    event_locality = models.CharField(max_length=200)
    event_short_intro = models.CharField(max_length=200)
    event_charges = models.IntegerField()
    event_description = models.TextField()
    event_location_extra = models.CharField(max_length=200)
    event_created = models.DateTimeField(auto_now_add=True, null=True)
    event_updated = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.event_name

class eventBookingModel(models.Model):
    event_booking_user = models.ForeignKey(usermodel, on_delete=models.PROTECT)
    event_booking_event = models.ForeignKey(eventModel, on_delete=models.PROTECT)
    event_booking_status = models.BooleanField(default=True)
    booking_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.event_booking_user
