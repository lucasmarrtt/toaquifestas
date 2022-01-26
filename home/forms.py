from django.forms import ModelForm
from django import forms
from . models import Solicitacao, Reclamacoes, Renovacao, City, District

# Local Flavor
from localflavor.br.br_states import STATE_CHOICES

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


class StateForm(forms.Form):
	state = forms.ChoiceField(
		choices=STATE_CHOICES,
		label='Estado',
	)

	class Meta:
		fields = ('state', )
