from   django import  forms
class TaskForm(forms.Form):
    title = forms.CharField(max_length=50,required=True, label='title')
    description = forms.CharField(max_length=2000, required=True,label='description')
    status = forms.CharField(max_length=50, required=True)
    date = forms.CharField(max_length=50, required=True)
