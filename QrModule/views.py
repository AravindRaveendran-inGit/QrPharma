# from django.shortcuts import render
#
# # Create your views here.
#
#
# def QrView(request):
#     return render(request, 'QrModule/QrRegeneration.html')


import qrcode
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from barcode import *


@csrf_exempt
def qr_codeView(request):
    if request.method == 'POST':
        # Get the scanned QR code data from the request
        qr_code_data = request.POST['qr_code_data']

        # Generate a new QR code with the scanned data
        qr = qrcode.QRCode()
        qr.add_data(qr_code_data)
        qr.make(fit=True)
        qr_code_image = qr.make_image()

        # Render the HTML page with the original and new QR codes
        return render(request, 'qr_code.html', {
            'original_qr_code': qr_code_data,
            'new_qr_code_data': qr_code_data,
        })

    return render(request, 'QrModule/QrRegeneration.html')