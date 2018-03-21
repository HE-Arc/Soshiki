from django.db import models
from django.contrib.auth.models import User
import datetime


class Table(models.Model):
    """
    Table for the kanban that will contain your
    organisation for one project.
    """
    name = models.CharField(max_length=200)
    favorite = models.BooleanField(default=False)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    background = models.FileField(blank=True, null=True)

    def __str__(self):
        return self.name


class List(models.Model):
    """
    Lists are sections of the Table.
    They'll contain cards that will be the tasks to do.
    """
    name = models.CharField(max_length=200)
    position = models.IntegerField()
    table = models.ForeignKey(Table, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Card(models.Model):
    """
    Cards that will be the tasks to do.
    They'll contain a title, a description,
    a deadline, some checklists, labels, etc...
    """
    title = models.CharField(max_length=200)
    deadline = models.DateTimeField('Deadline')
    description = models.TextField()
    file = models.FileField(blank=True, null=True)
    position = models.IntegerField()
    list = models.ForeignKey(List, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_deadline_info(self):
        if self.deadline.date() > datetime.datetime.now().date():
            if self.deadline.date() < datetime.date.today() + datetime.timedelta(days=1):
                return "bg-danger"
            else:
                return "bg-success"
        else:
            return "bg-warning"


class CheckList(models.Model):
    """
    List of tasks that are checkable.
    """
    name = models.CharField(max_length=200)
    card = models.ForeignKey(Card, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class OptionsList(models.Model):
    """
    Value of a checklist's element.
    """
    value = models.CharField(max_length=300)
    checkList = models.ForeignKey(CheckList, on_delete=models.CASCADE)

    def __str__(self):
        return self.value


class Label(models.Model):
    """
    A label is a text with a colorfull background.
    """
    name = models.CharField(max_length=200)
    color = models.CharField(max_length=7)
    card = models.ForeignKey(Card, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Comment(models.Model):
    """
    A card can contain several comments by the members of the table.
    """
    value = models.TextField()
    date = models.DateTimeField('published date')
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    card = models.ForeignKey(Card, on_delete=models.CASCADE)

    def __str__(self):
        return self.value
