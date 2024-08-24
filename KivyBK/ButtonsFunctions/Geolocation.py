from jnius import autoclass
from android.permissions import request_permissions, Permission
from SendServer import send_location


def get_location():
    request_permissions([Permission.ACCESS_COARSE_LOCATION, Permission.ACCESS_FINE_LOCATION], start_gps)


def start_gps(request_code, grants):
    if all(grants):
        getting_location()
    else:
        print("Доступ отклонен")


def getting_location():
    LocationManager = autoclass('android.location.LocationManager')
    Context = autoclass('android.content.Context')
    PythonActivity = autoclass('org.kivy.android.PythonActivity')
    location_manager = PythonActivity.mActivity.getSystemService(Context.LOCATION_SERVICE)

    location = None

    if location_manager.isProviderEnabled(LocationManager.GPS_PROVIDER):
        location = location_manager.getLastKnownLocation(LocationManager.GPS_PROVIDER)
        if location:
            latitude = location.getLatitude()
            longitude = location.getLongitude()
            print(f"Долгота: {latitude}, Широта: {longitude} (GPS_PROVIDER)")
            send_location(location.getLatitude(), location.getLongitude())
        else:
            print("GPS_PROVIDER не сработал")
    else:
        print("GPS выключен")
        Intent = autoclass('android.content.Intent')
        Settings = autoclass('android.provider.Settings')
        PythonActivity.mActivity.startActivity(Intent(Settings.ACTION_LOCATION_SOURCE_SETTINGS))

    if location is None and location_manager.isProviderEnabled(LocationManager.NETWORK_PROVIDER):
        location = location_manager.getLastKnownLocation(LocationManager.NETWORK_PROVIDER)
        if location:
            latitude = location.getLatitude()
            longitude = location.getLongitude()
            print(f"Latitude: {latitude}, Longitude: {longitude} (NETWORK_PROVIDER)")
            send_location(location.getLatitude(), location.getLongitude())
        else:
            print("NETWORK_PROVIDER не сработал")
    else:
        print("Не удалось получить гео")
