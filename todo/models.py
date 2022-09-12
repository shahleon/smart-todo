from django.db import models


class List(models.Model):
    title_text = models.CharField(max_length=100)
    created_on = models.DateTimeField()
    updated_on = models.DateTimeField()

    objects = models.Manager()

    def __str__(self):
        return "%s" % self.title_text


class ListItem(models.Model):
    item_text = models.CharField(max_length=100)
    is_done = models.BooleanField(default=False)
    created_on = models.DateTimeField()
    list = models.ForeignKey(List, on_delete=models.CASCADE)

    objects = models.Manager()

    def __str__(self):
        return "%s: %s" % (self.item_text, self.is_done)
