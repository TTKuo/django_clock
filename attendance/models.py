from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class SubmitAttendance(models.Model):

    class Meta:
        db_table = 'attendance'

    PLACES = (
        (1, 'GRC'),
        #(2, 'GRC 4F'),
    )
    IN_OUT = (
        (1, 'IN'),
        (0, 'OUT'),
    )

    staff = models.ForeignKey(get_user_model(), verbose_name="Member", on_delete=models.CASCADE, default=None)
    place = models.IntegerField(verbose_name='出勤場所名', choices=PLACES, default=None)

 

    in_out = models.IntegerField(verbose_name='IN/OUT', choices=IN_OUT, default=None)
    time = models.TimeField(verbose_name="打卡時間")
    date = models.DateField(verbose_name='打卡日')