from assopy.models import Order
from conference.models import Fare
from tests import factories
from prettyprinter import cpprint

def test_threshold_is_reached(db):
    fare = factories.FareFactory(threshold=1)

    assert Fare.objects.available().count() == 1
    assert Order.objects.count() == 0
    order = factories.OrderFactory(items=[(fare, {"qty": 1})])
    assert not order._complete
    assert Order.objects.count() == 1

    assert Fare.objects.available().count() == 0
