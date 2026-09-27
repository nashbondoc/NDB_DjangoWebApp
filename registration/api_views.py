from django.http import JsonResponse
from .models import Student


def student_api(request):
    if not request.user.is_authenticated:
        return JsonResponse(
            {"detail": "Authentication credentials were not provided."},
            status=401
        )

    if request.method == "GET":
        students = Student.objects.all()

        data = []

        for student in students:
            data.append({
                "id": student.id,
                "student_name": student.student_name,
                "program": student.program,
                "year_level": student.year_level,
                "email": student.email,
            })

        return JsonResponse(
            {
                "count": len(data),
                "students": data
            },
            status=200
        )

    return JsonResponse(
        {"detail": "Method not allowed."},
        status=405
    )