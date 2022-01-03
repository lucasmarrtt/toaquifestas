from django.forms import ModelForm
from . models import Solicitacao, Reclamacoes

class SolicitacaoForm(ModelForm):
	class Meta:
		model = Solicitacao
		fields = '__all__'


class ReclamacoesForm(ModelForm):
	class Meta:
		model = Reclamacoes
		fields = '__all__'