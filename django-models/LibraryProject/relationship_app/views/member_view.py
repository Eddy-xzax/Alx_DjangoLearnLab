from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test

# Helper function to check if user is a Member
def is_member(user):
    return user.is_authenticated and user.userprofile.role == 'Member'

@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_page.html')
