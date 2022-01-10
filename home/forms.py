from django.forms import ModelForm
from . models import Solicitacao, Reclamacoes, Renovacao 

class SolicitacaoForm(ModelForm):
	class Meta:
		model = Solicitacao
		fields = '__all__'


class ReclamacoesForm(ModelForm):
	class Meta:
		model = Reclamacoes
		fields = '__all__'


class RenovacaoForm(ModelForm):
	class Meta:
		model = Renovacao 
		fields = '__all__'
