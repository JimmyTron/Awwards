# from rest_framework import serializers
# from .models import Project, Profile

# class ProjectSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Project
#         fields = '__all__'

# class ProfileSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Profile
#         fields='__all__'



from rest_framework import serializers
from .models import Profile,Project,categories,technologies

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields='__all__'

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields='__all__'

class categoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = categories
        fields='__all__'

class technologiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = technologies
        fields='__all__'

