from requests_oauthlib import OAuth1Session
import os
import json


def create_url():
    # User fields are adjustable, options include:
    # created_at, description, entities, id, location, name,
    # pinned_tweet_id, profile_image_url, protected,
    # public_metrics, url, username, verified, and withheld
    user_fields = "user.fields=id"
    # You can replace list-id with the List ID you wish to find members of.
    id = os.environ.get("LIST_ID")
    url = "https://api.twitter.com/2/lists/{}/members".format(id)
    return url, user_fields


def connect_to_endpoint(oauth, url, user_fields):
    response = oauth.get(url, params=user_fields)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(
                response.status_code, response.text
            )
        )
    return response.json()


def main():
    oauth = OAuth1Session(
        os.environ.get("CONSUMER_KEY"),
        client_secret=os.environ.get("CONSUMER_SECRET"),
        resource_owner_key=os.environ.get("ACCESS_TOKEN"),
        resource_owner_secret=os.environ.get("ACCESS_TOKEN_SECRET"),
    )
    url, user_fields = create_url()
    json_response = connect_to_endpoint(oauth, url, user_fields)
    print(json.dumps(json_response, indent=4, sort_keys=True))


if __name__ == "__main__":
    main()
