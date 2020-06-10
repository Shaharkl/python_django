import email

from django import forms


from .models import Product


class ProductForm(forms.ModelForm):
    title = forms.CharField(label='',
                            widget=forms.TextInput(attrs={"placeholder": "your title"}))  # deafult required=True
    email = forms.EmailField()
    description = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                "placeholder": "your des",
                "class": "new class name two",
                "rows": 20,
                "cols": 20

            }
        )
    )

    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]

    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get('title')
        if "CFE" in title:
            return title
        else:
            raise forms.ValidationError("This is not valid title")

    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        if not email.endswith("edu"):
            raise forms.ValidationError("This is not valid title")
        return email


class RowProductForm(forms.Form):
    title = forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder": "your title"}))#deafult required=True
    description = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                "placeholder": "your des",
                "class": "new class name two",
                "rows": 20,
                "cols": 20

            }
        )
    )#deafult
    price = forms.DecimalField(initial=199.99)
