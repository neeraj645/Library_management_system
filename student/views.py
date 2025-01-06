from django.http import HttpResponse, JsonResponse
from .models import Student

def show_student(request, id):
    try:
        student = Student.objects.get(id=id)
        student_data = {
            "fname": student.fname,
            "lname": student.lname,
            "email": student.email,
            "phone": student.phone,
            "active": student.active,
            "created_at": student.created_at,
            "updated_at": student.updated_at,
            "verified": student.verified
        }
        return JsonResponse({"success": True, "data": student_data})
    except Student.DoesNotExist:
        return JsonResponse({"success": False, "message": "Student not found!"})


from django.http import JsonResponse
from .models import Student

def show_all_students(request):
    students = Student.objects.all()
    student_list = []
    
    for student in students:
        student_data = {
            "id": student.id,
            "fname": student.fname,
            "lname": student.lname,
            "email": student.email,
            "phone": student.phone,
            "active": student.active,
            "created_at": student.created_at,
            "updated_at": student.updated_at,
            "verified": student.verified
        }
        student_list.append(student_data)
    
    return JsonResponse({"success": True, "data": student_list})




from django.http import JsonResponse
from .models import Student
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def add_student(request):
    print("hello")
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        
        # Create new student
        student = Student.objects.create(
            fname=fname,
            lname=lname,
            email=email,
            phone=phone,
            password=password,
            active=True
        )
        return JsonResponse({"success": True, "message": "Student added successfully!"})
    return HttpResponse("done")


from django.http import JsonResponse
from .models import Student

def update_student(request, id):
    try:
        student = Student.objects.get(id=id)
        if request.method == 'POST':
            student.fname = request.POST.get('fname', student.fname)
            student.lname = request.POST.get('lname', student.lname)
            student.email = request.POST.get('email', student.email)
            student.phone = request.POST.get('phone', student.phone)
            student.password = request.POST.get('password', student.password)
            student.save()
            
            return JsonResponse({"success": True, "message": "Student updated successfully!"})
    except Student.DoesNotExist:
        return JsonResponse({"success": False, "message": "Student not found!"})
 
from django.http import JsonResponse
from .models import Student

def delete_student(request, id):
    try:
        student = Student.objects.get(id=id)
        student.delete()
        return JsonResponse({"success": True, "message": "Student deleted successfully!"})
    except Student.DoesNotExist:
        return JsonResponse({"success": False, "message": "Student not found!"})



from django.http import JsonResponse
from .models import Student

def verify_student(request, id):
    try:
        student = Student.objects.get(id=id)
        student.verified = True
        student.save()
        return JsonResponse({"success": True, "message": "Student verified successfully!"})
    except Student.DoesNotExist:
        return JsonResponse({"success": False, "message": "Student not found!"})


