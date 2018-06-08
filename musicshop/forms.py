from django import forms
from django.core.exceptions import ObjectDoesNotExist
from musicshop.models import User, Seller, Client, Article, TArticle, Order, ODetailt


class OrderCreationForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = '__all__'


class UserCreationForm(forms.ModelForm):

    password1 = forms.CharField(label='Ingrese Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Ingrese Contraseña Nuevamente', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'user_type', )
        exclude = ('password', )

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden", code='invalid')
        else:
            return password2

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        try:
            user_db = User.objects.filter(username=user.username)
        except ObjectDoesNotExist:
            pass
        else:
            user.set_password(self.cleaned_data.get('password2'))
            user = super(UserCreationForm, self).save(commit=True)
            if user.user_type == 'Seller':
                count = Seller.objects.all().count()
                Seller.objects.create(user=user, code=count+1)
            elif user.user_type == 'Client':
                Client.objects.create(user=user)
        if commit:
            user.save()
        return user
