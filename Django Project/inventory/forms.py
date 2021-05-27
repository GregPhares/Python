from django import forms
from .models import *

class AminoForm(forms.ModelForm):
    class Meta:
        model = Amino
        fields = ('Name','Number of Flavors', 'Product Rating', 'Price','Price Per Serving','Category','Description','Top Flavor','Url')

class BcaaForm(forms.ModelForm):
    class Meta:
        model = Bcaa
        fields = ('Name','Number of Flavors', 'Product Rating', 'Price','Price Per Serving','Category','Description','Top Flavor','Url')

class BetaForm(forms.ModelForm):
    class Meta:
        model = Beta
        fields = ('Name','Number of Flavors', 'Product Rating', 'Price','Price Per Serving','Category','Description','Top Flavor','Url')

class CaffeineForm(forms.ModelForm):
    class Meta:
        model = Caffeine
        fields = ('Name','Number of Flavors', 'Product Rating', 'Price','Price Per Serving','Category','Description','Top Flavor','Url')

class LCForm(forms.ModelForm):
    class Meta:
        model = LC
        fields = ('Name','Number of Flavors', 'Product Rating', 'Price','Price Per Serving','Category','Description','Top Flavor','Url')

class NewOneForm(forms.ModelForm):
    class Meta:
        model = NewOne
        fields = ('Name','Number of Flavors', 'Product Rating', 'Price','Price Per Serving','Category','Description','Top Flavor','Url')

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('Name','Number of Flavors', 'Product Rating', 'Price','Price Per Serving','Category','Description','Top Flavor','Url')

class PreForm(forms.ModelForm):
    class Meta:
        model = Pre
        fields = ('Name','Number of Flavors', 'Product Rating', 'Price','Price Per Serving','Category','Description','Top Flavor','Url')

class ProteinForm(forms.ModelForm):
    class Meta:
        model = Protein
        fields = ('Name','Number of Flavors', 'Product Rating', 'Price','Price Per Serving','Category','Description','Top Flavor','Url')

class RecoveryForm(forms.ModelForm):
    class Meta:
        model = Recovery
        fields = ('Name','Number of Flavors', 'Product Rating', 'Price','Price Per Serving','Category','Description','Top Flavor','Url')

class TestForm(forms.ModelForm):
    class Meta:
        model = Test
        fields = ('Name','Number of Flavors', 'Product Rating', 'Price','Price Per Serving','Category','Description','Top Flavor','Url')

