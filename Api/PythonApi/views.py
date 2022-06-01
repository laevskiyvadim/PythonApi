from urllib.request import Request
from rest_framework.response import Response
from rest_framework.utils.serializer_helpers import ReturnList
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_protect, ensure_csrf_cookie
from django.utils.decorators import method_decorator
from rest_framework import authentication
from rest_framework import permissions
from uritemplate import partial
from .serializers import *
from .models import *

# crud forever :)


class TasksView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [
        authentication.TokenAuthentication, authentication.SessionAuthentication]

    @method_decorator(ensure_csrf_cookie)
    def get(self, request, pk=None):
        try:
            tasks = Tasks.objects.all()
            serializer = TaskSerializer(tasks, many=True)

            user = User.objects.filter(email=request.user)
            curUserSerializer = currentUserSerializer(user, many=True)

            users = User.objects.all()
            userSerializer = UserSerializer(users, many=True)

            if(type(serializer.data) == ReturnList):
                tasks = []
                for el in (serializer.data):
                    tasks.append({**el, 'users': userSerializer.data})
            else:
                tasks = {**serializer.data, 'users': userSerializer.data}

            data = {'tasks': tasks, 'curUser': curUserSerializer.data}

            return Response(data, status=200)
        except:
            return Response(status=404)

    @method_decorator(csrf_protect, name='dispatch')
    def post(self, request, pk=None):
        if pk:
            return Response('Нельзя постить в запись')
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            tasks = Tasks.objects.all()
            tasksSerializer = TaskSerializer(tasks, many=True)

            users = User.objects.all()
            userSerializer = UserSerializer(users, many=True)

            if(type(tasksSerializer.data) == ReturnList):
                data = []
                for el in (tasksSerializer.data):
                    data.append({**el, 'users': userSerializer.data})

            else:
                data = {**tasksSerializer.data, 'users': userSerializer.data}

            return Response(data, status=201)
        return Response(request, status=400)

    @method_decorator(csrf_protect, name='dispatch')
    def put(self, request, pk):
        task = Tasks.objects.get(pk=pk)
        serializer = TaskSerializer(task, data=request.data, partial=partial)

        if serializer.is_valid():
            serializer.save()

            tasks = Tasks.objects.all()
            tasksSerializer = TaskSerializer(tasks, many=True)

            users = User.objects.all()
            userSerializer = UserSerializer(users, many=True)

            if(type(tasksSerializer.data) == ReturnList):
                data = []
                for el in (tasksSerializer.data):
                    data.append({**el, 'users': userSerializer.data})

            else:
                data = {**tasksSerializer.data, 'users': userSerializer.data}

            return Response(data, status=200)
        return Response(status=400)

    @method_decorator(csrf_protect, name='dispatch')
    def delete(self, request, pk=None):
        try:
            task = Tasks.objects.get(pk=pk)
            task.delete()

            return Response(status=204)
        except:
            return Response(status=400)
