
# Register your models here.
# from .models import Posts
# class PostModelAdmin(admin.ModelAdmin):
#     list_display = ["__unicode__", "updated", "timestamp"]
#     list_display_links = ["updated"]
#     list_filter = ["updated", "timestamp"]
#     search_field = ["title", "content"]
#     class Meta:
#         model = Post    


# admin.site.register(Post, PostModelAdmin)

# # Create your models here.
# class Post(models.Model):
#     title = models.CharField(max_length=120)
#     content = models.CharField(max_length=120)
#     updated = models.DateTimeField(auto_now=True, auto_now_add=False)
#     timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
#     def __unicode__(self):
#         return self.title
#     def __str__(self):
#         return self.title
#     def get_absolute_url(self):
#         return reverse("posts:detail", kwargs={"id": self.id})                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
# def post_create(request, *args, **kwargs):
#     return HttpResponse("<h1>Socail Page</h1>")
# def post_detail(request, id):
#     obj = get_object_or_404(Post, id=id)
#     # obj = Post.objects.get(id=id)
#     context = {
#         "title": "Detail Page",
#         "object": obj
#     }
#     return render(request, "post_detail.html", context)
# def post_list(request, *args, **kwargs):
#         object_list = Post.objects.all()
#         context = {
#             "title" : "your list",
#             "object_list" : object_list
#         }
#         return render(request, "post_list.html", context)
# def post_update(request, *args, **kwargs):
#     return HttpResponse("<h1>Socail Page</h1>") 
# def post_delete(request, *args, **kwargs):
#     return HttpResponse("<h1>Socail Page</h1>") 


# <!doctype html>
# <html>
# <head>
#     <title>Blog</title>
# </head>
# <body>
   

#    {% block content %}
#     replace me
#    {% endblock %} 

#     </body>
# </html>