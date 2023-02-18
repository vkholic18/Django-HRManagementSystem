from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
import datetime
from dateutil.relativedelta import relativedelta

from decimal import Decimal


class Employee(models.Model):
    POSITION_CHOICES = [
        ('CEO', 'Chief Executive Officer'),
        ('CTO', 'Chief Technology Officer'),
        ('Team Leader', 'Team Leader'),
        ('Employee', 'Employee'),
    ]
    full_name = models.CharField(max_length=50)
    birthday = models.DateField()
    email = models.EmailField()
    annual_salary = models.DecimalField(max_digits=10, decimal_places=2)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    first_day = models.DateField()
    position = models.CharField(max_length=20, choices=POSITION_CHOICES, default='Employee')

    def clean(self):
        if (self.birthday + relativedelta(years=18)) > datetime.date.today():
            raise ValidationError(_('Employee must be at least 18 years old.'))
        if self.first_day > datetime.date.today():
            raise ValidationError(_('First day cannot be in the future.'))

    def __str__(self):
        return self.full_name
    
    def annual_salary_usd(self):
        exchange_rate = Decimal('85.1')
        return (self.annual_salary / exchange_rate).quantize(Decimal('0.01'))
    
   


class Team(models.Model):
    name = models.CharField(max_length=50)
    team_leader = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True, related_name='team_leader_of')
    members = models.ManyToManyField(Employee, related_name='teams')
    
    def save(self, *args, **kwargs):
        update_employee_position = False
        
        # Check if the team leader has changed
        if self.pk is not None:
            original_team = Team.objects.get(pk=self.pk)
            if original_team.team_leader != self.team_leader:
                update_employee_position = True
        
        super().save(*args, **kwargs)
        
        # Update employee position if the team leader has changed
        if update_employee_position and original_team.team_leader is not None:
            original_team.team_leader.position = 'Employee'
            original_team.team_leader.save()
            
        if self.team_leader:
            self.team_leader.position = 'Team Leader'
            self.team_leader.save()


class EmployeeNotes(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    content = models.TextField()