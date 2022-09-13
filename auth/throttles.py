from rest_framework import throttling


class LoginThrottle(throttling.AnonRateThrottle):
    scope = 'login'

class PortalThrottle(throttling.UserRateThrottle):
    scope = 'portal'

class SendEmailThrottle(throttling.AnonRateThrottle):
    scope = 'sendemail'