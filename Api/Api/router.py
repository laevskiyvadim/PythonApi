from PythonApi.viewsets import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('user', Users)
router.register('tasks', Task)
