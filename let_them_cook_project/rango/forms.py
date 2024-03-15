from django import forms
from rango.models import Recipe, Review
from django.contrib.auth.models import User
from rango.models import UserProfile


# page, catgeory
class RecipeForm(forms.ModelForm):
    title = forms.CharField(max_length=255)
    quick_description = forms.CharField(widget = forms.Textarea())
    content = forms.CharField(widget = forms.Textarea())
    ingredients = forms.CharField(widget = forms.Textarea(), help_text="List each ingredient on a new line.")
    picture = forms.ImageField(upload_to='recipes/', blank=True, null=True)
   #? user = forms.ForeignKey(User, on_delete=models.CASCADE, related_name='recipes')
    
    class Meta:
        model = Recipe
        fields = ('__all__')

class ReviewForm(forms.ModelForm):
    content = forms.CharField(widget = forms.Textarea())
    rating = forms.IntegerField()
    #recipe = forms.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='reviews')
    #user = forms.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')

    class Meta:
        model = Review
        fields = ('__all__')

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password',)

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('website', 'picture',)
