
from django.contrib import admin
from django.urls import path
from cityapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',views.index,name='index'),
    path('', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('starter/', views.starter, name='starter'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('contactshow/', views.contactshow, name='contactshow'),
    path('deleteContact/<int:id>', views.deleteContact, name='deleteContact'),
    path('editContact/<int:id>', views.editContact, name='editContact'),
    path('updateContact/<int:id>', views.updateContact, name='updateContact'),
    path('menu/', views.menu, name='menu'),
    path('book/', views.book, name='book'),
    path('deleteBookings/<int:id>', views.deleteBookings, name='deleteBookings'),
    path('editBookings/<int:id>', views.editBookings, name='editBookings'),
    path('updateBookings/<int:id>', views.updateBookings, name='updateBookings'),
    path('show/', views.show, name='show'),
    path('rate_us/', views.rate_us, name='rate_us'),
    path('show_ratings/', views.show_ratings, name='show_ratings'),
    path('specials/', views.specials, name='specials'),
    path('events/', views.events, name='events'),
    path('chefs/', views.chefs, name='chefs'),
    path('testimonials/', views.testimonials, name='testimonials'),
    path('gallery/', views.gallery, name='gallery'),
    path('terms/', views.terms, name='terms'),
    path('passwordreset/', views.passwordreset, name='passwordreset'),

]
