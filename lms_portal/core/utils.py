from django.template.loader import render_to_string
from django.http import HttpResponse
from weasyprint import HTML
import tempfile


def render_to_pdf(template_src, context_dict={}):
    html_string = render_to_string(template_src, context_dict)
    html = HTML(string=html_string)

    result = tempfile.NamedTemporaryFile(delete=True, suffix=".pdf")
    html.write_pdf(target=result.name)

    with open(result.name, 'rb') as pdf_file:
        response = HttpResponse(pdf_file.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'inline; filename="report.pdf"'
        return response
