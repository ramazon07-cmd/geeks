from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser, Course

class SignUpForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']

    username = forms.CharField(
        label='User Name',
        widget=forms.TextInput(attrs={
            'id': 'signUpName',
            'class': 'form-control',
            'placeholder': 'User Name',
            'required': True,
        })
    )

    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={
            'id': 'signUpEmail',
            'class': 'form-control',
            'placeholder': 'Email address here',
            'required': True,
        })
    )

    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={
            'id': 'signUpPassword',
            'class': 'form-control',
            'placeholder': '**************',
            'required': True,
        })
    )

    password2 = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput(attrs={
            'id': 'signUpPasswordConfirm',
            'class': 'form-control',
            'placeholder': '**************',
            'required': True,
        })
    )

class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label='Username or Email',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Username or Email',
            'required': True,
        })
    )

    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': '**************',
            'required': True,
        })
    )

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'trailer', 'category', 'image', 'teacher', 'status', 'total_videos', 'total_duration', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'id': 'editor', 'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Course Title'}),
             'teacher': forms.Select(attrs={'class': 'form-select choices__input', 'id': 'addCourseTeacher'}),
            'category': forms.Select(attrs={'class': 'form-select choices__input', 'id': 'addCourseCategory'}),
            'status': forms.Select(attrs={'class': 'form-select choices__input', 'id': 'addCourseLevel'}),
            'trailer': forms.FileInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'input-hidden'}),
            'total_videos': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Total Videos'}),
            'total_duration': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Total Duration in Minutes'}),
        }
