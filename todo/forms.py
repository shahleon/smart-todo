from django import forms


class UpdateItemTextForm(forms.Form):
    item_text = forms.Textarea()
    # hidden_item_id = forms.CharField(label=)