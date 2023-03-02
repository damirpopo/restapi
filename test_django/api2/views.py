from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import BookSerializer

from .models import Book

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/book-list/',
        'Detail View':'/book-detail/<str:pk>',
        'Create':'/book-create/',
        'Update':'/book-update/<str:pk>',
        'Delete':'/book-delete/<str:pk>',
    }

    return Response(api_urls)


@api_view(['POST'])
def bookCreate(request):
    serializer=BookSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)



@api_view(['GET'])
def bookList(request):
    task =Book.objects.all().order_by('-id')
    serializer=BookSerializer(task,many=True)
    return Response(serializer.data)


@api_view(['GET'])
def bookDetail(request,pk):
    task = Book.objects.get(id=pk)
    serializer = BookSerializer(task, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def bookUpdate(request,pk):
    task = Book.objects.get(id=pk)
    serializer = BookSerializer(instance=task,data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)



@api_view(['DELETE'])
def bookDelete(request,pk):
    task = Book.objects.get(id=pk)
    task.delete()

    return Response('item delete')