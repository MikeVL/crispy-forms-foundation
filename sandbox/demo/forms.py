from django import forms
from django.utils.translation import ugettext_lazy as _

from crispy_forms.helper import FormHelper
from crispy_forms_foundation.layout import Layout, Fieldset, TabItem, TabHolder, AccordionHolder, AccordionItem

from .crispies import (part_1_crispies, part_2_crispies, part_3_crispies,
                       part_4_crispies, buttons_crispies)


SELECT_INPUT_CHOICES = [(f'item-{i}', f'Option item {i}')
                        for i in range(1, 6)]
RADIO_INPUT_CHOICES = [(f'item-{i}', f'Radio item {i}')
                       for i in range(1, 4)]


class BaseForm(forms.Form):
    """
    Base form with inputs
    """
    full_input = forms.CharField(label=_('Full width input'), widget=forms.TextInput(
        attrs={'required': ''}), required=True, help_text='This is a sample field help text.')
    column_input_1 = forms.CharField(label=_('Column input 1'), required=False)
    column_input_2 = forms.CharField(label=_('Column input 2'), required=True)
    column_input_3 = forms.CharField(label=_('Column input 3'), required=False)
    textarea_input = forms.CharField(label=_('Textarea'), widget=forms.Textarea(
        attrs={'rows': 5, 'required': ''}), required=True)
    select_input = forms.ChoiceField(
        label=_('Select input'), choices=SELECT_INPUT_CHOICES, required=True)
    radio_input = forms.ChoiceField(label=_(
        'Radio inputs'), choices=RADIO_INPUT_CHOICES, widget=forms.RadioSelect, required=False)
    checkbox_input = forms.BooleanField(
        label=_('Checkbox input'), required=False)
    checkbox_switch_input_1 = forms.BooleanField(
        label=_('Checkbox switch'), required=False)
    checkbox_switch_input_2 = forms.BooleanField(
        label=_('Checkbox inline switch'), required=False)
    inlinefield_input = forms.CharField(label=_('Inline field'), required=False)
    inlinejustifiedfield_input = forms.CharField(
        label=_('Inline justified field'), required=False)

    def clean(self):
        cleaned_data = super().clean()
        checkbox_input = cleaned_data.get('checkbox_input')

        if checkbox_input and checkbox_input == True:
            raise forms.ValidationError([
                'This is a global error',
                'This is another global error',
                'Uncheck the "Checkbox input" to ignore these errors']
            )

        # Always return the full collection of cleaned data.
        return cleaned_data

    def save(self, commit=True):
        # Do nothing
        return


class FormCrispyHelperMixin:
    """
    Form that define an empty helper and able to switch template pack
    """

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.template_pack = kwargs.pop('pack')

        super().__init__(*args, **kwargs)


class FormByFieldsetsForm(FormCrispyHelperMixin, BaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper.attrs = {'data_abide': '', 'novalidate': ''}
        self.helper.form_action = '.'

        part1 = [_('Part 1')]+part_1_crispies(pack=self.helper.template_pack)
        part2 = [_('Part 2')]+part_2_crispies(pack=self.helper.template_pack)
        part3 = [_('Part 3')]+part_3_crispies(pack=self.helper.template_pack)
        part4 = [_('Part 4')]+part_4_crispies(pack=self.helper.template_pack)

        self.helper.layout = Layout(
            Fieldset(*part1),
            Fieldset(*part2),
            Fieldset(*part3),
            Fieldset(*part4),
            *buttons_crispies(pack=self.helper.template_pack)
        )


class FormByTabsForm(FormCrispyHelperMixin, BaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper.attrs = {'data_abide': ''}
        self.helper.form_action = '.'

        part1 = [_('Part 1')]+part_1_crispies(pack=self.helper.template_pack)
        part2 = [_('Part 2')]+part_2_crispies(pack=self.helper.template_pack)
        part3 = [_('Part 3')]+part_3_crispies(pack=self.helper.template_pack)
        part4 = [_('Part 4')]+part_4_crispies(pack=self.helper.template_pack)

        self.helper.layout = Layout(
            TabHolder(
                TabItem(*part1),
                TabItem(*part2),
                TabItem(*part3),
                TabItem(*part4),
            ),
            *buttons_crispies(pack=self.helper.template_pack)
        )


class FormByAccordionsForm(FormCrispyHelperMixin, BaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper.attrs = {'data_abide': ''}
        self.helper.form_action = '.'

        part1 = [_('Part 1')]+part_1_crispies(pack=self.helper.template_pack)
        part2 = [_('Part 2')]+part_2_crispies(pack=self.helper.template_pack)
        part3 = [_('Part 3')]+part_3_crispies(pack=self.helper.template_pack)
        part4 = [_('Part 4')]+part_4_crispies(pack=self.helper.template_pack)

        self.helper.layout = Layout(
            AccordionHolder(
                AccordionItem(*part1),
                AccordionItem(*part2),
                AccordionItem(*part3),
                AccordionItem(*part4),
            ),
            *buttons_crispies(pack=self.helper.template_pack)
        )
