from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test

# Check if the user is an Admin
def is_admin(user):
    return user.userprofile.role == 'Admin'

# Check if the user is a Librarian
def is_librarian(user):
    return user.userprofile.role == 'Librarian'

# Check if the user is a Member
def is_member(user):
    return user.userprofile.role == 'Member'

# Admin view - Only accessible by users with Admin role
@login_required
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

# Librarian view - Only accessible by users with Librarian role
@login_required
@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

# Member view - Only accessible by users with Member role
@login_required
@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')

