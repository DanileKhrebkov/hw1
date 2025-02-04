class NotificationHandler:
    def __init__(self):
        self.callbacks = {}

    def register_notif_type(self, notification_type, callback):

        self.callbacks[notification_type] = callback

    def send_notif(self, notification_type, message):

        if notification_type in self.callbacks:
            self.callbacks[notification_type](message)
        else:
            print(f"Тип уведомления '{notification_type}' не зарегистрирован.")


def email_notification(message):
    print(f"Отправка email уведомления: {message}")

def sms_notification(message):
    print(f"Отправка SMS уведомления: {message}")


handler = NotificationHandler()
handler.register_notif_type('email', email_notification)
handler.register_notif_type('sms', sms_notification)

handler.send_notif('email', 'Ваш заказ успешно оформлен.')
handler.send_notif('sms', 'Ваш заказ будет доставлен завтра.')