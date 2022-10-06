from django.db import models
from django.contrib.auth.models import User

class List(models.Model):
    title_text = models.CharField(max_length=100)
    created_on = models.DateTimeField()
    updated_on = models.DateTimeField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    objects = models.Manager()

    def __str__(self):
        return "%s" % self.title_text


class ListItem(models.Model):
    # the name of a list item
    item_name = models.CharField(max_length=50, null=True, blank=True)
    # the text note of a list item
    item_text = models.CharField(max_length=100)
    is_done = models.BooleanField(default=False)
    created_on = models.DateTimeField()
    list = models.ForeignKey(List, on_delete=models.CASCADE)

    objects = models.Manager()

    def __str__(self):
        return "%s: %s" % (self.item_text, self.is_done)


class Template(models.Model):
    title_text = models.CharField(max_length=100)
    created_on = models.DateTimeField()
    updated_on = models.DateTimeField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    objects = models.Manager()

    def __str__(self):
        return "%s" % self.title_text


class TemplateItem(models.Model):
    item_text = models.CharField(max_length=100)
    created_on = models.DateTimeField()
    template = models.ForeignKey(Template, on_delete=models.CASCADE)

    objects = models.Manager()

    def __str__(self):
        return "%s" % self.item_text
