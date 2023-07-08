import base64
import qrcode
from io import BytesIO
from django.shortcuts import render
from django.http import JsonResponse
import cx_Oracle

def QrView(request):


    return render(request, 'QrModule/QrRegeneration.html')

def WithIndentView(request):
    error_message = None
    connection = cx_Oracle.connect(
        user="medilogics",
        password="sapyas210",
        dsn="192.168.1.46:1521/uattest"
    )

    if request.method == 'POST':
        get_indent_no = request.POST.get('indent_no')
        indent_no = get_indent_no.upper()

        if not indent_no.startswith('SR'):
            indent_no = 'SR' + indent_no

        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT GETSERVICENAME(A.INV_MAST_SERVICE_ID) ITEM,A.REQUESTED_QTY,A.REQUESTED_QTY_UNIT_NAME UNIT,GET_PH_SUBLOCATION_BY_ID(B.REQUEST_FROM) REQUESTING_LOCATION,GET_PH_SUBLOCATION_BY_ID(B.REQUEST_TO) RECEVING_LOCATION,B.REQUEST_NO FROM PH_DTLS_STOCK_REQUEST A , PH_MAST_STOCK_REQUEST B WHERE A.PH_MAST_STOCK_REQUEST_ID=B.PH_MAST_STOCK_REQUEST_ID AND REQUEST_NO =:indent_no",
                {'indent_no': indent_no})
            result = cursor.fetchall()


        if result:
            return render(request, 'QrModule/WithIndent.html', {'result': result})

        else:
            error_message = 'Please check the provided Indent number'

    return render(request, 'QrModule/WithIndent.html', {'error_message':error_message})