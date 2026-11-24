from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.http import require_GET

from .models import Robot
from .forms import RobotForm


# HOME PAGE

def robot_list(request):

    if request.method == "POST":

        form = RobotForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("robot_list")

    else:
        form = RobotForm()

    robots = Robot.objects.all().order_by("-id")

    for robot in robots:
        robot.status = robot.battery_status()

    return render(request, "robot_list.html", {
        "form": form,
        "robots": robots
    })


# EDIT ROBOT

def edit_robot(request, id):

    robot = get_object_or_404(Robot, id=id)

    if request.method == "POST":

        form = RobotForm(request.POST, instance=robot)

        if form.is_valid():
            form.save()
            return redirect("robot_list")

    else:
        form = RobotForm(instance=robot)

    return render(request, "edit_robot.html", {
        "form": form,
        "robot": robot
    })


# DELETE ROBOT

def delete_robot(request, id):

    robot = get_object_or_404(Robot, id=id)

    if request.method == "POST":

        robot.delete()
        return redirect("robot_list")

    return render(request, "delete_robot.html", {
        "robot": robot
    })


# LIVE BATTERY API

@require_GET
def battery_live(request):

    robots = Robot.objects.all()

    data = []

    for robot in robots:

        data.append({

            "id": robot.id,

            "name": robot.name,

            "battery_level": robot.battery_level,

            "battery_status": robot.battery_status()

        })

    return JsonResponse({
        "robots": data
    })
    
 
    
