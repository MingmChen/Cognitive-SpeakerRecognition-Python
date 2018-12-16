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


def Delete_ALL_Profile():
    global subscription_key
    ids = print_all_profiles(subscription_key)

    for i in ids:
        delete_profile(subscription_key, i)


# ffmpeg -v 8 -i {0} -f wav -acodec pcm_s16le {1}
# sox zy2.wav -c1 -r 16000 output.wav
if __name__ == '__main__':
    # profile_id = MS_verify_enroll('zy.wav')
    # verify_file(subscription_key, 'zy.wav', profile_id)
    verify_file(subscription_key, 'test.wav',
                'f503ad47-726d-46b5-bbec-98be024994eb')
    verify_file(subscription_key, 'zy4.wav',
                'f503ad47-726d-46b5-bbec-98be024994eb')
    verify_file(subscription_key, 'zy.wav',
                'f503ad47-726d-46b5-bbec-98be024994eb')
