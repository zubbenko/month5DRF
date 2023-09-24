from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Ads
from .serializers import AdsSerializer


@api_view(['GET', 'POST'])
def ads_list_api_view(request):
    if request.method == 'GET':
        """  Получить List of objects = QuerySet """
        ads_list = Ads.objects.all()

        """  Reformat (Serialize) list of object to JSONE """
        ads_jsone = AdsSerializer(instance=ads_list, many=True).data

        """  Return list of objects """
        return Response(data=ads_jsone)
    elif request.method == 'POST':
        print(request.data)
        print(request.data.get('text'))
        print(request.data.get('int'))
        return Response()



@api_view(['GET'])
def ads_detail_api_view(request, id):
    """Check object"""
    try:

        """Get ads item"""
        item = Ads.objects.get(id=id)
    except Ads.DoesNotExist:
        return Response(data={'error': 'Site not found'},
                        status=status.HTTP_404_NOT_FOUND)

        """Ads item serialize to dict"""
        ads_jsone = AdsSerializer(instance=item).data

        """Return dict by JSONE file"""
        return Response(data=ads_jsone)





@api_view(['GET'])
def test_api_view(request):
    """Logic"""
    data_dict = {
        'taxt': 'yo man',
        'int': 999,
        'float': 999.99,
        'bool': True,
        'list': [1,2,3],
        'dict': {'key': 'value'}

    }

    return Response(data=data_dict, status=status.HTTP_200_OK)