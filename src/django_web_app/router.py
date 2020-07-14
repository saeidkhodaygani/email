from users.api.viewsets import userviewsets
from users.api.views import MeApiHandler
from rest_framework import routers 
  
router = routers.DefaultRouter() 
router.register('user', userviewsets, basename ='user_api') 
#router.register('user', MeApiHandler.as_view(), basename ='user_api') 
