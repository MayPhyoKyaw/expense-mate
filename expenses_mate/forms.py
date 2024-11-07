from django import forms # type: ignore
from .models import ExpenseGroup, Expense, User


class ExpenseGroupForm(forms.ModelForm):
    """
    新規データ登録画面用のフォーム定義
    """
    shared_with = forms.ModelMultipleChoiceField(
        queryset=User.objects.all(),  # You can filter if necessary
        widget=forms.SelectMultiple(attrs={
            'class': 'expenses-list-input',
            'id': 'input__shared_with'
        }),
        required=False  # Makes this field optional
    )
    
    class Meta:
        model = ExpenseGroup
        fields =['title', 'shared_with']
        
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