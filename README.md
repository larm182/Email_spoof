# Email Spoofing 🚀  

✍️ **Autor:** Ing. Larm  
🏷️ **Tags:** Email Spoofing, Python, Seguridad, SMTP  

## 📖 Descripción  

Este script en Python permite realizar **email spoofing**, es decir, el envío de correos electrónicos con direcciones falsas en el campo "From". Esto es útil para pruebas de seguridad y análisis de vulnerabilidades en sistemas de correo.  

⚠️ **Nota:** Este script está diseñado **exclusivamente** para **fines educativos y pruebas de seguridad**. No debe utilizarse con propósitos malintencionados, ya que podría violar políticas de uso y normativas legales.  

## 🎯 Objetivo  

- Simular el envío de correos electrónicos suplantando la identidad del remitente.  
- Evaluar la seguridad de servidores SMTP y sistemas de detección de spoofing.  
- Aprender sobre encabezados SMTP y autenticación de correos.  

## ⚙️ Requisitos  

- Python 3.x  
- Un servidor SMTP (puedes usar **Mailtrap**, **SendGrid**, o un servidor propio)  
- Librerías requeridas (ver más abajo)  

## 🚀 Instalación  

1. Clona este repositorio:  
   git clone https://github.com/larm182/Email_spoof.git

2. Instalar
   cd email-spoofing
   pip install -r requirements.txt
   
3. Utilizar
   python Email_spoof.py

📢 Importante
🔹 Algunos servidores SMTP bloquean intentos de spoofing. Se recomienda usar servicios de pruebas como Mailtrap.
🔹 Implementa autenticación SPF, DKIM y DMARC en tus servidores para protegerte contra ataques de spoofing.

📧 ¡Explora el mundo del email spoofing de manera ética y responsable! 🔥

Ejemplo: 

![email_spoofing](https://github.com/user-attachments/assets/35efc191-6e67-4784-9b36-914388e54930)


