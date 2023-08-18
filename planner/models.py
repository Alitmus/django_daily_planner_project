from django.urls import reverse
from django.db import models


class Category(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self) :
        return self.name
    
    class Meta:
        verbose_name_plural='Categories'


class Activity(models.Model):
    class Meta:
        
        verbose_name_plural='Activities'
        

    class Priority(models.IntegerChoices):
        high=3, ('High')
        normal=2, ('Normal')
        low=1, ('Low')
        
    
    name=models.CharField(max_length=100)
    category=models.ManyToManyField(Category)
    priority=models.IntegerField(choices=Priority.choices,
                                 default=Priority.normal,
                                 verbose_name='Priority')
    
   
    def get_absolute_url(self):
        return reverse('activity_detail',kwargs={"pk":self.pk})

    def __str__(self) :
        return f" {self.name} "


class Action(models.Model):

    class Meta:
        verbose_name_plural='Actions'

    action=models.ForeignKey(Activity,on_delete=models.RESTRICT,null=True)
    start_time=models.TimeField()
    end_time=models.TimeField()
    date=models.DateField()    

    status_choices=(
    ('c','Complete'),
    ('o','Ongoing'),
    ('i','Incomplete'),
    )
    status=models.CharField(max_length=1,choices=status_choices,blank=False,default='i')

   
    class Meta:
        ordering=['start_time']


    def __str__(self) :
        return f" {self.action} {self.start_time} {self.end_time} {self.date} {self.status}"
