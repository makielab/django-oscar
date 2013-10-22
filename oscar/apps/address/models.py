from oscar.apps.address.abstract_models import (
    AbstractUserAddress, AbstractCountry)


class UserAddress(AbstractUserAddress):

    @property
    def city(self):
        return self.line4


class Country(AbstractCountry):
    pass
