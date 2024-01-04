import hashlib
import httpx
import uuid
from typing import Optional


class LeminCaptcha:
    
    def __init__(self,
                 captcha_id: str):
        self.captcha_id = captcha_id
        self.__challenge_id = str(uuid.uuid4())
        self.__session = httpx.Client(http2=True)
        self.__screen_width = "1920"
        self.__screen_height = "1080"
        self.__utc_offset = "-540"
    
    def __lsing_calculation(self) -> str:
        return hashlib.md5(str("https://api.leminnow.com/captcha/v1/cropped/%s/image/%s?+screen_width=%s&screen_height=%s&utc_offset=%s&v=3&enc=SHA256" % (self.captcha_id, self.__challenge_id, self.__screen_width, self.__screen_height, self.__utc_offset)).encode()).hexdigest()
    
    def get_image_url(self) -> Optional[str]:
        response = self.__session.request(method="GET",
                                          url=f"https://api.leminnow.com/captcha/v1/cropped/{self.captcha_id}/image/{self.__challenge_id}",
                                          headers={
                                              "authority": "api.leminnow.com",
                                              "accept": "*/*",
                                              "accept-language": "ja",
                                              "user-agent": "Mozilla/5.0 (Windows NT 10.0; rv:102.0) Gecko/20100101 Firefox/102.0"},
                                          params={
                                              "screen_width": self.__screen_width,
                                              "screen_height": self.__screen_height,
                                              "utc_offset": self.__utc_offset,
                                              "v": "3",
                                              "enc": "SHA256",
                                              "lsign": self.__lsing_calculation()})
        if response.status_code == httpx.codes.OK:
            return response.text.split("|")[0]
        return


if __name__ == "__main__":
    image_url = LeminCaptcha(captcha_id="CROPPED_3dfdd5c_d1872b526b794d83ba3b365eb15a200b").get_image_url()
    print(image_url)
