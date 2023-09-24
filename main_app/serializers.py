from rest_framework import serializers
from .models import Ads, Category, HashTag, AdsImage


class AdsImageSerializers(serializers.ModelSerializer):
    class Meta:
        model = AdsImage
        fields = 'id image'.split()


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'



class HashTagSerializers(serializers.ModelSerializer):
    class Meta:
        model = HashTag
        fields = '__all__'




class AdsSerializer(serializers.ModelSerializer):
    category = CategorySerializers()
    hash_tags = HashTagSerializers()
    category_name = serializers.SerializerMethodField()
    images = AdsImageSerializers(many=True)

    class Meta:
        model = Ads
        fields = 'id category category_name images hash_tag_name_list hash_tags title price created'.split()


    def get_category_name(self, ads):
        try:
            return  ads.category.name
        except:
            return None


