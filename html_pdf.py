

from weasyprint import HTML, CSS
from django.template.loader import get_template
from django.http import HttpResponse

def pdf_generation(request):
	Html_template = get_template("reume_page.html")
	pdf_file - HTML(string-html_template).write_pdf()
	response = HttpResponse(pdf_file, content_type="application/pdf")
	response["Content_Disposition"] = filename=”home_page.pdf"
	return response
