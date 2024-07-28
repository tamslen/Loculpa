    from dotenv import load_dotenv
    import os

    load_dotenv()  # Take environment variables from .env.

    ZENDESK_USER_EMAIL = os.getenv('ZENDESK_USER_EMAIL')

    if ZENDESK_USER_EMAIL is None:
        print("Error: The environment variable ZENDESK_USER_EMAIL is not set.")
    else:
        print(f"The Zendesk user email is: {ZENDESK_USER_EMAIL}")
    