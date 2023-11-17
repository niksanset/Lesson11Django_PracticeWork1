from django.shortcuts import render, redirect
from app.models import Student


def info_students_view(request):
    context = {"student_list": Student.objects.all()}

    return render(request, "info_students.html", context)


def info_student_and_change_view(request, student_slug):
    student = Student.objects.get(slug=student_slug)

    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        pay_or_not = request.POST.get("pay_or_not")
        grade = request.POST.get("grade")

        student.first_name = first_name
        student.last_name = last_name
        student.pay_or_not = pay_or_not
        student.grade = grade

        student.save()
        return redirect("info_students")
    context = {
        "student": student,
    }
    return render(request, "info_student.html", context)


def add_student_view(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        age = request.POST.get("age")
        course = request.POST.get("course")
        music_instrument = request.POST.get("music_instrument")
        grade = request.POST.get("grade")
        pay_or_not = request.POST.get("pay_or_not")

        student = Student()
        student.first_name = first_name
        student.last_name = last_name
        student.age = age
        student.course = course
        student.music_instrumet = music_instrument
        student.grade = grade
        student.pay_or_not = pay_or_not
        student.save()

    return render(request, "add_student.html")
