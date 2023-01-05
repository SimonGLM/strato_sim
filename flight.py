import datetime as dt
# import numpy as np
import astra

LAUNCHDATETIME=dt.datetime(2022,11,19,10,0,0)
LAUNCHLATITUDE=50.56862148136799
LAUNCHLONGITUDE=8.673392561502094
LAUNCHELEVATION=160
FLIGHTNUMBER=1
GROSSWEIGHT=1.8
NOZZLELIFT=2 #kg
TIMEVECTOR=[dt.datetime.fromtimestamp(1668852000+h) for h in range(14400)]

NSIMS=100
OUTPUTFILE="flight.csv"
WEATHERMODEL=astra.weather.forecastEnvironment(LAUNCHLATITUDE,LAUNCHLONGITUDE,LAUNCHELEVATION,LAUNCHDATETIME,inflationTemperature=0,load_on_init=True)
# PARACHUTEMODEL

theFlight=astra.simulator.flight('Helium', 'HW1600', NOZZLELIFT, GROSSWEIGHT, environment=WEATHERMODEL, outputFile=OUTPUTFILE)

theFlight.run()
# astra.simulator.flightProfile(,2, 1, timeVector, latitudeProfile, longitudeProfile, altitudeProfile, highestAltIndex, highestAltitude, hasBurst, balloonModel)
