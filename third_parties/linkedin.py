import os
import requests

# Here you are defining a new function where you pass the link to a profile and then the function extracts information from it
# You are using Proxycurl API to get JSON info on linkedin profiles

api_key = "5c9xIJFBE5rKKFhP_y6s3Q"


def scrape_linkedin_profile(linked_profile_url: str):
    """scape information from LinkedIn profiles,
    Manually scape the information form LinkedIn Profile"""
    api_endpoint = "https://nubela.co/proxycurl/api/v2/linkedin"
    header_dic = {"Authorization": "Bearer " + api_key}

    # You are using the requests module to request information from an API endpoint
    response = requests.get(
        api_endpoint,
        params={
            "url": linked_profile_url,
        },
        headers=header_dic,
    )

    # You might get a lot of empty fields, so best to eliminate empty stuff to reduce the tokens sent across
    Data_Output = response.json()
    Data_Output = {
        k: v
        for k, v in Data_Output.items()
        if v not in ([], "", "", None)
        and k not in ["people also viewed", "certifications"]
    }
    if Data_Output.get("groups"):
        for group_dict in Data_Output.get("groups"):
            group_dict.pop("profile_pic_url")

    return response


linkedin_data = scrape_linkedin_profile(
    linked_profile_url="https://www.linkedin.com/in/johnrmarty/"
)


# This is to print indented JSON
import json

print(json.dumps(linkedin_data.json(), indent=4))
