from tab_converter.forms import TabConverterForm
from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse

class TabConverterView(FormView):
    template_name = 'tab_converter/converter_base.html'
    form_class = TabConverterForm
    success_url = reverse_lazy('tabconverter:success')

    def form_valid(self, form, **kwargs):
        
        self.request.session['converted_tab'] = form.convert_to_piano_tab() #change to tablature model
        return super(TabConverterView, self).form_valid(form) 
    
      
class ConversionSuccessView(TemplateView):
    template_name = 'tab_converter/converter_success.html'
    
    """def get_context_data(self, **kwargs):
    
      return {'test' : 'checking context'}"""
    
       
