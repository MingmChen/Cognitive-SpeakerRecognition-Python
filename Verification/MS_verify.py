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


def MS_verify(file_path):
    profile_id = create_profile(subscription_key, locale)
    enroll_profile(subscription_key, profile_id, file_path)

if __name__=='__main__':
    MS_verify('test.wav')
        
