from django import forms
g=[('MALE','MALE'),('FEMALE','FEMALE')]

class StudentForm(forms.Form):
    name=forms.CharField(max_length=100)
    age=forms.IntegerField()
    email=forms.EmailField()
    password=forms.CharField(max_length=100,widget=forms.PasswordInput)
    address=forms.CharField(max_length=300,widget=forms.Textarea(attrs={'cols':5,'rows':5}))
    gender=forms.ChoiceField(choices=g)