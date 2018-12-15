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


# 用于注册用的函数
def MS_identify_enroll(file_path):
    profile_id = create_profile(subscription_key, locale)
    enroll_profile(subscription_key, profile_id, file_path, force_short_audio)
    return profile_id
    # enroll_dict = {"name": name, "profile_id": profile_id}
    # return enroll_dict


# 用于identify的函数
def MS_identify_identify(file_path, profile_ids):
    return identify_file(subscription_key, file_path, force_short_audio, profile_ids)


# 用于比较两端录音是不是一个人说的的函数
def MS_verify(enroll_wav_path, verify_wav_path):
    profile_ids = []
    enroll_id = MS_identify_enroll(enroll_file_path)
    profile_ids.append(enroll_id)
    identify_id = MS_identify_identify(verify_file_path, profile_ids)
    if enroll_id == identify_id:
        return True
    else:
        return False


if __name__ == '__main__':
    enroll_file_path = input('enroll_file_path:')
    verify_file_path = input('verify_file_path:')
    if MS_verify(enroll_file_path, verify_file_path):
        print('accept')
    else:
        print('reject')

