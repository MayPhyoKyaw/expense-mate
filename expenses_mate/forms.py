from django import forms # type: ignore
from .models import ExpenseGroup, Expense


class ExpenseGroupForm(forms.ModelForm):
    """
    新規データ登録画面用のフォーム定義
    """
    class Meta:
        model = ExpenseGroup
        fields =['title']
        
    def __init__(self, *args, **kwargs):
        super(ExpenseGroupForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({
            'class': 'expenses-list-input',
            'placeholder': ' ',
            'id': 'input__username'
        })
        

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['item_name', 'amount']
        
    def __init__(self, *args, **kwargs):
        super(ExpenseForm, self).__init__(*args, **kwargs)
        self.fields['item_name'].widget.attrs.update({
            'class': 'expenses-list-input',
            'placeholder': ' ',
            'id': 'input__item_name'
        })
        
        self.fields['amount'].widget.attrs.update({
            'class': 'expenses-list-input',
            'placeholder': ' ',
            'id': 'input__amount'
        })