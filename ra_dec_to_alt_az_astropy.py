#sudo pip install --no-deps astropy
#need to make changes to implement for anita

from astropy.coordinates import EarthLocation, SkyCoord, AltAz
from astropy.time import Time
from astropy import units as u
from astropy.coordinates import AltAz

def main():

#Figure out ANITA longitude, latitude, altitude at the begin time of the GRB
	Anita_location = EarthLocation(lon='-109.70392',lat='-89.8105588',height=2649.85*u.m)

#GRB time
	time = Time('2013-01-04 17:18:07')

#Telling it the frame
	Anita_frame = AltAz(location=Anita_location, obstime=time)

#getting the coordinates
	coord = SkyCoord(ra = 174.09 * u.degree, dec = 25.92 * u.degree)

#getting the coordinates in the Anita frame
	coordAnita = coord.transform_to(Anita_frame)

	print coordAnita

main()
