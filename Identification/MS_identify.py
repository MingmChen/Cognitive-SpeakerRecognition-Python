#################################################
from key import *
#################################################
# import sdk
from CreateProfile import *
from GetProfile import *
from DeleteProfile import *
from EnrollmentResponse import *
from EnrollProfile import *
from EnrollmentResponse import *
from IdentificationProfile import *
from IdentificationResponse import *
from IdentificationServiceHttpClientHelper import*
from IdentifyFile import *
from PrintAllProfiles import *
from ProfileCreationResponse import *
from ResetEnrollments import *
#################################################


def MS_identify(file_path):
    profile_id = create_profile(subscription_key, locale)
    enroll_profile(subscription_key, profile_id, file_path, force_short_audio)


if __name__ == '__main__':
    print_all_profiles(subscription_key)
