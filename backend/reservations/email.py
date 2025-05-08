from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings

def send_reservation_email(reservation):
    subject = "Childcare Reservation Confirmation"
    from_email = settings.DEFAULT_FROM_EMAIL
    to = [reservation.email]

    special_notes = reservation.special_notes if reservation.special_notes else "No special notes provided."

    context = {
        "parent_name": reservation.parent_name,
        "rehearsal_date": reservation.rehearsal_date,
        "num_children": reservation.num_children,
        "child_ages": reservation.child_ages,
        "special_notes": special_notes
    }

    text_content = render_to_string("emails/reservation_confirmation.txt", context)
    html_content = render_to_string("emails/reservation_confirmation.html", context)

    msg = EmailMultiAlternatives(subject, text_content, from_email, to)
    msg.attach_alternative(html_content, "text/html")
    msg.send()