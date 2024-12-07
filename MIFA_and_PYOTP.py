import pyotp

def generate_otp(secret):
    totp = pyotp.TOTP(secret)
    return totp.now()

def authenticate_with_mfa(otp):
    import boto3
    client = boto3.client('sts')
    response = client.get_session_token(
        SerialNumber='arn:aws:iam::123456789012:mfa/user',
        TokenCode=otp
    )
    return response
