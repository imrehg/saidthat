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
    name = models.CharField(max_length=200, default=True)
    screenname = models.CharField(max_length=50, unique=True, default='-missing-')
    description = models.CharField(max_length=200, default=True)
    imageurl = models.URLField(default=True)
    url = models.URLField(default=True)
    verified = models.BooleanField()
    location = models.CharField(max_length=200, default=True)
    twitterid = models.CharField(max_length=200, default=True)
    category = models.ManyToManyField(Category)

    def __unicode__(self):
        """ How to print the person """
        return "%s (%s)" %(self.name, self.screenname)

    class Meta:
        verbose_name = "person"
        verbose_name_plural = "people"

class Quote(models.Model):
    """ A quote to guess the owner of """
    updateid = models.CharField(max_length=50, unique=True, default=0)
    text = models.CharField(max_length=150, blank=True)
    author = models.ForeignKey(Person, blank=True)
    posted = models.DateTimeField(blank=True)
    voteup = models.IntegerField(default=0)
    votedown = models.IntegerField(default=0)

    def __unicode__(self):
        if len(self.text) > 15:
            text = self.text[0:13] + "..."
        else:
            text = self.text
        return text

class Puzzle(models.Model):
    """ A puzzle to solve """
    quote = models.ForeignKey(Quote, blank=True)
    fakeauth0 = models.ForeignKey(Person, blank=True, related_name='+')
    fakeauth1 = models.ForeignKey(Person, blank=True, related_name='+')
    fakeauth2 = models.ForeignKey(Person, blank=True, related_name='+')
    totalguess = models.IntegerField(default=0)
    goodguess = models.IntegerField(default=0)

    def __unicode__(self):
        text = self.quote.text
        if len(text) > 30:
            text = text[0:28] + "..."
        text = self.quote.author.name + ":" + text
        return text

    class Meta:
        verbose_name = "puzzle"
        verbose_name_plural = "puzzles"
