from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import HttpResponse
from wkhtmltopdf.views import PDFTemplateView
from wkhtmltopdf.views import PDFTemplateResponse
from .models import Post

def post_detail(request, post_id):
    post = Post.objects.get(pk=post_id)
    return render(request, 'myapp/post_detail.html', {'post': post})

def post_to_pdf(request, post_id):
    post = Post.objects.get(pk=post_id)
    context = {
        'post': post,
    }
    template = 'myapp/post_template.html'
    pdf_file = f'post_{post_id}.pdf'

    response = PDFTemplateResponse(request=request, template=template, filename=pdf_file, context=context)
    response['Content-Disposition'] = f'attachment; filename="{pdf_file}"'
    return response
