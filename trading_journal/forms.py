from django import forms
from .models import CurrencyPair

class CurrencyPairForm(forms.ModelForm):
    """The currency pair user will trade"""

    class Meta:
        model = CurrencyPair
        fields = ('__all__')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['pair'].widget.attrs.update({'class' : 'form-control'})
        self.fields['pair'].widget.attrs.update({'placeholder' : "'GBPUSD'"})
        self.fields['opening_price'].widget.attrs.update({'class' : 'form-control'})
        self.fields['opening_price'].widget.attrs.update({'placeholder' : 'Enter opening price'})
        self.fields['closing_price'].widget.attrs.update({'class' : 'form-control'})
        self.fields['closing_price'].widget.attrs.update({'placeholder' : 'Enter closing price'})
        self.fields['take_profit'].widget.attrs.update({'class' : 'form-control'})
        self.fields['take_profit'].widget.attrs.update({'placeholder' : 'Enter take profit'})
        self.fields['stop_loss'].widget.attrs.update({'class' : 'form-control'})
        self.fields['stop_loss'].widget.attrs.update({'placeholder' : 'Enter stop loss'})
        self.fields['lot_size'].widget.attrs.update({'class' : 'form-control'})
        self.fields['lot_size'].widget.attrs.update({'placeholder' : 'Enter lot size'})
        self.fields['date_added'].widget.attrs.update({'class' : 'form-control'})
        self.fields['date_added'].widget.attrs.update({'placeholder' : '01/01/2023'})
        self.fields['reason'].widget.attrs.update({'class' : 'form-control'})
        self.fields['reason'].widget.attrs.update({'placeholder' : 'Enter reasons for trade'})
        self.fields['result'].widget.attrs.update({'class' : 'form-control'})
        self.fields['result'].widget.attrs.update({'placeholder' : 'Enter perentage profit/loss'})