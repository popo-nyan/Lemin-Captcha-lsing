import hashlib
import httpx
import uuid
from typing import Optional


def lsing_calculation(captcha_id: str,
                      challenge_id: str = str(uuid.uuid4()),
                      screen_width: str = "1920",
                      screen_height: str = "1080",
                      utc_offset: str = "-540") -> str:
    return hashlib.md5(str("https://api.leminnow.com/captcha/v1/cropped/%s/image/%s?+screen_width=%s&screen_height=%s&utc_offset=%s&v=3&enc=SHA256" % (captcha_id, challenge_id, screen_width, screen_height, utc_offset)).encode()).hexdigest()


if __name__ == "__main__":
    print(lsing_calculation(captcha_id="CROPPED_3dfdd5c_d1872b526b794d83ba3b365eb15a200b"))
