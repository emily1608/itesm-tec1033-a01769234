from AirportDP import Pilot
class AirportAD:
    def read_pilots_file(self):
        pilots_file(data/pilots.csv, "r")
        lines = pilots_file.readlines()
        lines.pop(0)

        pilots = {}
        for line in lines:
            fields = line.split(",")
            passport = fields[0]
            forname = fields[1]
            surname = fields[2]
            date_of_birth = fields[3]
            country = fields[4]
            gender = fields[5]
            marital_status = fields[6]

            _pilot = Pilot(passport, forname, surname, date_of_birth, country, gender, marital_status)

            pilots[passport] = pilot
            return pilots