from django.shortcuts import render, get_object_or_404
from .models import User, Event
from django.http import HttpResponseRedirect

# Create your views here.


def home(request):
    return render(request, "base.html", {})


def login(request):
    errors = None
    if request.method == 'POST':
        u = User.objects.get(username=request.POST['username'])
        if u.exist():
            if u.password == request.POST['password']:
                request.session['Username'] = u.username
                return HttpResponseRedirect(f'/{u.username}/')
            else:
                errors = 'password incorrect'
                return render(request, "base.html", {'errors': errors})
        else:
            errors = 'username incorrect'
            return render(request, "base.html", {'errors': errors})
    return render(request, "base.html", {'errors': errors})


def logout(request):
    try:
        del request.session['Username']
    except KeyError:
        pass
    return HttpResponseRedirect('/login/')


def register(request):
    errors = None
    if request.method == 'POST':
        username = request.POST['username']
        object_list = User.objects.all()
        for obj in object_list:
            if username == obj.username:
                errors = f'already have a user with username: {username}'
                return render(request, "base.html", {'errors': errors})
        password1 = request.POST['password']
        password2 = request.POST['repassword']
        if password1 == password2:
            User.objects.create(
                username=username,
                password=password1,
                email=request.POST['email']
            )
            request.session['Username'] = username
            return HttpResponseRedirect(f'/{username}/')
        else:
            errors = 'password confirm is not match with your password'
            return render(request, "base.html", {'errors': errors})
    return render(request, "base.html", {'errors': errors})


def show_program(request , **kwargs):
    name = kwargs.get('slug')
    username = request.session['Username']
    if name == username:
        events = Event.objects.filter(owner__username__iexact=username)
        return render(request, "base.html", {'events': events})
    else:
        errors = 'login to your account to see your program'
        return render(request, "base.html", {'errors': errors})


def create(request , **kwargs):
    name = kwargs.get('slug')
    username = request.session['Username']
    if name == username:
        events = Event.objects.filter(owner__username__iexact=username)
        if request.method == 'POST':
            date = request.POST['date']
            from_ = request.POST['from']
            until_ = request.POST['until']
            title = request.POST['title']
            if from_ <= until_:
                errors = 'time is incorrect'
                return render(request, "base.html", {'errors': errors})
            for obj in events:
                if obj.title == title:
                    errors = f'already have an event title: {title}'
                    return render(request, "base.html", {'errors': errors})
                if (not obj.date == date) or from_ >= obj.untill or until_ <= obj.fromm:
                    pass
                else:
                    errors = 'already have an event in this time'
                    return render(request, "base.html", {'errors': errors})
            Event.objects.create(
                owner=User.objects.get(username__iexact=username),
                date=date,
                fromm=from_,
                untill=until_,
                title=title,
                note=request.POST['note'],
            )
            return HttpResponseRedirect(f'/{username}/')
        return render(request, "base.html", {})
    else:
        errors = 'login to your account to add an event in your program'
        return render(request, "base.html", {'errors': errors})


def edit(request, **kwargs):
    name = kwargs.get('slug')
    event_title = kwargs.get('event_title')
    username = request.session['Username']
    if name == username:
        events = Event.objects.filter(owner__username__iexact=username)
        event = get_object_or_404(Event, title__iexact=event_title, owner__username__iexact=username)
        if request.method == 'POST':
            date = request.POST['date']
            from_ = request.POST['from']
            until_ = request.POST['until']
            title = request.POST['title']
            note = request.POST['note']
            if from_ <= until_:
                errors = 'time is incorrect'
                return render(request, "base.html", {'errors': errors})
            for obj in events:
                if not obj == event:
                    if obj.title == title:
                        errors = f'already have an event title: {title}'
                        return render(request, "base.html", {'errors': errors})
                    if (not obj.date == date) or from_ >= obj.untill or until_ <= obj.fromm:
                        pass
                    else:
                        errors = 'already have an event in this time'
                        return render(request, "base.html", {'errors': errors})
            if date is not None:
                event.date = date
            if from_ is not None:
                event.fromm = from_
            if until_ is not None:
                event.untill = until_
            if title is not None:
                event.title = title
            if note is not None:
                event.note = note
            return HttpResponseRedirect(f'/{username}/')
        return render(request, "base.html", {'event': event})
    else:
        errors = 'login to your account to edit an event in your program'
        return render(request, "base.html", {'errors': errors})


def delete(request, **kwargs):
    name = kwargs.get('slug')
    event_title = kwargs.get('event_title')
    username = request.session['Username']
    if name == username:
        if request.method == 'POST':
            get_object_or_404(Event, title__iexact=event_title, owner__username__iexact=username).delete()
    else:
        errors = 'login to your account to delete an event from your program'
        return render(request, "base.html", {'errors': errors})
