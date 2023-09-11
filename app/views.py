from .models import Special, Testimonial
from .serializers import SpecialSerializer, TestimonialSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


#SPECIAL API ONLY
@api_view(['GET', 'POST'])
def special_list(request):
    if (request.method == 'GET'):
        specials = Special.objects.all()
        serializer = SpecialSerializer(specials, many=True)
        return Response(serializer.data)
    
    if (request.method == 'POST'):
        serializer = SpecialSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
@api_view(['GET', 'PUT', 'DELETE'])
def special_detail(request, id):
    try:
        special = Special.objects.get(pk=id)
    except Special.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if (request.method == 'GET'):
        serializer = SpecialSerializer(special)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif (request.method == 'PUT'):
        serializer = SpecialSerializer(special, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif (request.method == 'DELETE'):
        special.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#TESTIMONIAL API ONLY
@api_view(['GET', 'POST'])
def testimonial_list(request):
    if (request.method == 'GET'):
        testimonial = Testimonial.objects.all()
        serializer = TestimonialSerializer(testimonial, many=True)
        return Response(serializer.data)
    if (request.method == 'POST'):
        serializer = TestimonialSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def testimonial_detail(request, id):
    try:
        testimonial = Testimonial.objects.get(pk=id)
    except Testimonial.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if (request.method == 'GET'):
        serializer = TestimonialSerializer(testimonial)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif (request.method == 'PUT'):
        serializer = TestimonialSerializer(testimonial, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    elif (request.method == 'DELETE'):
        testimonial.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)