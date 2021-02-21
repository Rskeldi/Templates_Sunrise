from django.contrib.auth import get_user_model
from django.forms import ModelForm

User = get_user_model()


class UserEditForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({'class': 'postInpName'})
        self.fields['last_name'].widget.attrs.update({'class': 'postInpLast'})


    class Meta:
        model = User
        fields = ('first_name', 'last_name')
