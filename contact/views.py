from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail
from about.models import Biography


# Create your views here.
def contact_index(request):
    bio = Biography.objects.first()

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        if email and subject and message:
            full_message = f"""
                        Received message below from {name}, {email}, {subject}
                        ________________________


                        {message}
                        """
            send_mail(
                subject="Received contact form submission",
                message=full_message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.NOTIFY_EMAIL],
            )
    context = {
        'result': "Email sent successfully",
        'bio': bio
    }

    return render(request, "contact/contact_index.html", context)
