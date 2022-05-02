from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('postbook', views.postbook, name='postbook'),
    path('displaybooks', views.displaybooks, name='displaybooks'),
    path('book_detail/<int:book_id>', views.book_detail, name='book_detail'),
    path('mybooks', views.mybooks, name='mybooks'),
    path('book_delete/<int:book_id>', views.book_delete, name='book_delete'),
    path('about_us', views.about_us, name='about_us'),
    path('search_books', views.search_books, name='search_books'),
    path('shopping_cart', views.shopping_cart, name='shopping_cart'),
    path('add_to_cart/<int:book_id>', views.add_to_cart, name=''),
    path('remove_from_cart/<int:book_id>', views.remove_from_cart, name=''),
]

