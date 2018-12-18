################################################
from key import *
#################################################
# import sdk
from CreateProfile import *
from GetProfile import *
from DeleteProfile import *
from EnrollmentResponse import *
from EnrollProfile import *
from EnrollmentResponse import *
from PrintAllProfiles import *
from ProfileCreationResponse import *
from ResetEnrollments import *
from ResetEnrollments import *
from VerificationProfile import *
from VerificationResponse import *
from VerificationServiceHttpClientHelper import *
from VerifyFile import *
################################################


def MS_verify_enroll(file_paths):
    if len(file_paths) == 3:
        profile_id = create_profile(subscription_key, locale)
        for file_path in file_paths:
            enroll_profile(subscription_key, profile_id, file_path)
        return profile_id

    else:
        print("error")


def Delete_ALL_Profile():
    global subscription_key
    ids = print_all_profiles(subscription_key)

    for i in ids:
        delete_profile(subscription_key, i)


# ffmpeg -v 8 -i {0} -f wav -acodec pcm_s16le {1}
# sox zy2.wav -c1 -r 16000 output.wav
if __name__ == '__main__':
    Delete_ALL_Profile()
    paths = ['e3.wav', 'e3.wav', 'e3.wav']
    MS_id = MS_verify_enroll(paths)

    verify_file(subscription_key, 'e3.wav', MS_id)
