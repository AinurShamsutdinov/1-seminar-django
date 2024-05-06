from django.contrib import admin
from .models import TossCoin, Author, Article, Commentary, Client, Item, Order
# Register your models here.

class CommentAdmin(admin.ModelAdmin):
    """List of commentaries."""
    list_display = ['comment', 'article']
    list_filter = ['date_creat']
    search_fields = ['comment', 'author']
    search_help_text = f'Поиск по полю комментарий.'


    """List of comment."""
    fields = ['comment', 'article', 'author', 'date_creat', 'date_edit']
    readonly_fields = ['date_creat', 'date_edit']

class AuthorAdmin(admin.ModelAdmin):
    """List of authors."""
    list_display = ['name', 'last_name']
    ordering = ['birthday']
    list_filter = ['name', 'last_name']
    search_fields = ['name', 'last_name']
    search_help_text = f'Поиск по полю автор.'


    """List of author."""
    fields = ['name', 'last_name', 'full_name', 'email', 'biography', 'birthday']
    readonly_fields = ['birthday']

class ArticleAdmin(admin.ModelAdmin):
    """List of articles."""
    list_display = ['head', 'views', 'publish_date']
    ordering = ['publish_date']
    list_filter = ['head', 'content']
    search_fields = ['head', 'author']
    search_help_text = f'Поиск по полю творению.'


    """List of article."""
    fields = ['head', 'content', 'category', 'author', 'views', 'publish_date']
    readonly_fields = ['publish_date', 'views']

class ItemAdmin(admin.ModelAdmin):
    """List of articles."""
    list_display = ['name', 'price', 'amount']
    ordering = ['name']
    list_filter = ['name', 'description']
    search_fields = ['name', 'description']
    search_help_text = f'Поиск по полю творению.'


    """List of article."""
    fields = ['name', 'description', 'price', 'amount', 'date_add', 'image']
    readonly_fields = ['date_add']

class ClientAdmin(admin.ModelAdmin):
    """List of clients."""
    list_display = ['name', 'email']
    ordering = ['name']
    list_filter = ['name', 'date_reg']
    search_fields = ['name', 'date_reg']
    search_help_text = f'Поиск по полю имен клиентов.'


    """List of client."""
    fields = ['name', 'email', 'phone', 'address', 'date_reg']
    readonly_fields = ['date_reg']

class OrderAdmin(admin.ModelAdmin):
    """List of clients."""
    list_display = ['client', 'full_price']
    ordering = ['client']
    list_filter = ['client', 'date_order']
    search_fields = ['client', 'date_order']
    search_help_text = f'Поиск по полю имен клиентов.'


    """List of client."""
    fields = ['client', 'items', 'full_price', 'date_order']
    readonly_fields = ['date_order', 'items', 'client', 'full_price']

admin.site.register(TossCoin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Commentary, CommentAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(Order, OrderAdmin)
