
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse # resposta para requisição



# Django funciona em MVT (Model, View Template)

# HTTP Request <-> Response
def my_view(request):
    print("enviado!")
    return HttpResponse ("quero que o mundo se acabe em crack")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', my_view),
]
