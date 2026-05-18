from abc import abstractmethod


class Parrot:
    BASE_SPEED = 12.0

    @abstractmethod
    def speed(self):
        pass

    @abstractmethod
    def cry(self):
        pass

    def _base_speed(self):
        return self.BASE_SPEED


class EuropeanParrot(Parrot):
    def __init__(self):
        return

    def speed(self):
        return self._base_speed()

    def cry(self):
        return "Sqoork!"


class AfricanParrot(Parrot):
    LOAD_FACTOR = 9.0

    def __init__(self, number_of_coconuts):
        self._number_of_coconuts = number_of_coconuts

    def speed(self):
        calculated_speed = (
            self._base_speed() - self._load_factor() * self._number_of_coconuts
        )
        if calculated_speed < 0:
            return 0
        else:
            return calculated_speed

    def cry(self):
        return "Sqaark!"

    def _load_factor(self):
        return self.LOAD_FACTOR


class NorwegianBlueParrot(Parrot):
    def __init__(self, voltage, nailed):
        self._voltage = voltage
        self._nailed = nailed

    def speed(self):
        if self._nailed:
            return 0
        else:
            return self._compute_base_speed_for_voltage(self._voltage)

    def cry(self):
        return "Bzzzzzz" if self._voltage > 0 else "..."

    def _compute_base_speed_for_voltage(self, voltage):
        return min([24.0, voltage * self._base_speed()])
