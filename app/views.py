from django.shortcuts import render, get_object_or_404, redirect
from .models import Course, Category, Teacher, Lesson, Video
from django.contrib.auth import login, authenticate
from .forms import SignUpForm, LoginForm, CourseForm
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import DeleteView
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

# Create your views here.
def home(request):
    categories = Category.objects.all()
    courses = Course.objects.all()
    teachers = Teacher.objects.all()

    data = {
        'categories': categories,
        'courses': courses,
        'teachers': teachers,
    }
    return render(request, 'home.html', data)

def detail(request, id):
    course = get_object_or_404(Course, id=id)
    categories = Category.objects.all()

    data = {
        'course': course,
        'categories': categories,
    }
    return render(request, 'detail.html', data)

def courses(request, id):
    categories = Category.objects.all()
    courses = Course.objects.filter(category_id=id)

    data = {
        'categories': categories,
        'courses': courses,
    }
    return render(request, 'courses.html', data)

def all_courses(request):
    categories = Category.objects.all()
    courses = Course.objects.all()

    data = {
        'categories': categories,
        'courses': courses,
    }
    return render(request, 'courses.html', data)

def search(request):
    query = request.GET.get('q')
    categories = Category.objects.all()
    if query:
        courses = Course.objects.filter(name__icontains=query)
    else:
        courses = Course.objects.none()

    return render(request, 'courses.html', {'courses': courses, 'categories': categories})

def teachers(request):
    teachers = Teacher.objects.all()
    categories = Category.objects.all()


    data = {
        'teachers': teachers,
        'categories': categories,
    }

    return render(request, 'teachers.html', data)

def teacher_detail(request, id):
    teacher = get_object_or_404(Teacher, id=id)
    teachers = Teacher.objects.all()
    categories = Category.objects.all()


    data = {
        'teacher': teacher,
        'categories': categories,
        'teachers': teachers,
    }
    return render(request, 'teacher-detail.html', data)

def lesson_detail(request, id, lesson_id, slug):
    course = get_object_or_404(Course, id=id)
    categories = Category.objects.all()
    lesson = get_object_or_404(Lesson, id=lesson_id)
    video = get_object_or_404(Video, slug=slug)

    data = {
        'course': course,
        'lesson': lesson,
        'video': video,
        'categories': categories,
    }
    return render(request, 'lesson_detail.html', data)

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'accounts/sign_up.html', {'form': form})

def login_view(request):
    form = LoginForm(data=request.POST or None)

    if request.method == 'POST' and form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            form.add_error(None, 'Invalid username or password.')

    return render(request, 'accounts/sign_in.html', {'form': form})


class CourseCreateView(CreateView):
    model = Course
    form_class = CourseForm
    template_name = 'create.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        return super().form_valid(form)

class CourseUpdateView(UpdateView):
    model = Course
    form_class = CourseForm
    template_name = 'create.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        return super().form_valid(form)

class CourseDeleteView(DeleteView):
    model = Course
    success_url = reverse_lazy('home')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.delete()
        return HttpResponseRedirect(success_url)
