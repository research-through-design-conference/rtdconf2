from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class Page(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    slug = models.SlugField(unique=True, max_length=255, null=True, blank=True)
    text = models.TextField()
    header_image = models.FileField(upload_to='pages/%Y/%m/%d', null=True, blank=True)

    def __unicode__(self):
        return u'%s' % self.title

    def get_absolute_url(self):
        return reverse('microsite_2015.views.page', args=[self.slug])
