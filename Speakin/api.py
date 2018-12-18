import speakin_number_vec_sdk
import time
import datetime
import hashlib
import hmac
import base64
import json


GMT_FORMAT = '%a, %d %b %Y %H:%M:%S GMT'

SecretId = 'AKIDe3Dx8IhdM4og08XK9fF5r6sKs0k2qpyge7bv'
SecretKey = 'c7BwQ3BzlMhAGeQgXI0j3zy4b0Y5sI71y2VJ1U5X'


# 腾讯云加密函数
def getSimpleSign(source, SecretId, SecretKey):
    if SecretId == "" or SecretKey == "":
        return "", ""
    dateTime = datetime.datetime.utcnow().strftime(GMT_FORMAT)
    auth = "hmac id=\"" + SecretId + \
        "\", algorithm=\"hmac-sha1\", headers=\"date source\", signature=\""
    signStr = "date: " + dateTime + "\n" + "source: " + source
    sign = hmac.new(bytes(SecretKey.encode('utf8')), bytes(
        signStr.encode('utf8')), hashlib.sha1).digest()

    sign = base64.b64encode(sign)
    sign = auth + str(sign, encoding='utf8') + "\""
    return sign, dateTime


def get_enroll_vector(filepaths):
    if len(filepaths) == 3:
        Source = 'test'
        sign, dateTime = getSimpleSign(Source, SecretId, SecretKey)
        headers = {'Authorization': sign, 'Date': dateTime, 'Source': Source}
        api = speakin_number_vec_sdk.NumreleasevApi()
        api.api_client.default_headers = headers

        enroll_result = api.post_num_vecforregister(
            file1=filepaths[0], file2=filepaths[1], file3=filepaths[2])
        print('enroll_result is:\n', enroll_result)
        result = eval(enroll_result)
        return result['data']['vecId']  # vec


def get_verify_vector(filepath):
    Source = 'test'
    sign, dateTime = getSimpleSign(Source, SecretId, SecretKey)
    headers = {'Authorization': sign, 'Date': dateTime, 'Source': Source}
    api = speakin_number_vec_sdk.NumreleasevApi()
    api.api_client.default_headers = headers

    verify_result = api.post_num_vecforcompare(file1="./test.wav")
    print('verify result is:\n', verify_result)
    result = eval(verify_result)
    return result['data']['vecId']  # vec


def one2oneCompere(enroll_vec, verify_vec):
    Source = 'test'
    sign, dateTime = getSimpleSign(Source, SecretId, SecretKey)
    headers = {'Authorization': sign, 'Date': dateTime, 'Source': Source}
    api = speakin_number_vec_sdk.NumreleasevApi()
    api.api_client.default_headers = headers
    req = speakin_number_vec_sdk.VoiceprintRawcompareReq()
    req.vec_id = enroll_vec
    req.cmp_vec_id_list = []

    req.cmp_vec_id_list.append(verify_vec)
    result = api.post_num_compare(req)
    print(result)
    return result


def speakin_Voice_verify(enroll_files, verify_file):
    enroll_vec = get_enroll_vector(enroll_files)
    verify_vec = get_verify_vector(verify_file)
    speakin_result = eval(one2oneCompere(enroll_vec, verify_vec))
    data = speakin_result['data']
    thresholdScore = data['thresholdScore']
    cmpResultList = data['cmpResultList'][0]
    score = cmpResultList['score']
    
    if score > thresholdScore:
        print('accept')
        return True
    else:
        print('reject')
        return False


if __name__ == "__main__":
    enroll_files = ['zy.wav', 'zy2.wav', 'zy3.wav']
    verify_file = 'test.wav'

    speakin_Voice_verify(enroll_files, verify_file)

    #enroll_vec = get_enroll_vector(enroll_files)
    #verify_vec = get_verify_vector(verify_file)
    #one2oneCompere(enroll_vec, verify_vec)
