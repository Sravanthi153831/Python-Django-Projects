from django.db import models

class Robot(models.Model):
    name = models.CharField(max_length=100)
    robot_type = models.CharField(max_length=100)
    description = models.TextField()

    # Battery Monitoring
    battery_level = models.IntegerField(default=100)

    def battery_status(self):
        if self.battery_level <= 20:
            return "Needs Charging"
        elif self.battery_level <= 50:
            return "Low Battery"
        else:
            return "Active"

    def __str__(self):
        return self.name
