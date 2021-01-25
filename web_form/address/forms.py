from django import forms

class AddressForm(forms.Form):
    cep = forms.CharField(max_length=9, label='CEP', required=True)
    rua = forms.CharField(max_length=100, label='Rua', required=True)
    bairro = forms.CharField(max_length=100, label='Bairro', required=True)
    num = forms.CharField(max_length=10, label='Número Residencial', required=True)
    numcompl = forms.CharField(max_length=10, label='Número Complementar', required=True)
    estado = forms.CharField(max_length=50, label='Estado', required=True)
    uf = forms.CharField(max_length=2, label='UF', required=True)
    descricao = forms.CharField(max_length=255, label='Descrição', widget=forms.Textarea(), required=False)
