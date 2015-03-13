from tab_converter.forms import TabConverterForm
from django.views.generic.edit import FormView
from django.core.urlresolvers import reverse_lazy


class TabConverterView(FormView):
    template_name = 'tab_converter/converter_base.html'
    form_class = TabConverterForm
    success_url = reverse_lazy('tabconverter:base')

    def form_valid(self, form, **kwargs):
        context = self.get_context_data(form=form)
        context['piano_tab'] = form.cleaned_data.get('guitar_tab')
        return self.render_to_response(context)
