from django.shortcuts import render
from django.contrib.auth import authenticate, login
# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from .forms import EmployeeForm,TeamForm
from .models import Employee,Team,EmployeeNotes
from .forms import EmployeeNoteForm,LoginForm
from .forms import SignUpForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required




def home(request):
    return render(request,"employees/home.html")

@login_required(login_url="login")
def employee_list(request):
    employees = Employee.objects.all()
    
    context={'employees': employees ,}
    return render(request, 'employees/employee_list.html',context )
    

@login_required(login_url="login")
def employee_detail(request, id):
    employee = get_object_or_404(Employee, id=id)
    return render(request, 'employees/employee_detail.html', {'employee': employee,'exchange_rate' : 0.014})

@login_required(login_url="login")
def employee_new(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            employee = form.save()
            return redirect('employee_detail', pk=employee.pk)
    else:
        form = EmployeeForm()
    return render(request, 'employees/employee_edit.html', {'form': form})

@login_required(login_url="login")
def employee_edit(request, id):
    employee = get_object_or_404(Employee, id=id)
    if request.method == "POST":
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            employee = form.save()
            return redirect('detail', id=employee.id)
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'employees/employee_edit.html', {'form': form})

@login_required(login_url="login")
def employee_delete(request, id):
    employee = get_object_or_404(Employee, id=id)
    employee.delete()
    return redirect('employee_list')


def employee_add(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to success page
            return redirect('employee_list')
    else:
        form = EmployeeForm()
    return render(request, 'employees/employee_add.html', {'form': form})

@login_required(login_url="login")
def team_list(request):
    teams=Team.objects.all()
    context={'teams':teams}
    return render(request,'employees/team_list.html',context)




@login_required(login_url="login")
def team_detail(request,id):
    team=Team.objects.get(id=id)
    members = team.members.all()
    context={"team":team,'members':members}
    
    return render(request,"employees/team_details.html",context)

@login_required(login_url="login")
def team_delete(request,id):
    team=get_object_or_404(Team, id=id)
    team.delete()
    return redirect("team_list")

@login_required(login_url="login")
def team_edit(request, id):
    team = get_object_or_404(Team, id=id)
    if request.method == "POST":
        form = TeamForm(request.POST, instance=team)
        if form.is_valid():
            employee = form.save()
            return redirect('team_detail', id=team.id)
    else:
        form = TeamForm(instance=team)
    return render(request, 'employees/team_edit.html', {'form': form})

def team_add(request):
    if request.method == 'POST':
        form = TeamForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to success page
            return redirect('team_list')
    else:
        form = TeamForm()
    return render(request, 'employees/team_add.html', {'form': form})


@login_required(login_url="login")
def employee_note(request,id):
    # Retrieve the employee
    employee = get_object_or_404(Employee, id=id)

    # Retrieve any existing notes
    notes = EmployeeNotes.objects.filter(employee=employee)

    # Process the form submission
    if request.method == 'POST':
        form = EmployeeNoteForm(request.POST)
        if form.is_valid():
            # Save the new note
            note = form.save(commit=False)
            note.employee = employee
            note.save()
            return redirect('employee_note', id=employee.id)
    else:
        form = EmployeeNoteForm()

    return render(request, 'employees/employee_notes.html', {'employee': employee, 'notes': notes, 'form': form})
    
    


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'employees/signup.html', {'form': form})



def login_view(request):
    # Check if user is already authenticated, redirect to dashboard
    if request.user.is_authenticated:
        return redirect('home')

    # Handle form submission
    if request.method == 'POST':
        form = LoginForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                form.add_error(None, 'Invalid username or password')
    else:
        form = LoginForm()

    return render(request, 'employees/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('home')

@login_required(login_url="login")
def organization(request):
    return render(request,"employees/organization.html")
