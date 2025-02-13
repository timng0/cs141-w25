from datetime import datetime

class DivvyStation:
    """
    Represents a Divvy station
    """
    def __init__(self, station_id, name, docks, lat, lon):
        """
        Constructor 
        
        Input:
            station_id (int): unique identifier for the station
            name (str): friendly name for station
            docks (int): number of docks at station
            lat (float): latitude of station
            lon (float): longitude of station
        """
        self.station_id = station_id
        self.name = name
        self.docks = docks
        self.lat = lat
        self.lon = lon

    def __repr__(self):
        """
        Internal string representation for DivvyStation
        """
        return (f"<DivvyStation: station_id={self.station_id},"
                f" name = '{self.name}'>")

    def __str__(self):
        """
        String representation for DivvyStation
        """
        return f"Divvy Station #{self.station_id} ({self.name})"


class DivvyTrip:
    """
    Represents a Divvy trip.
    """
    def __init__(self, trip_id, starttime, stoptime, bikeid, 
                 tripduration, from_station, to_station, usertype): 
        """
        Constructor

        Input:
            trip_id (int): unique identifier for trip
            starttime (datetime): timestamp for start of trip
            stoptime (datetime): timestamp for end of trip
            bikeid (int): identifier for bike used
            tripduration (int): duration of trip, in 
            from_station (DivvyStation): 
            to_station (DivvyStation): 
            usertype (str): whether the user is a one-off or subscriber
        """
        self.trip_id = trip_id
        self.starttime = starttime
        self.stoptime = stoptime
        self.bike_id = bikeid
        self.tripduration = tripduration
        self.from_station = from_station
        self.to_station = to_station
        self.usertype = usertype

    def __repr__(self):
        """
        Internal string representation for DivvyTrip
        """
        return (f"<DivvyTrip: trip_id={self.trip_id},"
                f" from_station={self.from_station.station_id}",
                f" to_station={self.to_station.station_id}>")

    def __str__(self):
        """
        String representation for DivvyTrip
        """
        return (f"Divvy Trip #{self.trip_id}"
                f" from {self.from_station.name}"
                f" to {self.to_station.name}")

                 

