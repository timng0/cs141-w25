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
                f" from_station={self.from_station.station_id},"
                f" to_station={self.to_station.station_id}>")

    def __str__(self):
        """
        String representation for DivvyTrip
        """
        return (f"Divvy Trip #{self.trip_id}"
                f" from {self.from_station.name}"
                f" to {self.to_station.name}")

                 





def station_dict_to_object(station_dicts):
    """
    Converts a list of Divvy station dictionaries into DivvyStations.

    Input:
        station_dicts (list[dict[str,Any]]): list of dictionaries

    Output (dict[int,DivvyStation]): dictionary mapping station IDs
        to DivvyStations
    """
    stations = {}
    for station in station_dicts:
        st_id = int(station['id'])
        name = station['name']
        docks = int(station['total_docks'])
        lat = float(station['latitude'])
        lon = float(station['longitude'])
        stations[st_id] = DivvyStation(st_id, name, docks, lat, lon)
    return stations




def trip_dict_to_object(trip_dicts, stations):
    """
    Converts a list of Divvy trip dictionaries into DivvyTrips.

    Input:
        trip_dicts (list[dict[str,Any]]): list of dictionaries

    Output (list[DivvyTrip]): list of DivvyTrips
    """
    trips = []
    for trip in trip_dicts:
        trip_id = int(trip['trip_id'])
        start = datetime.strptime(trip['starttime'], '%m/%d/%Y %I:%M:%S %p')
        stop = datetime.strptime(trip['stoptime'], '%m/%d/%Y %I:%M:%S %p')
        bike_id = int(trip['bikeid'])
        duration = int(trip['tripduration'])
        from_station = int(trip['from_station_id'])
        to_station = int(trip['to_station_id'])
        user = trip['usertype']
        trips.append(DivvyTrip(trip_id, start, stop, bike_id, duration, stations[from_station], stations[to_station], user))
    return trips



class Location:
    """
    Represents a geographic location
    """

    def __init__(self, latitude, longitude):
        """
        Constructor

        Inputs:
        - latitude, longitude [float]: The coordinates for
          this location.
        """
        self.latitude = latitude
        self.longitude = longitude


    def __str__(self):
        """
        Human-friendly string representation of Location
        """
        lat = 'S' if (self.latitude < 0.0) else 'N'
        lon = 'W' if (self.longitude < 0.0) else 'E'
        return (f"({self.latitude:.3f} {lat},"
                f" {self.longitude:.3f} {lon})")

    def __repr__(self):
        """
        Internal string representation of Location.
        """
        return f"Location({self.latitude}, {self.longitude})"

    def distance_to(self, other):
        """
        Computes the distance to another location using the
        Haversine Formula

        Inputs:
        - other: [Location object] Another location

        Returns [float]: the distance to the other location
        """
        # print("self: ", self)
        # print("other:", other)
        diffLatitude = math.radians(other.latitude - self.latitude)
        diffLongitude = math.radians(other.longitude - self.longitude)

        a = math.sin(diffLatitude/2) * math.sin(diffLatitude/2) + \
            math.cos(math.radians(self.latitude)) * \
            math.cos(math.radians(other.latitude)) * \
            math.sin(diffLongitude/2) * math.sin(diffLongitude/2)
        d = 2 * math.asin(math.sqrt(a))

        return 6371000.0 * d