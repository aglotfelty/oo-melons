"""This file should have our order classes in it."""

class AbstractMelonOrder(object):
    """A base melon order."""

    def __init__(self, species, qty):
        """Initialize melon order attributes"""

        self.species = species
        self.qty = qty
        self.shipped = False

    def get_total(self):
        """Calculate price."""
        base_price = 5
        if self.species == "Christmas melons":
            base_price *= 1.5

        total = (1 + self.tax) * self.qty * base_price

        return total

    def mark_shipped(self):
        """Set shipped to true."""

        self.shipped = True



class DomesticMelonOrder(AbstractMelonOrder):
    """A domestic (in the US) melon order."""

    order_type = "domestic"
    tax = 0.08

    
class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""
    
    order_type = "international"
    tax = 0.17

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes"""

        super(InternationalMelonOrder, self).__init__(species, qty)
        self.country_code = country_code

    def get_country_code(self):
        """Return the country code."""

        return self.country_code

    def get_total(self):
        """Calculate melon order total"""

        if self.qty < 10:
            return super(InternationalMelonOrder, self).get_total() + 3
        else:
            return super(InternationalMelonOrder, self).get_total()

class GovernmentMelonOrder(AbstractMelonOrder):
    """A government melon order"""

    tax = 0
    pass_inspection = False

    def mark_inspection(self, pass_inspection):
        """Marks inspection as passed"""

        self.pass_inspection = pass_inspection
