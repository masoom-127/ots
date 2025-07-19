from django.urls import path
from OTS import views
app_name = 'OTS'

urlpatterns = [
    path('',views.welcome,name='welcome'),
    # path('new-candidate',views.candidateRegistrationForm,name='registration-Form'),
    path('store-candidate',views.candidateRegistration,name='storeCandidate'),
    path('login',views.loginView,name='login'),
    path('home',views.candidateHome),
    path('testpaper',views.testpaper),
    path('calculateresult',views.calculateTestResult),
    path('testhistory',views.testResultHistory),
    path('showtestresult',views.showTestresult),
    path('logoutview',views.logoutView),

]



