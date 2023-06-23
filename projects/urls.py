from rest_framework import routers
from .api import ProjectsViewSets


router = routers.DefaultRouter()

router.register('api/projects', ProjectsViewSets, 'projects')

urlpatterns = router.urls

