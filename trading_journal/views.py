from django.shortcuts import render,redirect, get_object_or_404
from django.views.generic import TemplateView
from .forms import CurrencyPairForm
from .models import CurrencyPair
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    return render(request, 'trading_journal/home.html')


class CurrencyPairView(LoginRequiredMixin, TemplateView):
    template_name = "trading_journal/new_trade.html"


    def get(self, request):
        form = CurrencyPairForm()
        return render(request, self.template_name, {'form':form})

    def post(self, request):         
        form = CurrencyPairForm(request.POST, request.FILES)
        if form.is_valid():
            form.save() 
            pair = form.cleaned_data['pair'],    
            opening_price = form.cleaned_data['opening_price'],
            closing_price = form.cleaned_data['closing_price'],
            take_profit = form.cleaned_data['take_profit'],
            stop_loss = form.cleaned_data['stop_loss'],
            lot_size = form.cleaned_data['lot_size'],
            trade_screenshort= form.cleaned_data['trade_screenshort']
            date_added = form.cleaned_data['date_added'],
            reason =  form.cleaned_data['reason'],
            result = form.cleaned_data['result']
            return redirect('http://127.0.0.1:8000/trades/')
        else:
            form = CurrencyPairForm()
            return render(request, self.template_name, {'form':form})
        
        arg = {'form':form,
               'pair': pair,
               'OpeningPrice':opening_price,
               'ClosingPrice':closing_price,
               'TakeProfit':take_profit,
               'StopLoss':stop_loss,
               'LotSize':lot_size,
               'TradeScreenshort':trade_screenshort,
               'Date':date_added,
               'Reason':reason,
               'Result':result,}
        return render(request, self.template_name)

@login_required
def display_trades(request):
    trades = CurrencyPair.objects.filter(user=request.user)
    
    return render(request, 'trading_journal/trades.html', {'trades':trades})


    


        
        
 

