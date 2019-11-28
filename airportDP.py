class Airport:
    def __init__(self):
        self.traks = None
        self.airplanes = None
        self.passengers = None
        self.pilots = None
        self.attendants = None
        self.travellers = None

    def populate_airport(self):
        data_loader = AirportAD()
        self.travellers = data_loader.read_pilots_file()


class pilot:
    def __init__(self, _passport, _forname, _surname, _date_of_birth, _country, _gender, _marital_status):
      self._passport= _passport
      self.forname=_forname
      self.surname=_surname
      self.date_of_birth=_date_of_birth
      self.coutry=_country
      self.gender=_gender
      self.marital_status=_marital_status
        