from django.shortcuts import render,redirect

from django.http import HttpResponse,HttpResponseNotFound
from  django.views.decorators.http import require_http_methods
from django.template import loader
from myapp.form import StuForm,StudentForm

#for file upload
from myapp.functions.functions import handle_uploaded_file
from myapp.form import StudentFormUpload
  
def hello(request):
    return HttpResponse("<h2>Hello, Welcome to Django!</h2>")

def index(request):
    template=loader.get_template('index.html')
    name={
        'student':'Shoumitro'
    }
    return HttpResponse(template.render(name))
    # return render(request, 'index.html')

# @require_http_methods(["GET"])
# def show(request):
#
#     fname=request.GET.get("firstname")
#     lname=request.GET.get("lastname")
#     date=request.GET.get("date")
#     html='<h1>Your First Name : %s  </h1> ' \
#          '<h1>Your Last Name :  %s  </h1>' \
#          ' <h1>Date :  %s  </h1>'%(fname,lname,date)
#
#     return HttpResponse(html)
def show(request):

    fname=request.GET.get("first_name")
    lname=request.GET.get("last_name")
    csrfmiddlewaretoken=request.GET.get("csrfmiddlewaretoken")

    html='<h1>Your First Name : %s  </h1> ' \
         '<h1>Your Last Name :  %s  </h1>'\
         '<h1>csrfmiddlewaretoken :  %s  </h1>'%(fname,lname,csrfmiddlewaretoken)

    return HttpResponse(html)


def stform(request):

    if request.method == "POST":
        stu = StuForm(request.POST)
        if stu.is_valid():
            try:
                return redirect('/index')
            except:
                pass
    else:
        stu = StuForm()
        # stu = StudentForm()
    return render(request, "forms.html", context={'form': stu})

def emp(request):
    if request.method == "POST":
        form = StuForm(request.POST)
        if form.is_valid():
            try:
                return redirect('/')
            except:
                pass
    else:
        form = StuForm()
    return render(request,'vaild.html',{'form':form})




def file_upload(request):
    if request.method == 'POST':
        student = StudentFormUpload(request.POST, request.FILES)
        if student.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponse("File uploaded successfuly")
    else:
        student = StudentFormUpload()
        return render(request,"file_upload.html",{'form':student})