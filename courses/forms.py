from django import forms

class ContactCourse(forms.Forms):

    name = forms.CharField(labels='Name', max_length = 100)
    email = forms.EmailField(labels='E-mail')
    message = forms.CharField(
        labels='Menssagem/Dúvida', widget= forms.Textarea
    )
