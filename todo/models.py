from django.db import models
from django.contrib.auth.models import User

class List(models.Model):
    title_text = models.CharField(max_length=100)
    created_on = models.DateTimeField()
    updated_on = models.DateTimeField()
    list_tag = models.CharField(max_length=50, default='none')
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    is_shared = models.BooleanField(default=False)

    objects = models.Manager()

    def __str__(self):
        return "%s" % self.title_text

class ListTags(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    tag_name = models.CharField(max_length=50, null=True, blank=True)
    created_on = models.DateTimeField()

    objects = models.Manager()

    def __str__(self):
        return "%s" % self.tag_name


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
        return "%s: %s" % (str(self.item_text), self.is_done)


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

class SharedUsers(models.Model):
    list_id = models.ForeignKey(List, on_delete=models.CASCADE)
    shared_user = models.CharField(max_length=200)

    objects = models.Manager()

    def __str__(self):
        return "%s" % str(self.list_id)

class SharedList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    shared_list_id = models.CharField(max_length=200)

    objects = models.Manager()

    def __str__(self):
        return "%s" % str(self.user)