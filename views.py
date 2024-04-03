
from django.db.models import  Count, Avg
from django.shortcuts import render, redirect
from django.db.models import Count
from django.db.models import Q



# Create your views here.
from Remote_User.models import studentdata_Model,ClientRegister_Model


def collegeserverlogin(request):
    if request.method  == "POST":
        admin = request.POST.get('admin')
        password = request.POST.get('password')
        if admin == "Server" and password =="Server":
            return redirect('viewallclients')

    return render(request,'TServer/collegeserverlogin.html')


def Find_Student_Behavior_Prediction(request):
    regno = request.POST.get('regno')
    obj1 = studentdata_Model.objects.all().filter(Regno=regno)
    return render(request, 'TServer/Find_Student_Behavior_Prediction.html', {'objects': obj1})


def View_All_Behavioral_Change_ByLSTM(request):

    obj1=''
    btype= request.POST.get('btype')
    if btype=="Stress" :
      obj1 = studentdata_Model.objects.values('Regno','names','Stu_Class','Gender','Age','Stress')
    elif btype=="Mental Health" :
        obj1 = studentdata_Model.objects.values('Regno', 'names', 'Stu_Class', 'Gender', 'Age', 'Mental_Health')
    elif btype == "Intelligent":
        obj1 = studentdata_Model.objects.values('Regno', 'names', 'Stu_Class', 'Gender', 'Age', 'Intelligent')
    elif btype == "Executive Function":
        obj1 = studentdata_Model.objects.values('Regno', 'names', 'Stu_Class', 'Gender', 'Age', 'Executive_fun')
    elif btype == "Eating":
        obj1 = studentdata_Model.objects.values('Regno', 'names', 'Stu_Class', 'Gender', 'Age', 'Eating')
    elif btype == "Pyhsical Activity":
        obj1 = studentdata_Model.objects.values('Regno', 'names', 'Stu_Class', 'Gender', 'Age', 'Pyhsical_Activity')
    elif btype == "Sleep Pattern":
        obj1 = studentdata_Model.objects.values('Regno', 'names', 'Stu_Class', 'Gender', 'Age', 'Sleep_pattern')
    elif btype == "Social Tie":
        obj1 = studentdata_Model.objects.values('Regno', 'names', 'Stu_Class', 'Gender', 'Age', 'Social_Tie')
    elif btype == "Time Management":
        obj1 = studentdata_Model.objects.values('Regno', 'names', 'Stu_Class', 'Gender', 'Age', 'Time_Management')
    elif btype == "Time Management":
        obj1 = studentdata_Model.objects.values('Regno', 'names', 'Stu_Class', 'Gender', 'Age', 'Time_Management')
    elif btype == "Library Entry":
        obj1 = studentdata_Model.objects.values('Regno', 'names', 'Stu_Class', 'Gender', 'Age', 'Library_Entry')
    elif btype == "Online learning and Forum Discueeing":
        obj1 = studentdata_Model.objects.values('Regno', 'names', 'Stu_Class', 'Gender', 'Age', 'Online_learning')



    return render(request, 'TServer/View_All_Behavioral_Change_ByLSTM.html', {'objects': obj1})


def viewallclients(request):
    obj=ClientRegister_Model.objects.all()
    return render(request,'TServer/viewallclients.html',{'objects':obj})


def negativechart(request,chart_type):
    dd = {}
    pos, neu, neg = 0, 0, 0
    poss = None
    topic = studentdata_Model.objects.values('ratings').annotate(dcount=Count('ratings')).order_by('-dcount')
    for t in topic:
        topics = t['ratings']
        pos_count = studentdata_Model.objects.filter(topics=topics).values('names').annotate(topiccount=Count('ratings'))
        poss = pos_count
        for pp in pos_count:
            senti = pp['names']
            if senti == 'positive':
                pos = pp['topiccount']
            elif senti == 'negative':
                neg = pp['topiccount']
            elif senti == 'nutral':
                neu = pp['topiccount']
        dd[topics] = [pos, neg, neu]
    return render(request,'TServer/negativechart.html',{'object':topic,'dd':dd,'chart_type':chart_type})


def charts(request,chart_type):
    chart1 = studentdata_Model.objects.values('names').annotate(dcount=Avg('Attendance'))
    return render(request,"TServer/charts.html", {'form':chart1, 'chart_type':chart_type})

def dislikeschart(request,dislike_chart):
    charts = studentdata_Model.objects.values('names').annotate(dcount=Avg('dislikes'))
    return render(request,"TServer/dislikeschart.html", {'form':charts, 'dislike_chart':dislike_chart})

def View_College_Dataset_Details(request):
    chart = studentdata_Model.objects.all()
    return render(request,'TServer/View_College_Dataset_Details.html',{'objects':chart})


def Extract_PoorAcademic_PerformancePrediction(request):

    objs = studentdata_Model.objects.all().filter(Q(Stress='Not Manageable'), Q(Mental_Health='Poor') | Q(Pyhsical_Activity='No'), Q(Sleep_pattern='Late Night') )

    return render(request,'TServer/Extract_PoorAcademic_PerformancePrediction.html',{'objects':objs})
