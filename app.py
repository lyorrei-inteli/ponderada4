import os
import keyboard
import cv2
import time
import datetime
from dotenv import load_dotenv
from supabase import create_client, Client

load_dotenv()

# URL and Access Key
URL = "https://mevykdhhmprmbbhupxij.supabase.co"
KEY = os.getenv("SUPABASE_KEY")
supabase = create_client(URL, KEY)
bucket_name = "Images"


class VideoUploader:
    def __init__(self):
        self.camera = None
        self.output_file = None

    def upload_image(self, name):
        supabase.storage.from_(bucket_name).upload(name, name)
        print("File uploaded successfully")

    def delete_file(self, file_path):
        try:
            os.remove(file_path)
            print("Temporary file deleted successfully: {}".format(file_path))
        except OSError as e:
            print("Error occurred while deleting file: {}".format(file_path))
            print(e)

    def capture_and_upload_video(self):
        self.camera = cv2.VideoCapture(0)
        fourcc = cv2.VideoWriter_fourcc(*"mp4v")  # Use mp4v codec for .mp4 file
        current_time = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        output_file_name = "output_{}.mp4".format(current_time)  # Change file extension to .mp4
        self.output_file = cv2.VideoWriter(output_file_name, fourcc, 27.0, (1920, 1080))

        print("Recording started.")

        start_time = time.time()
        duration = 5
        time_left = duration

        while True:
            ret, frame = self.camera.read()
            if not ret:
                break

            self.output_file.write(frame)

            elapsed_time = time.time() - start_time
            time_left = duration - elapsed_time

            if time_left <= 0:
                break

            if int(elapsed_time) % 1 == 0:
                print("Time Left: {:.1f} seconds".format(time_left))

        print("Created a temporary file: {}".format(output_file_name))

        self.camera.release()
        self.output_file.release()
        cv2.destroyAllWindows()

        self.upload_image(output_file_name)
        self.delete_file(output_file_name)
        self.prints()

    def uploaded_videos(self):
        res = supabase.storage.from_(bucket_name).list()
        print("Logs:")
        print(res)
        self.prints()

    @staticmethod
    def prints():
        print("................................")
        print("Press Enter to start recording.")
        print("Press Space to get a log of uploaded videos")


uploader = VideoUploader()
keyboard.add_hotkey("enter", uploader.capture_and_upload_video)
keyboard.add_hotkey("space", uploader.uploaded_videos)

uploader.prints()

keyboard.wait("esc")  # Wait for the user to press the "Esc" key to exit

keyboard.clear_all()  # Clean up the keyboard hook
