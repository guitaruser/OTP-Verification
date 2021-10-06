import os
import math
import random
import smtplib

# making the OTP
digits="0123456789"
OTP=""
for i in range(6):
    OTP+=digits[math.floor(random.random()*10)]
otp = OTP + " is your OTP"
msg= otp

# sending the OTP
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login("YOUR EMAIL", "YOUR PASSWORD")
emailid = input("Enter your email: ")
s.sendmail('&&&&&&&&&&&',emailid,msg)

# verifying the OTP
a = input("Enter Your OTP >>: ")
if a == OTP:
    print("Verified")
else:
    print("Please Check your OTP again")
