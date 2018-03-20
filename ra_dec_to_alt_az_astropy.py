#sudo pip install --no-deps astropy

#things I need
#anita lon, lat, alt, grb_time, grb_date, grb_ra, grb_dec

from astropy.coordinates import EarthLocation, SkyCoord, AltAz
from astropy.time import Time
from astropy import units as u
from astropy.coordinates import AltAz
import numpy as np
import pandas as pd

def main():

  grb_list = pd.read_csv('/Users/oindreebanerjee/python/A3_GRB_List_For_Astropy.csv')

  print grb_list

  #print grb_list.loc[: , "GRB_RA"][4]

  #print grb_list.shape

  for i in range(0,grb_list.shape[0]):
    #print grb_list.loc[: , "GRB_RA"][i]
    Anita_location = EarthLocation(lon = grb_list.loc[: , "ANITA_Longitude_Begin"][i], lat = grb_list.loc[: , "ANITA_Latitude_Begin"][i], height = grb_list.loc[: , "ANITA_Altitude_Begin"][i] * u.m)

    #print Anita_location

    time_string = grb_list.loc[: , "Date"][i] + " " + grb_list.loc[: , "Time"][i]
    #print time_string

    grb_time = Time(time_string)
    #print grb_time

    Anita_frame = AltAz(location = Anita_location, obstime = grb_time)

    coord = SkyCoord(grb_list.loc[: , "GRB_RA"][i] * u.degree, grb_list.loc[: , "GRB_Dec"][i] * u.degree)

    coordAnita = coord.transform_to(Anita_frame)

    print "Azimuth: ", coordAnita.az.degree, " Altitude: ", coordAnita.alt.degree

main()
