from android.permissions import request_permissions, Permission
from ButtonsFunctions.Geolocation import getting_location
import threading


def geo_live():
    request_permissions([Permission.ACCESS_COARSE_LOCATION, Permission.ACCESS_FINE_LOCATION], start_gps)


def start_gps(request_code, grants):
    if all(grants):
        getting_location()
        threading.Timer(30, getting_location).start()
    else:
        print("Доступ отклонен")
