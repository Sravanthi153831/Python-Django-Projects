from django.shortcuts import render, redirect, get_object_or_404

from .models import Robot
from .forms import RobotForm


# ADD AND DISPLAY ROBOTS

def robot_list(request):

    if request.method == 'POST':

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

def edit_robot(request, id):

    robot = get_object_or_404(Robot, id=id)

    if request.method == 'POST':

        form = RobotForm(request.POST, instance=robot)

        if form.is_valid():

            form.save()

            print("ROBOT UPDATED SUCCESSFULLY")

            return redirect('robot_list')

    else:
        form = RobotForm(instance=robot)

    return render(request, 'edit_robot.html', {
        'form': form,
        'robot': robot
    })


# DELETE ROBOT

def delete_robot(request, id):

    robot = get_object_or_404(Robot, id=id)

    if request.method == 'POST':

        robot.delete()

        print("ROBOT DELETED SUCCESSFULLY")

        return redirect('robot_list')

    return render(request, 'delete_robot.html', {
        'robot': robot
    })
          
