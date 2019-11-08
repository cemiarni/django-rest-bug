from django.db import models


class IP(models.Model):
    ipv4 = models.GenericIPAddressField(protocol="ipv4")
    ipv6 = models.GenericIPAddressField(protocol="ipv6")
    both = models.GenericIPAddressField()
