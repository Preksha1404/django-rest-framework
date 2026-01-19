# Set different user rate limits for different classes
from rest_framework.throttling import UserRateThrottle

class DemoUserRateThrottle(UserRateThrottle):
    scope = 'demouser'