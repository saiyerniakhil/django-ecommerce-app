from rest_framework import viewsets
 
from .serializers import CategorySerializer
from .models import Category

#TODO What is the data that we're bringing from the database
#TODO Based on the serializer that we've written earlier, that data from above step is gonna get converted into JSON
class CategoryViewSet(viewsets.ModelViewSet): 
    queryset = Category.objects.all().order_by('name')
    serializer_class = CategorySerializer
     