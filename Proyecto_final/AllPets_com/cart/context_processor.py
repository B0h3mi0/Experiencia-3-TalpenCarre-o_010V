def precio_total(request):
    total = 0 
    if request.user.is_authenticated:

        if 'carrito' in request.session.keys():
            for key,value in request.session['carrito'].items():
                total = total +(float(value['precio'])*value['cantidad'])

    return {'precio_total':total}








