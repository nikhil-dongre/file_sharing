from .models import Files,Folder
from rest_framework import serializers
import shutil

class FileListSerializers(serializers.Serializer):
    files = serializers.ListField(
        child=serializers.FileField(max_length=1000000, allow_empty_file=False, use_url=False)
    )


    def zip_files(self,folder_name):
        print("sfsf")
        shutil.make_archive(f"public/static/zip/{folder_name}", 'zip', f"public/static/{folder_name}")

    def create(self, validated_data):
        folder = Folder.objects.create()
        files = validated_data.pop('files')
        files_objs = []
        for file in files:
            files_obj = Files.objects.create(folder=folder, file=file)
            files_objs.append(files_obj)
        print(folder.uid)

        self.zip_files(folder.uid)
        return { 'folder' : folder.uid,'files' : {} }
        files_data = [{'file': str(file.file)} for file in files_objs]
        # Return the data of uploaded files along with the folder UID
        # return {'files': files_data, 'folder': str(folder.uid)}