from django.db import models



# parent model
class forum(models.Model):
    name = models.CharField(max_length=200, default="anonymous", verbose_name="שם")
    email = models.CharField(max_length=200, null=True, verbose_name="אימייל")
    topic = models.CharField(max_length=300, verbose_name="נושא")
    description = models.CharField(max_length=1000, blank=True, verbose_name="תיאור")
    date_created = models.DateTimeField(auto_now_add=True, null=True, verbose_name="תאריך")

    def __str__(self):
        return str(self.topic)


# child model
class Discussion(models.Model):
    forum = models.ForeignKey(forum, blank=True, on_delete=models.CASCADE, default=None, verbose_name="הנושא עליו תרצה להגיב")
    discuss = models.TextField(max_length=1000, default=None, verbose_name="התגובה")
    name = models.CharField(max_length=100, default=None, verbose_name="שם")

    def __str__(self):
        return str(self.forum)