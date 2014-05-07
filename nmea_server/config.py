#!/usr/bin/env python2.6
# -*- coding: utf-8 -*-

from helper_functions import *

test = False;

HTTP_HOST = '';
HTTP_PORT = 8082; # The port that the HTTP data will be output on

NMEA_HOST = '192.168.5.200';     # The host with the NMEA TCP feed
NMEA_PORT = 10110;              # The port with the NMEA TCP feed

watchFields = [NmeaWatchField(name="lat", sentence="RMC", fields=["latitude"],
                              formatFunction=formatLatitude),
               NmeaWatchField(name="lon", sentence="RMC", fields=["longitude"],
                              formatFunction=formatLongitude),
               NmeaWatchField(name="cog", sentence="RMC", fields=["true_course"],
                              formatFunction=formatAngle),
               NmeaWatchField(name="sog", sentence="RMC", fields=["spd_over_grnd"],
                              formatFunction=formatSog),
               NmeaWatchField(name="xte", sentence="APB", fields=["cross_track_err_mag"]),
               NmeaWatchField(name="xte_unit", sentence="APB", fields=["cross_track_unit"],
                              formatFunction=formatDistanceUnit),
               NmeaWatchField(name="dir_to_steer", sentence="APB", fields=["dir_steer"]),
               NmeaWatchField(name="heading_to_steer", sentence="APB", fields=["heading_to_dest"],
                              formatFunction=formatAngle),
               NmeaWatchField(name="heading_to_steer_type", sentence="APB", fields=["heading_to_dest_type"],
                              formatFunction=formatType),
               NmeaWatchField(name="waypoint", sentence="BWC", fields=["waypoint_name"]),
               NmeaWatchField(name="wpt_lat", sentence="BWC", fields=["lat_next"],
                              formatFunction=formatLat),
               NmeaWatchField(name="wpt_lat_dir", sentence="BWC", fields=["lat_next_direction"]),
               NmeaWatchField(name="wpt_lon", sentence="BWC", fields=["lon_next"],
                              formatFunction=formatLon),       
               NmeaWatchField(name="wpt_lon_dir", sentence="BWC", fields=["lon_next_direction"]),
               NmeaWatchField(name="dtw", sentence="BWC", fields=["range_next"]),
               NmeaWatchField(name="dtw_unit", sentence="BWC", fields=["range_unit"],
                              formatFunction=formatDistanceUnit),
               NmeaWatchField(name="btw", sentence="BWC", fields=["true_track"],
                              formatFunction=formatAngle),
               NmeaWatchField(name="depth", sentence="DPT", fields=["depth"],
                              formatFunction=formatDepth),
               NmeaWatchField(name="temp", sentence="MTW", fields=["temperature"]),
               NmeaWatchField(name="temp_unit", sentence="MTW", fields=["units"]),
               NmeaWatchField(name="boat_speed", sentence="VHW", fields=["water_speed_knots"],
                              formatFunction=formatSog),
               NmeaWatchField(name="heading", sentence="VHW", fields=["heading_true"],
                              formatFunction=formatAngle),
               NmeaWatchField(name="distance_total", sentence="VLW", fields=["trip_distance"],
                              formatFunction=formatDistanceNM),
               NmeaWatchField(name="distance_reset", sentence="VLW", fields=["trip_distance_reset"],
                              formatFunction=formatDistanceNM),
               NmeaWatchField(name="wind_angle", sentence="MWV", fields=["wind_angle"],
                              formatFunction=formatWindAngle),
               NmeaWatchField(name="wind_speed", sentence="MWV", fields=["wind_speed"])];
