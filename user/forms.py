from attr import field, fields
from django.forms import ModelForm
from .models import *


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['isim','resim']
        
    def __init__(self,*args,**kwargs):
        super(ProfileForm,self).__init__(*args, **kwargs)
        for name, field in self.fields.items(): # items kullandığım için bu dictinory yani 2 sinede ihtiyaç var naem ile ismin döngüsünü field ile valueleri
            field.widget.attrs.update({'class':'form-control'})
            
class AccountForm(ModelForm):
    class Meta:
        model = Account
        fields = ['resim','tel']
        
    def __init__(self,*args,**kwargs):
        super(AccountForm,self).__init__(*args, **kwargs)
        for name, field in self.fields.items(): # items kullandığım için bu dictinory yani 2 sinede ihtiyaç var naem ile ismin döngüsünü field ile valueleri
            field.widget.attrs.update({'class':'form-control'})