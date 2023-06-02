from .forms import LoginForm, RegistrationFrom, EditAccountForm, EditProfileForm


def add_my_forms(request):
    return {
        'login_form': LoginForm(),
        'register_form': RegistrationFrom(),
        'edit_account': EditAccountForm(instance=request.user if request.user.is_authenticated else None),
        'edit_profile': EditProfileForm(),
    }
