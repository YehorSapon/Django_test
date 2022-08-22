from django.forms import DateInput, ModelForm
from crispy_forms.layout import Submit
from crispy_forms.helper import FormHelper
from order.models import Order


class AddOrderForm(ModelForm):
    class Meta:
        model = Order
        fields = [
            'cart',
            'status',
            'address',
        ]

    def __init__(self, *args, **kwargs):
        super(AddOrderForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'blueForms'
        # self.helper.form_method = 'POST'
        # self.helper.add_input(
        #      Submit('submit', 'Add order', css_class='btn-primary'))


class EditOrderForm(ModelForm):
    class Meta:
        model = Order
        fields = [
            'cart',
            'status',
            'address',
        ]

    def __init__(self, *args, **kwargs):
        super(EditOrderForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'POST'
        self.helper.add_input(
            Submit('submit', 'Edit order', css_class='btn-primary'))
