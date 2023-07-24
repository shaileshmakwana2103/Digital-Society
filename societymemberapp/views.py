from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from chairmanapp.models import *


# Create your views here.

"""
models.objects.get(fieldname = htmlname)  : fetch data from database (model).

"""
def societymember_profile(request):
    if "email" in request.session:
        uid = User.objects.get(email = request.session['email'])
        sid = Societymember.objects.get(user_id = uid)
        if request.POST:
            firstname = request.POST['firstname']
            lastname = request.POST['lastname']

            sid.firstname = firstname
            sid.lastname = lastname

            if "picture" in request.FILES:
                sid.pic = request.FILES['picture']

            sid.save()
            
            context = {
                'uid' : uid,
                'sid' : sid,
            }
            return render(request,"societymemberapp/profile.html",context)
        else:
            context = {
                'uid' : uid,
                'sid' : sid,
            }
            return render(request,"societymemberapp/profile.html",context)
    else:
        return redirect("login")

def societymember_change_password(request):

    if "email" in request.session:
        uid = User.objects.get(email = request.session['email'])
        sid = Societymember.objects.get(user_id = uid)

        if request.POST:
            currentpassword = request.POST['currentpassword']
            newpassword = request.POST['newpassword']

            if uid.password == currentpassword:
                uid.password = newpassword
                uid.save()
                return redirect("logout")
            else:
                pass

            context = {
                'uid' : uid,
                'sid' : sid,
            }
            return render(request,"societymemberapp/profile.html",context)
        else:
            context = {
                'uid' : uid,
                'sid' : sid,
            }
            return render(request,"societymemberapp/profile.html",context)
        

def view_notice_society(request):
     if "email" in request.session:
        uid = User.objects.get(email = request.session['email'])
        sid = Societymember.objects.get(user_id = uid)
        nall = Notice.objects.all()
        context = {
                'uid' : uid,
                'sid' : sid, 
                'nall' : nall,
        }
        return render(request,"societymemberapp/notice-list.html",context)
     
def view_notice_society_details(request,pk):
     if "email" in request.session:
        print("----------->PK",pk)
        uid = User.objects.get(email = request.session['email'])
        sid = Societymember.objects.get(user_id = uid)
        notice_id = Notice.objects.get(id = pk)
 
        nall = NoticeViewDetails.objects.filter(user_id = uid,notice_id = notice_id)
        if len(nall) == 0:
            nid = NoticeViewDetails.objects.create(user_id = uid,notice_id = notice_id)


        notice = Notice.objects.filter(id = pk)
        context = {
                'uid' : uid,
                'sid' : sid, 
                'notice' : notice,
        }
        return render(request,"societymemberapp/notice-details.html",context)
     
    

def view_events_society(request):
     if "email" in request.session:
        uid = User.objects.get(email = request.session['email'])
        sid = Societymember.objects.get(user_id = uid)
        eall = Events.objects.all()
        context = {
                'uid' : uid,
                'sid' : sid, 
                'eall' : eall,
        }
        return render(request,"societymemberapp/events-list.html",context)
     
def view_events_society_details(request,pk):
     if "email" in request.session:
        print("----------->PK",pk)
        uid = User.objects.get(email = request.session['email'])
        sid = Societymember.objects.get(user_id = uid)
        event_id = Events.objects.get(id = pk)
        # print("=====> EVENT ID ",event_id)
 
        eall = EventsViewDetails.objects.filter(user_id = uid,event_id = event_id)
        if len(eall) == 0:
            eid = EventsViewDetails.objects.create(user_id = uid,event_id = event_id)


        event = Events.objects.filter(id = pk)
        # print("--------------->>pk",pk)
        context = {
                'uid' : uid,
                'sid' : sid, 
                'event' : event,
        }
        # print("------------------>>event",event)
        return render(request,"societymemberapp/events-details.html",context)
     

def add_complaints(request):
    if "email" in request.session:
        uid = User.objects.get(email = request.session['email'])
        sid = Societymember.objects.get(user_id = uid)

        if request.POST:
            cid = Complaints.objects.create(
                user_id = uid,
                title = request.POST['title'],
                description = request.POST['description'],
            )
            # print("-----> EID ",eid)
            call = Complaints.objects.all()
            context = {
                'uid' : uid,
                'sid' : sid, 
                'call' : call,
            }
            return render(request,"societymemberapp/complaints-list.html",context)
        else:
            context = {
                'uid' : uid,
                'sid' : sid, 
            }
            # print("outside the if part ")
            return render(request,"societymemberapp/add-complaints.html",context)
        
    else:
        return redirect("login")
    
def view_complaints(request):
     if "email" in request.session:
        print("____> SOCIETY ")
        uid = User.objects.get(email = request.session['email'])
        sid = Societymember.objects.get(user_id = uid)
        call = Complaints.objects.all()
        print("----->>>> CALL ",call)
        context = {
                'uid' : uid,
                'sid' : sid, 
                'call' : call,
        }
        return render(request,"societymemberapp/complaints-list.html",context)
    
def view_complaints_details(request,pk):
     if "email" in request.session:
        print("----------->PK",pk)
        uid = User.objects.get(email = request.session['email'])
        sid = Societymember.objects.get(user_id = uid)
        complaint = Complaints.objects.filter(id = pk)
        
        context = {
                'uid' : uid,
                'sid' : sid, 
                'complaint' : complaint,
        }
        return render(request,"societymemberapp/complaints-details.html",context)
     





            

     
