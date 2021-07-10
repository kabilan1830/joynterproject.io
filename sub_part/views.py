from django.core.mail import send_mail
from django.conf import settings
import easygui
from django.shortcuts import redirect, render
from.models import College, course, feedback, stdregister, stdsignin
from.models import clgsignin
from.models import unisignin
from.models import addstd
from django.contrib.auth import logout as stdlog
from django.contrib.auth import logout as cllglog
from django.contrib.auth import logout as unilogout
multi_user_name = ''
multi_clg_name=''
multi_uni_name=''

def landingpage(request):
    # Create your views here.
    return render(request, 'landingpage.html')

    # student.


def stdsign(request):
    if request.method == 'POST':
        user = stdsignin(name=request.POST['name'],
                         email=request.POST['email'],
                         pwd=request.POST['pwd'],
                         re_pass=request.POST['re_pass'],

                         )
        user.save()
        subject = 'Welcome to Joynter'
        message = 'Student councils are always a means of the endless bonds and friendships for ever'
        email_from = settings.EMAIL_HOST_USER
        recepient = request.POST.get('email')
        print("check:", recepient)
        send_mail(subject, message, email_from, [recepient], fail_silently=False)
        easygui.msgbox("Register successfully", title="Joynter")
        return redirect(student)
    return render(request, 'student-signin-page.html')


def csign(request):
    if request.method == 'POST':
        var2 = clgsignin(name=request.POST['name'],
                         email=request.POST['email'],
                         pwd=request.POST['pwd'],
                         re_pass=request.POST['re_pass'],

                         )
        var2.save()
        subject = 'Welcome to Joynter'
        message = 'College councils are always a means of the endless bonds and friendships for ever'
        email_from = settings.EMAIL_HOST_USER
        recepient = request.POST.get('email')
        print("check:", recepient)
        send_mail(subject, message, email_from, [recepient], fail_silently=False)
        easygui.msgbox("Register successfully", title="Joynter")
        return redirect(clogin)
    return render(request, 'csignup.html')


def usign(request):
    if request.method == 'POST':
        var2 = unisignin(name=request.POST['name'],
                         email=request.POST['email'],
                         pwd=request.POST['pwd'],
                         re_pass=request.POST['re_pass'],

                         )
        var2.save()
        subject = 'Welcome to Joynter'
        message = 'Student councils are always a means of the endless bonds and friendships for ever'
        email_from = settings.EMAIL_HOST_USER
        recepient = request.POST.get('email')
        print("check:", recepient)
        send_mail(subject, message, email_from, [recepient], fail_silently=False)
        easygui.msgbox("Register successfully", title="Joynter")
        return redirect(udlogin)
    return render(request, 'usignup.html')


def student(request):
    if request.method == 'POST':
        if stdsignin.objects.filter(name=request.POST['name'], pwd=request.POST['pwd']).exists():
            var5 = stdsignin.objects.get(name=request.POST['name'],
                                         pwd=request.POST['pwd'])
            global multi_user_name
            multi_user_name = var5.name
            ut_data = stdsignin.objects.get(name=multi_user_name)
            easygui.msgbox("Logged In Successfully", title="Joynter")
            return redirect(studentdash)
        else:
            var4 = {'msg': 'Incorrect Password or Name'}
            return render(request, 'student-login-page.html', var4)
    return render(request, 'student-login-page.html')


def studentdash(request):
    ut_data = stdsignin.objects.get(name=multi_user_name)
    return render(request, 'student-dashboard.html', {'ut_data': ut_data})


def srf(request):
    ut_data = stdsignin.objects.get(name=multi_user_name)
    return render(request, 'std-registration-form.html', {'ut_data': ut_data})


def vicd(request):
    varv = College.objects.all
    ut_data = stdsignin.objects.get(name=multi_user_name)
    return render(request, 'view-individual-college-details.html', {'varv': varv, 'ut_data': ut_data})


def vcd(request):
    varn = course.objects.all
    ut_data = stdsignin.objects.get(name=multi_user_name)
    return render(request, 'view-course-details.html', {'varn': varn, 'ut_data': ut_data})

# university


def udlogin(request):
    if request.method == 'POST':
        if unisignin.objects.filter(name=request.POST['name'], pwd=request.POST['pwd']).exists():
            var6 = unisignin.objects.get(name=request.POST['name'],
             pwd=request.POST['pwd'])
            global multi_uni_name
            multi_uni_name = var6.name
            uni_data = unisignin.objects.get(name=multi_uni_name)
            easygui.msgbox("Logged In Successfully", title="Joynter")
            return redirect(udash)
        else:
            var4 = {'msg': 'Incorrect Password or Name'}
            return render(request, 'ud-admin.html', var4)
    return render(request, 'ud-admin.html')


def university(request):
    uni_data = unisignin.objects.get(name=multi_uni_name)
    return render(request, 'super-admin-login-page.html',{'uni_data': uni_data})


def udash(request): 
    uni_data = unisignin.objects.get(name=multi_uni_name)
    return render(request, 'University-dashboard.html',{'uni_data': uni_data})


def vstd(request):
    vark = stdregister.objects.all()
    uni_data = unisignin.objects.get(name=multi_uni_name)
    return render(request, 'ud-view-student-details.html', {'vark': vark,'uni_data': uni_data})


def uvcld(request):
    varv = College.objects.all()
    uni_data = unisignin.objects.get(name=multi_uni_name)
    return render(request, 'ud-view-college-details.html', {'varv': varv,'uni_data': uni_data})


def uvcd(request): 
    varn = course.objects.all()
    uni_data = unisignin.objects.get(name=multi_uni_name)
    return render(request, 'ud-view-course-details.html', {'varn': varn,'uni_data': uni_data})


# college
def clogin(request):
    if request.method == 'POST':
        if clgsignin.objects.filter(name=request.POST['name'], pwd=request.POST['pwd']).exists():
            var3 = clgsignin.objects.get(name=request.POST['name'],
                                         pwd=request.POST['pwd'])
            global multi_clg_name
            multi_clg_name = var3.name
            clg_data = clgsignin.objects.get(name=multi_clg_name)                            
            easygui.msgbox("Logged In Successfully", title="Joynter")
            return redirect(cdash)
        else:
            var4 = {'msg': 'Incorrect Password or Name'}
            return render(request, 'clglogin.html', var4)

    return render(request, 'clglogin.html')


def cdash(request):
    clg_data = clgsignin.objects.get(name=multi_clg_name)  
    return render(request, 'College-dashboard.html',{'clg_data':clg_data})


def cvcd(request):
    varn = course.objects.all()
    clg_data = clgsignin.objects.get(name=multi_clg_name)  
    return render(request, 'cd-view-course-details.html', {'varn': varn,'clg_data':clg_data})


def cvcld(request):
    varv = College.objects.all()
    clg_data = clgsignin.objects.get(name=multi_clg_name) 
    return render(request, 'cd-view-college-details.html', {'varv': varv,'clg_data':clg_data})

# Database


def feed(request):
    if request.method == 'POST':
        var1 = feedback(name=request.POST['name'],
                        email=request.POST['email'],
                        msg=request.POST['msg'],

                        )
        var1.save()
        easygui.msgbox("feedback submitted", title="joynter")
        return redirect(landingpage)
    return render(request, 'landingpage.html')


def addstudent(request):
    if request.method == 'POST':
        var1 = addstd(sno=request.POST['sno'],
                      stdname=request.POST['stdname'],
                      stdid=request.POST['stdid'],
                      fname=request.POST['fname'],
                      mobile=request.POST['mobile'],
                      reg=request.POST['reg'],
                      cls=request.POST['cls'],
                      sec=request.POST['sec'],
                      group=request.POST['group'],
                      )
        var1.save()
        easygui.msgbox("successfully Added", title="joynter")
        return redirect(vstd)
    return render(request, 'ud-view-student-details.html')


def delstd(request, id):
    varS = stdregister.objects.get(id=id)
    varS.delete()
    easygui.msgbox("successfully Deleted", title="joynter")
    return redirect(vstd)


def course1(request):
    if request.method == 'POST':
        varn = course(cid=request.POST['cid'],
                      code=request.POST['code'],
                      cname=request.POST['cname'],
                      cd=request.POST['cd'],

                      )
        varn.save()
        easygui.msgbox("Added Successfully", title="joynter")
        return redirect(cvcd)
    return render(request, 'cd-view-course-details.html')


def course2(request):
    if request.method == 'POST':
        varn = course(cid=request.POST['cid'],
                      code=request.POST['code'],
                      cname=request.POST['cname'],
                      cd=request.POST['cd'],

                      )
        varn.save()
        easygui.msgbox("Added Successfully", title="joynter")
        return redirect(uvcd)
    return render(request, 'ud-view-course-details.html')


def college1(request):
    if request.method == 'POST':
        varv = College(uid=request.POST['uid'],
                       cc=request.POST['cc'],
                       clgname=request.POST['clgname'],
                       clgd=request.POST['clgd'],

                       )
        varv.save()
        easygui.msgbox("Added Successfully", title="joynter")
        return redirect(uvcld)
    return render(request, 'ud-view-college-details.html')


def vstdreg(request):
    varq = stdregister.objects.all()
    clg_data =clgsignin.objects.get(name=multi_clg_name)
    return render(request, 'viewstdreg.html', {'varq': varq,'clg_data':clg_data})


def vsr(request):
    if request.method == 'POST':
        var1 = stdregister(
            fname=request.POST['fname'],
            lname=request.POST['lname'],
            fathername=request.POST['fathername'],
            gender=request.POST['gender'],
            pschool=request.POST['pschool'],
            add=request.POST['add'],
            dob=request.POST['dob'],

        )
        var1.save()
        easygui.msgbox("successfully Registered", title="joynter")
        return redirect(studentdash)
    return render(request, 'Student-dashboard.html')


def stdedit(request, id):
    varn = stdregister.objects.get(id=id)
    uni_data = unisignin.objects.get(name=multi_uni_name)
    return render(request, 'editstd.html', {'varn': varn,'uni_data':uni_data})


def sedit(request):
    return render(request, 'editstd.html')


def saves(request, id):
    varn = stdregister(id=id, fname=request.POST['fname'],
                       lname=request.POST['lname'],
                       fathername=request.POST['fathername'],
                       gender=request.POST['gender'],
                       pschool=request.POST['pschool'],
                       add=request.POST['add'],
                       dob=request.POST['dob']

                       )
    varn.save()
    easygui.msgbox("Updated successfully", title="joynter")
    return redirect(vstd)


def rf(request):
    if request.method == 'POST':
        vari = stdregister(fname=request.POST['fname'],
                           lname=request.POST['lname'],
                           fathername=request.POST['fathername'],
                           gender=request.POST['gender'],
                           pschool=request.POST['pschool'],
                           add=request.POST['add'],
                           dob=request.POST['dob']
                           )
        vari.save()
        return redirect(studentdash)


def clgedit(request, id):
    vara = stdregister.objects.get(id=id)
    clg_data =clgsignin.objects.get(name=multi_clg_name)
    return render(request, 'clgedit.html', {'vara': vara,'clg_data':clg_data})


def cedit(request):
    return render(request, 'clgedit.html')


def savec(request, id):
    varb = stdregister(id=id, fname=request.POST['fname'],
                       lname=request.POST['lname'],
                       fathername=request.POST['fathername'],
                       gender=request.POST['gender'],
                       pschool=request.POST['pschool'],
                       add=request.POST['add'],
                       dob=request.POST['dob']

                       )
    varb.save()
    easygui.msgbox("Updated successfully", title="joynter")
    return redirect(vstdreg)


def delclg(request, id):
    varc = stdregister.objects.get(id=id)
    varc.delete()
    easygui.msgbox("successfully Deleted", title="joynter")
    return redirect(vstdreg)

def studentlogout(request):
    stdlog(request)
    return render(request,'student-login-page.html')

def collegelogout(request):
    cllglog(request)
    return render(request,'clglogin.html')

def universitylogout(request):
    unilogout(request)
    return render(request,'ud-admin.html')


