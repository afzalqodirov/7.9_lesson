from django.db import models

class Lugat(models.Model):
    #Beton and Concrete are the same but in different rows
    name = models.CharField(max_length=50)

    desc = models.TextField()
    sinonim = models.ManyToManyField('self', blank=True)

    # related names
    relateds = models.ManyToManyField('self', blank=True)

    # 1 -> Beton and Бетон and Concrete
    unique_identificator = models.PositiveIntegerField() 

    # for example (0 -> Russian) or (1 -> Uzbek in latin)
    language = models.IntegerField() 

    def __str__(self):return self.name

    class Meta:
        unique_together = ('name', 'language')
        db_table = 'lugat'
