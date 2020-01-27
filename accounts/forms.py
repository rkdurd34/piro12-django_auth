from django.contrib.auth.forms import UserCreationForm
from django.core.validators import validate_email
class SignupForm(UserCreationForm):
    def __init__(self, *args ,**kwargs):
        super().__init__(*args ,**kwargs)
        self.fields['username'].validators=[validate_email]#이메일인지 검사
        self.fields['username'].help_text = 'ENTER EMAIL FORMAT'#커스터마이징!
        self.fields['username'].label = 'mail'
    def save(self,commit=True):
        user = super().save(commit=True)
        user.email = user.username
        if commit:
            user.save()
        return user



"""
    def clean_username(self):
        value = self.cleaned_data.get('username')
        if value:
            validate_email(value)
        return value
"""

#여기서 폼 관련 수정 하기
#폼 관련 커스터마이징은 종류가 엄청 많음!