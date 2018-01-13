from django.db import models
from django.conf import settings
from django.db.models.signals import pre_save, post_save

from tinymce import HTMLField
from mptt.models import MPTTModel, TreeForeignKey

from .utils import get_read_time


class Post(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(max_length=250, blank=True, null=True)
    category = TreeForeignKey('Category',null=True,blank=True,on_delete=models.SET_NULL)
    content = HTMLField('Content')
    slug = models.SlugField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    read_time = models.IntegerField(default=0)
    hits = models.IntegerField(default=0)
    draft = models.BooleanField(default=False)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, default=1,
        on_delete=models.SET_DEFAULT
        )

    def __str__(self):
        return self.title


class Category(MPTTModel):
    name = models.CharField(max_length=50, unique=True)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True,on_delete=models.CASCADE)
    slug = models.SlugField()

    class Meta:
        unique_together = (('parent', 'slug',))
        verbose_name_plural = 'Categories'

    def get_slug_list(self):
        try:
            ancestors = self.get_ancestors(include_self=True)
        except:
            ancestors = []
        else:
            ancestors = [ i.slug for i in ancestors]
        slugs = []
        for i in range(len(ancestors)):
            slugs.append('/'.join(ancestors[:i+1]))
        return slugs

    def __str__(self):
        return self.name


def pre_save_post_receiver( sender, instance, *args, **kwargs):
    if instance.content:
        instance.read_time = get_read_time(instance.content)


pre_save.connect(pre_save_post_receiver, sender=Post)
