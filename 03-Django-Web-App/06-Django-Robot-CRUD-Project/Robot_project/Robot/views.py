from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Robot
from .forms import RobotForm


# ADD AND DISPLAY ROBOTS
def robot_list(request):
    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect('/admin/login/?next=/')
        form = RobotForm(request.POST)
        if form.is_valid():
            form.save()
            print("ROBOT ADDED SUCCESSFULLY")
            return redirect('robot_list')
    else:
        form = RobotForm()

    robots = Robot.objects.all().order_by('-id')
    return render(request, 'robot_list.html', {
        'form': form,
        'robots': robots
    })


# EDIT AND UPDATE ROBOT
@login_required(login_url='/admin/login/')
def edit_robot(request, id):
    robot = get_object_or_404(Robot, id=id)
    if request.method == 'POST':
        form = RobotForm(request.POST, instance=robot)
        if form.is_valid():
            form.save()
            return redirect('robot_list')
    else:
        form = RobotForm(instance=robot)

    return render(request, 'edit_robot.html', {'form': form, 'robot': robot})


# DELETE ROBOT
@login_required(login_url='/admin/login/')
def delete_robot(request, id):
    robot = get_object_or_404(Robot, id=id)
    robot.delete()
    return redirect('robot_list')
    
