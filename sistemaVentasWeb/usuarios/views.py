from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from main.models import User
from django.urls import reverse_lazy
# Import for print
from django.http import FileResponse
import io
from reportlab.platypus import Paragraph,Image
from reportlab.lib.enums import TA_CENTER
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import A4
from reportlab.platypus.tables import Table,TableStyle
from datetime import datetime
# Create your views here.

class usuarios_View(ListView):
    template_name='usuarios/usuarios.html'
    model = User
    

class create_user_view(CreateView):
    template_name='usuarios/form-user.html'
    fields = ['first_name','last_name','email','password','role']
    model = User
    
    
class update_user_view(UpdateView):
    template_name='usuarios/form-user.html'
    fields = ['first_name','last_name','email','password','role']
    model = User
    success_url=reverse_lazy('usuarios')
    
    
class delete_user_view(DeleteView):
    model = User
    
def print_pdf_button(request):
    # Create Bytestream buffer
    buf = io.BytesIO()
    # Create a canvas
    c = canvas.Canvas(buf,pagesize=A4)
    # Create a Text object
    #textob = c.beginText()
    #textob.setTextOrigin(inch,inch)
    #textob.setFont("Helvetica",14)
    
    #HEADER
    c.setLineWidth(.3)
    c.setFont('Helvetica',22)
    c.drawString(30,750,'Usuarios')
    c.setFont('Helvetica',12)
    c.drawString(30,735,'Reporte')
    
    today = datetime.now()
    date_now = today.strftime("%d/%m/%Y")
    
    c.setFont('Helvetica-Bold',12)
    c.drawString(480,750,f"Fecha: {date_now}")
    c.line(460,747,560,747)
    
    # GET DATE FROM DATABASE
    users_list = User.objects.all()

    # TABLE HEADER
    styles = getSampleStyleSheet()
    styleBH = styles['Normal']
    styleBH.alignment = TA_CENTER
    styleBH.fontsize = 10
    
    Id = Paragraph('''ID''',styleBH)
    nombre = Paragraph('''Nombre''',styleBH)
    apellido = Paragraph('''Apellido''',styleBH)
    email = Paragraph('''Email''',styleBH)
    rol = Paragraph('''Rol''',styleBH)
    
    data = []
    
    data.append([Id,nombre,apellido,email,rol])

    # Table
    styleN = styles['BodyText']
    styleN.alignment = TA_CENTER
    styleN.fontsize = 7
    
    high = 650
    for user in users_list:
        this_user = [user.id,user.nombre,user.apellido,user.email,user.rol]
        data.append(this_user)
        high=high-18
        
    # Table size
    width,height = A4
    table = Table(data)
    table.setStyle(TableStyle([
        ('INNERGRID',(0,0),(1,1))
    ]))
    
    # Add some lines of text
    #lines = [
    #    "Reporte de Usuarios",
    #    f"Fecha: {date_now}",
    #    "This is the line 3"
    #]
    # loop
    #for line in lines:    
    #    textob.textLine(line)
        
    # FInish up
    #c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)
    
    # Return something
    return FileResponse(buf, as_attachment=True,filename="usuarios.pdf")