from rest_framework import serializers
from assessment.models import Assessment,AssessmentLink,AssessmentSkills


class AssessmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assessment
        fields = '__all__'

class AssessmentLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssessmentLink
        fields = '__all__'


class AssessmentSkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssessmentSkills
        fields = '__all__'