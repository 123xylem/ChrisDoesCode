from django import forms

class contactMeForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',  # Add custom CSS classes
        'placeholder': 'Your Name'
    }), label='form-name')
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Your Email'
    }), label='form-email')
    message = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'rows': 5,
        'placeholder': 'Your Message'
    }), label='form-message')
