from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
@api_view(['POST'])
def post(request):
       nums = eval(request.body.decode('utf-8'))
       sum=str(nums["operator"])
       if sum == "+" :
              num1 = int(nums["number_1"])
              num2 = int(nums["number_2"])
              return Response(str(num1 + num2))
       if sum == "-" :
              num1 = int(nums["number_1"])
              num2 = int(nums["number_2"])
              return Response(str(num1 - num2))
       if sum == "x" :
              num1 = int(nums["number_1"])
              num2 = int(nums["number_2"])
              return Response(str(num1 * num2))
       if sum == "/" :
              num1 = int(nums["number_1"])
              num2 = int(nums["number_2"])
              return Response(int(num1 / num2))
       else:
              return Response('number not allow')