from django.shortcuts import render
from .forms import regForm,loginForm
from .models import User
from django.contrib.auth.hashers import check_password,make_password


# Create your views here.
def showregForm(req):
    context={}
    print(req.method)
    
    if req.method=="POST":
        form=regForm(req.POST)
        
        if form.is_valid():

            uid=form.cleaned_data['userid']
            email=form.cleaned_data['email']
            pwd=form.cleaned_data['passward']
            cpwd=form.cleaned_data['retype_passward']
           # print(f"{uid} \n {email} \n {pwd} \n {cpwd}")

            

            if pwd!=cpwd :
                print(f"{uid} \n {email} \n {pwd} \n {cpwd}")
                context['notmatch']=True 
                print(context['notmatch'])              
            else:

                userobj=User.objects.filter(userid=uid)
                userobj2=User.objects.filter(email=email)
                userobj3=User.objects.filter(userid=uid).filter(email=email) 
                print(userobj,userobj2,userobj3)

                if len(userobj)==0 and len(userobj2)==0: 
                   # form.__setattr__('passward',make_password(str(pwd)))
                   # print(form.__getattribute__('passward'))           
                    print(form.data)
                    
                    userobj=form.save(commit=False)
                    #print(userobj)
                    
                    ps=make_password(str(pwd))
                    userobj.__setattr__('passward',ps)
                    userobj.__setattr__('retype_passward',ps)
                    #print(userobj.retype_passward)
                    userobj.save()
                    
                    
                    #print(userobj)
                    #print(f"{uid} \n {email} \n {pwd} \n {cpwd}")

                    context['notmatch']=False    
                    context["success"]=True    
                    context['userid']=uid
                    #return render(req,'registerapp/signup.html',context)  
                else:
                    
                    if len(userobj)!=0:  
                        context["exist"]='userid'
                    elif len(userobj2)!=0:
                        context['exist']='email'
                    
                    #return render(req,'registerapp/signup.html',context)
        

    
    else:        
        form=regForm()

    #context={'form':form}
    context['form']=form
    print(context)
    
    return render(req,'registerapp/signup.html',context)


def showloginForm(req):
    context={}
    print(req.method)
    
    if req.method=="POST":
        form=loginForm(req.POST)
        if form.is_valid():

            uid=form.cleaned_data['userid']
            pwd=form.cleaned_data['passward']
            print(form.cleaned_data)
           
            print(f"{uid}  \n {pwd}")
            #userobj=form.save()
            
            userobj= User.objects.filter(userid=uid)
               
            #print(userobj[0].passward)
            if len(userobj)==0:
                context["fail"]='userid'
           
            elif check_password(str(pwd),userobj[0].passward) :
                
                context['user']={'name':userobj[0].name , 'userid':uid ,'email':userobj[0].email , "phone" : userobj[0].phone_no}
                print(context)
                print(context['user'])
                
                return render(req,'registerapp/user.html',context)
                
                 
            else:
                #form=loginForm()   
                context["fail"]='passward'  
                #return render(req,'registerapp/loginform.html',context)    
            
            
    else:
        form=loginForm()
    context['loginform']=form
    return render(req,'registerapp/loginform.html',context)


            


