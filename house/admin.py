from django.contrib import admin
from .models import Post, Comment, Testimonial

# Register your models here.
admin.site.site_header = "Fashion House"

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Testimonial)