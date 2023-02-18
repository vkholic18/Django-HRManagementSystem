from django.urls import path
from .views import employee_list,employee_detail,employee_delete,home,employee_edit,employee_add,team_list,team_detail,team_delete,team_edit,employee_note,login_view,signup_view,logout_view,organization,team_add

urlpatterns = [
    path("",home,name='home'),
    path('Employees',employee_list,name="employee_list"),
    path("Employees/<int:id>",employee_detail,name="detail"),
    path("Employee_delete/<int:id>",employee_delete,name="delete"),
    path("Employee_edit/<int:id>",employee_edit,name="edit"),
    path("Teams",team_list,name="team_list"),
    path("Teams/<int:id>",team_detail,name="team_detail"),
    path("Team_edit/<int:id>",team_edit,name="team_edit"),
    path("Team_delete/<int:id>",team_delete,name="team_delete"),
    path("Employee_notes/<int:id>",employee_note,name="employee_note"),
    path("login",login_view,name="login"),
    path("signup",signup_view,name="signup"),
    path("logout",logout_view,name="logout"),
    path("Organization",organization,name="org"),
    path("Employee_add",employee_add,name="add"),
    path("Team_add",team_add,name="team_add")
    
]
