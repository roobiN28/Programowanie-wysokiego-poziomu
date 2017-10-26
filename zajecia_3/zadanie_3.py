class Car(object):
    brand = None
    gasTankCapability = 100
    maxSpeed = 180
    fuelConsumption = 7

    def __init__(self):
        self.brand = ''

    def drive(self, speed, distance):
        print 'Predkosc samochodu wynosi: ' + str(self.speed(speed)) + 'km/h'
        print 'Czas podrozy: ' + str(self.travelTime(self.speed(speed), distance)) + ' godzin'
        fuelConsumptionOnTravel = (distance / 100) * self.calculateFuelConsumption(speed)
        print 'Samochod zuzyje ' + str(fuelConsumptionOnTravel) + 'l podczas podrozy'
        print 'Trzeba tankowac ' + str(fuelConsumptionOnTravel / (self.gasTankCapability * 1.0)) + ' razy'

    def speed(self, speed):
        if speed > self.maxSpeed:
            return self.maxSpeed
        else:
            return speed

    def travelTime(self, speed, distance):
        return distance / (speed * 1.0)

    def calculateFuelConsumption(self, speed):
        if speed / self.maxSpeed < 30 or speed / self.maxSpeed > 80:
            return self.getFuelConsumption() + self.getFuelConsumption() * 0.2
        else:
            return self.getFuelConsumption()

    def getFuelConsumption(self):
        return self.fuelConsumption


class Cabriolet(Car):
    openRoof = False

    def closeRoof(self):
        self.openRoof = False

    def openRoof(self):
        self.openRoof = True

    def getFuelConsumption(self):
        if self.openRoof == True:
            return self.fuelConsumption + self.fuelConsumption * 0.15
        else:
            return self.fuelConsumption


car = Car()
car.drive(100, 200)
cabriolet = Cabriolet()
cabriolet.openRoof()
cabriolet.drive(100, 200)
