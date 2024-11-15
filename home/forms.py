from django import forms

class ContatoForm(forms.Form):
    nome = forms.CharField(
        label="Nome Completo",
        max_length=250,
       
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Insira o seu nome' })
        )
    email = forms.EmailField(
        label="Email",
        max_length=250,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'insira o seu email'})
        )
    mensagem = forms.CharField(
        label="Mensagem",
        max_length=250,
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Insira sua mensagem'})
    )
    
    
class ProdutoForm(forms.Form):
    nome = forms.CharField(
        label="Nome",
        max_length=250,
        widget=forms.TextInput(attrs={"class": "form-control", 'placeholder': 'Insira o nome do produto...'})
    )
    preco = forms.DecimalField(
        label="Preço",
        max_digits=10,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Preço'})
    )