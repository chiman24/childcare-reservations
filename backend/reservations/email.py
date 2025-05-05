from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings

def send_reservation_email(reservation):
    subject = "Childcare Reservation Confirmation"
    from_email = settings.DEFAULT_FROM_EMAIL
    to = [reservation.email]

    context = {
        "parent_name": reservation.parent_name,
        "rehearsal_date": reservation.rehearsal_date,
        "num_children": reservation.num_children,
        "child_ages": reservation.child_ages,
    }

    text_content = render_to_string("emails/reservation_confirmation.txt", context)
    html_content = render_to_string("emails/reservation_confirmation.html", context)

    msg = EmailMultiAlternatives(subject, text_content, from_email, to)
    msg.attach_alternative(html_content, "text/html")
    msg.send()