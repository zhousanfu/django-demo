import xadmin
from xadmin import views
from .models import CommentInfo_India, KeyWords




class CommentInfo_India_Xadmin():
    list_display = ['title', 'content', 'source', 'mediatype', 'attribute', 'time', 'heat', 'go_to']
    search_fields = ['title', 'content']
    list_filter = ['mediatype', 'source', 'attribute', 'time']
    ordering = ['-time','-heat']
    list_display_links = ['source']
    list_per_page = 50
    actions = ['custom_button']
    model_icon = 'fa fa-university'



class KeyWords_Xadmin():
    list_display = ['keyword', 'username', 'status']
    list_filter = ['keyword', 'username', 'status']
    list_per_page = 50
    show_bookmarks = False
    ordering = ['keyword']
    model_icon = 'fa fa-plus-square-o'



xadmin.site.register(KeyWords, KeyWords_Xadmin)
xadmin.site.register(CommentInfo_India, CommentInfo_India_Xadmin)
