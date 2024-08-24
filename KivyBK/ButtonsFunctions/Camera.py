import os
from android.permissions import request_permissions, Permission
from jnius import autoclass, cast
from android import activity


def take_picture():
    def on_permissions_result(permissions, grantResults):
        if all(grantResults):
            proceed_with_camera()
        else:
            print("Разрешение не предоставлено")

    request_permissions([Permission.CAMERA, Permission.WRITE_EXTERNAL_STORAGE], on_permissions_result)


def proceed_with_camera():
    PythonActivity = autoclass('org.kivy.android.PythonActivity')
    Intent = autoclass('android.content.Intent')
    File = autoclass('java.io.File')
    Uri = autoclass('android.net.Uri')
    FileProvider = autoclass('androidx.core.content.FileProvider')
    Environment = autoclass('android.os.Environment')

    pictures_dir = File(Environment.getExternalStoragePublicDirectory(Environment.DIRECTORY_PICTURES), "MyAppPhotos")
    if not pictures_dir.exists():
        pictures_dir.mkdirs()

    photo_file = File(pictures_dir, "photo.jpg")
    photo_uri = FileProvider.getUriForFile(PythonActivity.mActivity, 'org.test.myapp.fileprovider', photo_file)

    intent = Intent(Intent.ACTION_IMAGE_CAPTURE)
    intent.putExtra(Intent.EXTRA_OUTPUT, photo_uri)

    activity.bind(lambda req, res, data: on_activity_result(res, photo_file.getAbsolutePath()))
    PythonActivity.mActivity.startActivityForResult(intent, 0)


def on_activity_result(result_code, photo_path):
    if result_code == -1:
        print("Фото сохранено")
        try:
            with open(photo_path, 'rb') as photo_file:
                photo_data = photo_file.read()
                # Здесь должен был быть вызов функции отправки фото на сервер
        except Exception as e:
            print(f"Ошибка при чтении файла: {e}")

