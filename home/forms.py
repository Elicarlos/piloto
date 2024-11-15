from django import forms

class ContatoForm(forms.Form):
    nome = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    mensagem = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    
    
class ProdutoForm(forms.Form):
    nome = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    preco = forms.DecimalField(widget=forms.TextInput(attrs={'class': 'form-control'}))