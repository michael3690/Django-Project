from django import forms

class ContactForm(forms.Form):
    your_name = forms.CharField(max_length=100, label='Your name:', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Add your name here"}))
    email = forms.EmailField(required=False,label='Your e-mail address:', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Add your e-mail address here"}))
    subject = forms.CharField(max_length=100, label="Subject:", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Add your subject here"}))
    message = forms.CharField(label="Your Message:", widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': "Add your message here"}))
