from django.http.response import HttpResponse, HttpResponseNotAllowed
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .models import *
import requests

# Create your views here.
def homepage(request):
    return render(request,'base.html')
    # return HttpResponse("this is homepage")

#----------------------------Login-----------------------------------------------------
def login_page(request):
    if request.method=='POST':
        username1 = request.POST.get('username')
        password1 = request.POST.get('pwd')
        print(password1)
        user = authenticate(request,username = username1,password = password1)
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            return render(request,'login.html')
    else:   
        return render(request,'login.html')

#--------------------------Change Password----------------------------------------------
# def changepwd(request):
#     if request.method=='POST':
#         user = request.user.username
#         user1 = User.objects.get(username=user)
#         newpass = request.POST.get('newpwd')
#         user1.set_password(newpass)
#         user1.save()
#         return redirect('/administration-portal')
#     else:
#         return render(request,'Change.html')

#-----------------------------Logout----------------------------------------------------
def logout_view(request):
    logout(request)
    return redirect('/')

#-----------------------------SignUp----------------------------------------------
def signup(request):
    if request.method=='POST':
        username1 = request.POST.get('email')
        password1 = request.POST.get('password')
        firstname = request.POST.get('fname')
        lastname = request.POST.get('lname')
        email1 = request.POST.get('email')
        std=request.POST.get('standard')
        # print(password1)
        user = User.objects.create_user(username1, email1, password1)
        user.first_name = firstname
        user.last_name = std
        user.save()
        user1=LeaderBoard(email=email1,first_name=firstname,last_name=lastname,standard=std)
        user1.save()
        return redirect('/')

#---------------------------------Quiz---------------------------------------------------
def quiz(request):
    # if request.user.is_authenticated:
        # user=request.user
        # # row=user.UserDetails
        # std=user.last_name
        # print("Standard: ")
        # print(std)
        # std=UserDeails.get_standard(email=email1)
        # return render(request,'Quiz.html')
        # que=Question2.objects.filter(Standard=std)
        # que=Question2.objects.filter(standard='12',subject='Chemistry')
    que=Question2.objects.all()
    return render(request,'Quiz.html',{'que':que})
    
#---------------------------------Submit-----------------------------------------------
def submit(request):
    if request.method=='POST':
        marks=0
        for id in request.POST:
            val=request.POST.get(id)
            # print(val)
            # ans=Question2.Answer(id==val)
            if val=='2':
                marks=marks+2
        # user1=request.user.username
        # temp=LeaderBoard.objects.filter(email=user1)
        # for i in temp:    
        #     i.points=i.points+marks
        #     i.save()
        dict={'marks':marks}
        return render(request, 'markspage.html',dict)

def leaderboard(request):
    if request.user.is_authenticated:
        user1=request.user.username
        temp=LeaderBoard.objects.filter(email=user1)
        # print(temp)
        # std=12
        for i in temp:    
            std=i.standard
        context=LeaderBoard.objects.filter(standard=std).order_by('-points')
        return render(request,'leaderboard.html',{'context':context})
    else:
        return redirect('/login')


#My edits



def questionsearch(request):
    questionNumber=request.GET.get('problem')
    print(questionNumber)


    result = [item for item in Question.objects.all() if questionNumber== item.problemNo.lower()]

    ourword=result[0].word
    desc=result[0].desc
    wordlength = len(ourword)
    display= '_' * wordlength

    tries=5

    dict={'ourword':ourword,'display':display,'tries':tries, 'desc':desc}
    return render(request, 'gameproblem.html', dict )


def search(request):
    alphabet = request.GET.get('search').lower()
    display=request.GET.get('display').lower()
    ourword=request.GET.get('ourword').lower()
    desc = request.GET.get('desc')
    tries=request.GET.get('tries')
    tries=int(tries)

    game_over = False
    while not game_over:
        # remaining = 'you have ' + str(tries) + 'remaining'
        # print(display)
        # guess = input('Please guess a letter: ')
        guess = alphabet
        i = 0
        if guess in ourword:
            while ourword.find(guess, i) != -1:
                i = ourword.find(guess, i)
                display = display[:i] + guess + display[i + 1:]
                i += 1
            # print('Correct!')
            # correct = 'correcta'
            if display != ourword:
                dict = {'ourword': ourword, 'display': display, 'tries': tries,'desc':desc}
                return render(request, 'gameproblem.html', dict)


        else:
            # print('Sorry, wrong guess.')
            # wrongguess = 'wrongguessa'
            tries -= 1
            if tries!=0:
                dict = {'ourword': ourword, 'display': display, 'tries': tries,'desc':desc}
                return render(request, 'gameproblem.html', dict)

        if ourword == display:
            # print('you win' + word)
            # youwin = 'youwina'
            game_over = True
            return render(request,'congratespage.html')

        if tries == 0:
            game_over = True
            return render(request,'failed.html')





    dict = {'ourword': ourword, 'display': display, 'tries': tries,'desc':desc}
    return render(request, 'gameproblem.html', dict)

def home(request):
    return render(request, 'home.html')

def gamequestions(request):
    return render(request,'gamequestions.html')

def subjects(request):
    return render(request,'subjects.html')