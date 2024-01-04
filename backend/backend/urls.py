from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/book-review/', include('book.urls')),
    path('api/genre/', include('genre.urls')),
    path('api/token/', include('api.urls')),  # Corrected line
]
