from django.db import models

class Category(models.Model):
    """ Categories people fit into """
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(default=['name'])
    description = models.CharField(max_length=200, blank=True)
    uri = models.CharField(max_length=200, default=True)

    def __unicode__(self):
        """ How to print the category """
        return self.name

    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"

class Person(models.Model):
    """ A person to be guessed """
    name = models.CharField(max_length=200)
    short_name = models.CharField(max_length=50, unique=True)
    category = models.ManyToManyField(Category)
    imageurl = models.URLField()
    verified = models.BooleanField()

    def __unicode__(self):
        """ How to print the person """
        return "%s (%s)" %(self.name, self.short_name)

    class Meta:
        verbose_name = "person"
        verbose_name_plural = "people"

class Quote(models.Model):
    """ A quote to guess the owner of """
    update_id = models.CharField(max_length=50, unique=True)
    text = models.CharField(max_length=150)
    author = models.ForeignKey(Person)
    posted = models.DateTimeField()
    vote_up = models.IntegerField(default=0)
    vote_down = models.IntegerField(default=0)

    def __unicode__(self):
        if len(self.text) > 15:
            text = self.text[0:13] + "..."
        else:
            text = self.text
        return text
