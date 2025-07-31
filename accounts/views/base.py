from rest_framework.views import APIView
from rest_framework.exceptions import APIException
from companies.models import Enterprise, Employee
from accounts.models import User_Groups, Group_Permissions

class Base(APIView):
    def get_enterprise_user(self, user_id):
        enterprise = {
            "is_owner": False,
            "permission": []
        }

        enterprise["is_owner"] = Enterprise.objects.filter(user_id=user_id).exists()

        if enterprise["is_owner"]:
            return enterprise
        
        # Permissions, Get Employee
        employee = Employee.objects.filter(user_id=user_id).first()

        if not employee:
            raise APIException("Este usuario não é um funcionario")
        
        groups = User_Groups.objects.filter(user_id-user_id).all()

        for group in groups:
            group = group.group

            permissions = Group_Permissions.objects.filter(group_id=group.id).all()

            for p in permissions:
                enterprise['permission'].append({
                    "id": p.permission.id,
                    "label": p.permissions.name,
                    "codename": p.permission.codename
                })
            
        return enterprise