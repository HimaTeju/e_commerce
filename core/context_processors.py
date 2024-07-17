from django.contrib.auth.models import User

def common_data(request):
    return {
        'user': request.user,
        # Add other common data here
    }
