from django.shortcuts import render

def home(request):
    return render(request, 'calculation_2/home.html')


def perimeter(request):
    side_1 = request.GET.get('1_side')
    side_2 = request.GET.get('2_side')
    side_3 = request.GET.get('3_side')
    return render(request, 'calculation_2/perimeter.html', {'one_side': side_1,
                                                            'two_side': side_2,
                                                            'three_side': side_3})


def square(request):
    return render(request, 'calculation_2/square.html')