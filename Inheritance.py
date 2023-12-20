class Airline:
    def length(self):
        print("All planes are at least 5 meters long")

    def engine(self):
        print("The engine of most planes are powered by a Rolls Royce engine")

class Etihad(Airline):
    def service(self):
        print("""This airline (Arguably) has the best first class suite and service(s)
And also cool amenity kits in nice color
    """)


etihad1 = Etihad()
etihad1.service()
etihad1.engine()
etihad1.length()