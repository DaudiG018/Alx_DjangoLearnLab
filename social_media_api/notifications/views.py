from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from notifications.models import Notification

@login_required
def user_notifications(request):
    notifications = Notification.objects.filter(recipient=request.user).order_by('-timestamp')
    unread_notifications = notifications.filter(read=False)
    for notification in unread_notifications:
        notification.read = True
        notification.save()
    return render(request, 'notifications/notifications_list.html', {'notifications': notifications})
