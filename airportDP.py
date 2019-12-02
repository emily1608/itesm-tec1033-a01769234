class Airport:
	#Constructor
	def __init__(self):

		#None, por defecto, hasta que se cambie, de asi desearlo
		self.attendants = None
		self.flights = None
		self.passengers = None
		self.pilots = None
		self.planes = None
		self.travellers = None

    def populate_airport():
		#Cargador de datos
		data_loader = AirportAD
		#Datos asignados a sus componenetes
		self.attendants = data.loader.read_attendants_file()
		self.flights = data.loader.read_flights_file()
		self.passengers = data.loader.read_passengers_file()
		self.pilots = data.loader.read_pilots_file()
		self.planes = data.loader.read_planes_file()
		self.travellers = data.loader.read_travellers_file()
#Clase nueva
class Attendant:
	def __init__(self, _passport, _forename, _surname, _date_of_birth, _country, _gender, _marital_status):

		self.passport = _passport
		self.forename = _forename
		self.surname = _surname
		self.date_of_birth = _date_of_birth
		self.country = _country
		self.gender = _gender
		self.marital_status = _marital_status
#Clase nueva
class Flight:
	def __init__(self, _idenfical, _plate, _origin, _destiny, _departure, _arriving, _status, _departureGate, _takeOFFtrack, _arrivingGate, _landingTrack, _pilot, _copilot, _attendants):

		self.identifical = _identifical
		self.plate = _plate
		self.origin = _origin
		self.destiny = _destiny
		self.departure = _departure
		self.arriving = _arriving
		self.status = _status
		self.departureGate = _departureGate
		self.takeOFFtrack = _takeOFFtrack
		self.arrivingGate = _arrivingGate
		self.landingTrack = _landingTrack
		self.pilot = _pilot
		self.copilot = _copilot
		self.attendants = _attendants
