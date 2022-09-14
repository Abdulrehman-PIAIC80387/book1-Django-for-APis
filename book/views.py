from django.shortcuts import render
from .models import My_library
from django.views.generic import ListView
# Create your views here.
from rest_framework import generics,permissions
from .serializers import bookserializer
from .permissions import IsAuthorOrReadOnly # new

class get_book(ListView):
    model = My_library
    template_name= 'index.html'



class libraryapi(generics.ListAPIView):
    queryset = My_library.objects.all()
    serializer_class = bookserializer



class details(generics.RetrieveAPIView):
    queryset = My_library.objects.all()
    serializer_class = bookserializer



class postdetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = My_library.objects.all()
    serializer_class = bookserializer



class postlist(generics.ListCreateAPIView):
    # permission_classes = (permissions.IsAuthenticated,) # new
    permission_classes = (IsAuthorOrReadOnly,) # new
    queryset = My_library.objects.all()
    serializer_class = bookserializer



