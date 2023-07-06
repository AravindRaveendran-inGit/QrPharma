import base64
import qrcode
from io import BytesIO
from django.shortcuts import render
from django.http import JsonResponse

def QrView(request):
    return render(request, 'QrModule/QrRegeneration.html')

# def generate_qr_image(request):
#     data = request.POST.get('data')
#     if data:
#         # Generate QR code image
#         qr = qrcode.QRCode()
#         qr.add_data(data)
#         qr.make(fit=True)
#         qr_image = qr.make_image(fill_color="black", back_color="white")
#
#         # Convert QR code image to base64
#         buffer = BytesIO()
#         qr_image.save(buffer, format='PNG')
#         qr_image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
#
#         return JsonResponse({'qr_image_base64': qr_image_base64})
#
#     return JsonResponse({'error': 'No data provided'})