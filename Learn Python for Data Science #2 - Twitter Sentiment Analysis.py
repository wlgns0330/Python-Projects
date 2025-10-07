import tweepy
from textblob import TextBlob

bearer_token = "AAAAAAAAAAAAAAAAAAAAAOoE4gEAAAAAQ0yGZ2VcG9yKG%2BZlfGvPBYqCyFM%3DjD2Ly4tFa0dd4UEdap8fwtrqO4mtUlVa72byW9frN1wCA2T5ry"

consumer_key = '9hPVWC12OpU2HztP1qyH79FY9'
consumer_secret = 'UWAjkkBoObLMhVZdFVFvmBDIFTrEROCfWj3ffnxhxdtPmrmCJp'

access_token = '1602090308636127232-peDbyXnLCeuQcAdPdkXRNlo3KXX4uB'
access_token_secret = '9yyyefjSAEBUFoQxCrKGmF2tHVpgNIyFq6AhjdbBQBrsI'

client = tweepy.Client(
    bearer_token=bearer_token
)

# Replace with your X username (no @)
user = client.get_user(username="Wadawadabang")

if user.data:
    print("User ID:", user.data.id)
    print("Username:", user.data.username)
    print("Name:", user.data.name)
else:
    print("User not found")