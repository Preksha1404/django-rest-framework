from rest_framework import serializers
from .models import Student

# Model Serializer Class
# Validator
def start_with_a(value):
    if value[0].lower() != 'a':
        raise serializers.ValidationError("Name must start with 'A'")
    
class StudentSerializer(serializers.ModelSerializer):
    name = serializers.CharField(validators=[start_with_a])
    # name = serializers.CharField(read_only=True)
    class Meta:
        model = Student
        fields = '__all__'
        # read_only_fields = ['name', 'roll_number']
        # extra_kwargs = {
        #     'name': {'read_only': True},
        #     'roll_number': {'read_only': True}
        # }

    # Field-level validation for roll_number
    def validate_roll_number(self, value):
        if value >= 200:
            raise serializers.ValidationError("Seats are full")
        return value
    
    # Object-level validation
    def validate(self, data):
        name = data.get('name')
        city = data.get('city')
        if name.lower() == 'preksha' and city.lower() != 'ahmedabad':
            raise serializers.ValidationError("Preksha can only be from Ahmedabad")
        return data

# Serializer Class
# Validators
# def start_with_a(value):
#     if value[0].lower() != 'a':
#         raise serializers.ValidationError("Name must start with 'A'")

# class StudentSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(max_length=100, validators=[start_with_a])
#     roll_number = serializers.IntegerField()
#     age = serializers.IntegerField()
#     city = serializers.CharField(max_length=100)

#     def create(self, validated_data):
#         return Student.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.roll_number = validated_data.get('roll_number', instance.roll_number)
#         instance.age = validated_data.get('age', instance.age)
#         instance.city = validated_data.get('city', instance.city)
#         instance.save()
#         return instance

#     # Field-level validation for roll_number
#     def validate_roll_number(self, value):
#         if value >= 200:
#             raise serializers.ValidationError("Seats are full")
#         return value

#     # Object-level validation
#     def validate(self, data):
#         name = data.get('name')
#         city = data.get('city')
#         if name.lower() == 'preksha' and city.lower() != 'ahmedabad':
#             raise serializers.ValidationError("Preksha can only be from Ahmedabad")
#         return data