#!/usr/bin/python
#-*- coding: utf-8 -*-
#Autor: Luis Angel Ramirez Mendoza
#______________________________________________________________________________________________________________________

import smtplib
import csv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os
from tkinter import Tk, Label, Entry, Button, Text, filedialog, messagebox, Frame, font

# Función para crear el correo
def crear_correo(remitente, destinatario, asunto, cuerpo, archivo_adjunto=None):
    correo = MIMEMultipart()
    correo['From'] = remitente
    correo['To'] = destinatario
    correo['Subject'] = asunto
    correo.attach(MIMEText(cuerpo, 'html'))

    if archivo_adjunto:
        with open(archivo_adjunto, 'rb') as adjunto:
            parte = MIMEBase('application', 'octet-stream')
            parte.set_payload(adjunto.read())
            encoders.encode_base64(parte)
            parte.add_header(
                'Content-Disposition',
                f'attachment; filename={os.path.basename(archivo_adjunto)}'
            )
            correo.attach(parte)

    return correo

# Función para leer destinatarios desde un archivo CSV
def leer_destinatarios(archivo_csv):
    destinatarios = []
    with open(archivo_csv, 'r', newline='', encoding='utf-8') as archivo:
        lector = csv.reader(archivo)
        for fila in lector:
            if fila:  # Evitar líneas vacías
                destinatarios.append(fila[0])
    return destinatarios

# Función para enviar correos masivos
def enviar_correos_masivos():
    try:
        # Obtener los datos de la interfaz
        smtp_server = entry_smtp.get()
        smtp_port = int(entry_port.get())
        email_address = entry_correo.get()
        email_password = entry_password.get()
        asunto = entry_asunto.get()
        cuerpo = text_cuerpo.get("1.0", "end-1c")
        archivo_adjunto = label_adjunto.cget("text") if label_adjunto.cget("text") != "Ningún archivo seleccionado" else None

        # Obtener destinatarios
        destinatarios = []
        if entry_destinatario_manual.get():  # Si se ingresó un correo manualmente
            destinatarios.append(entry_destinatario_manual.get())
        if label_destinatarios.cget("text") != "Ningún archivo seleccionado":  # Si se cargó un archivo CSV
            destinatarios.extend(leer_destinatarios(label_destinatarios.cget("text")))

        if not destinatarios:
            messagebox.showerror("Error", "Debes ingresar al menos un destinatario o cargar un archivo CSV.")
            return

        # Conectar al servidor SMTP
        with smtplib.SMTP(smtp_server, smtp_port) as servidor:
            servidor.starttls()
            servidor.login(email_address, email_password)

            # Enviar correos
            for destinatario in destinatarios:
                correo = crear_correo(email_address, destinatario, asunto, cuerpo, archivo_adjunto)
                servidor.sendmail(email_address, destinatario, correo.as_string())
                print(f'Correo enviado a: {destinatario}')

        messagebox.showinfo("Éxito", "Todos los correos se enviaron correctamente.")

    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error: {e}")

# Función para seleccionar archivo de destinatarios
def seleccionar_destinatarios():
    archivo = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
    if archivo:
        label_destinatarios.config(text=archivo)

# Función para seleccionar archivo adjunto
def seleccionar_adjunto():
    archivo = filedialog.askopenfilename()
    if archivo:
        label_adjunto.config(text=archivo)

# Crear la ventana principal
ventana = Tk()
ventana.title("Herramienta de Envío Masivo de Correos")
ventana.geometry("600x550")
ventana.configure(bg="#f0f0f0")
ventana.iconbitmap('logo.ico')  

# Fuentes personalizadas
fuente_titulo = font.Font(family="Helvetica", size=14, weight="bold")
fuente_texto = font.Font(family="Helvetica", size=10)

# Marco para la configuración SMTP
frame_smtp = Frame(ventana, bg="#ffffff", bd=2, relief="solid")
frame_smtp.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

Label(frame_smtp, text="Configuración SMTP", font=fuente_titulo, bg="#ffffff").grid(row=0, column=0, columnspan=3, pady=5)

Label(frame_smtp, text="Servidor SMTP:", font=fuente_texto, bg="#ffffff").grid(row=1, column=0, padx=5, pady=5, sticky="w")
entry_smtp = Entry(frame_smtp, width=40, font=fuente_texto)
entry_smtp.grid(row=1, column=1, padx=5, pady=5)

Label(frame_smtp, text="Puerto SMTP:", font=fuente_texto, bg="#ffffff").grid(row=2, column=0, padx=5, pady=5, sticky="w")
entry_port = Entry(frame_smtp, width=40, font=fuente_texto)
entry_port.grid(row=2, column=1, padx=5, pady=5)

Label(frame_smtp, text="Correo Electrónico:", font=fuente_texto, bg="#ffffff").grid(row=3, column=0, padx=5, pady=5, sticky="w")
entry_correo = Entry(frame_smtp, width=40, font=fuente_texto)
entry_correo.grid(row=3, column=1, padx=5, pady=5)

Label(frame_smtp, text="Contraseña:", font=fuente_texto, bg="#ffffff").grid(row=4, column=0, padx=5, pady=5, sticky="w")
entry_password = Entry(frame_smtp, width=40, font=fuente_texto, show="*")
entry_password.grid(row=4, column=1, padx=5, pady=5)

# Marco para los destinatarios
frame_destinatarios = Frame(ventana, bg="#ffffff", bd=2, relief="solid")
frame_destinatarios.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

Label(frame_destinatarios, text="Destinatarios", font=fuente_titulo, bg="#ffffff").grid(row=0, column=0, columnspan=3, pady=5)

Label(frame_destinatarios, text="Correo Manual:", font=fuente_texto, bg="#ffffff").grid(row=1, column=0, padx=5, pady=5, sticky="w")
entry_destinatario_manual = Entry(frame_destinatarios, width=40, font=fuente_texto)
entry_destinatario_manual.grid(row=1, column=1, padx=5, pady=5)

Label(frame_destinatarios, text="Archivo CSV:", font=fuente_texto, bg="#ffffff").grid(row=2, column=0, padx=5, pady=5, sticky="w")
label_destinatarios = Label(frame_destinatarios, text="Ningún archivo seleccionado", fg="blue", bg="#ffffff", font=fuente_texto)
label_destinatarios.grid(row=2, column=1, padx=5, pady=5)
Button(frame_destinatarios, text="Seleccionar", command=seleccionar_destinatarios, font=fuente_texto).grid(row=2, column=2, padx=5, pady=5)

# Marco para el contenido del correo
frame_correo = Frame(ventana, bg="#ffffff", bd=2, relief="solid")
frame_correo.grid(row=2, column=0, padx=10, pady=10, sticky="ew")

Label(frame_correo, text="Contenido del Correo", font=fuente_titulo, bg="#ffffff").grid(row=0, column=0, columnspan=3, pady=5)

Label(frame_correo, text="Asunto:", font=fuente_texto, bg="#ffffff").grid(row=1, column=0, padx=5, pady=5, sticky="w")
entry_asunto = Entry(frame_correo, width=40, font=fuente_texto)
entry_asunto.grid(row=1, column=1, padx=5, pady=5)

Label(frame_correo, text="Cuerpo del Correo:", font=fuente_texto, bg="#ffffff").grid(row=2, column=0, padx=5, pady=5, sticky="w")
text_cuerpo = Text(frame_correo, width=40, height=5, font=fuente_texto)
text_cuerpo.grid(row=2, column=1, padx=5, pady=5)

Label(frame_correo, text="Archivo Adjunto:", font=fuente_texto, bg="#ffffff").grid(row=3, column=0, padx=5, pady=5, sticky="w")
label_adjunto = Label(frame_correo, text="Ningún archivo seleccionado", fg="blue", bg="#ffffff", font=fuente_texto)
label_adjunto.grid(row=3, column=1, padx=5, pady=5)
Button(frame_correo, text="Seleccionar", command=seleccionar_adjunto, font=fuente_texto).grid(row=3, column=2, padx=5, pady=5)

# Botón para enviar correos
Button(ventana, text="Enviar Correos", command=enviar_correos_masivos, font=fuente_titulo, bg="#4CAF50", fg="white").grid(row=3, column=0, padx=10, pady=20, sticky="ew")

# Ejecutar la ventana
ventana.mainloop()