# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    script.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: majrou <majrou@student.1337.ma>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/04/14 04:04:08 by majrou              #+#    #+#            #
#    Updated: 2022/04/14 04:04:09 by majrou              ###   ########.fr     #
#                                                                              #
# **************************************************************************** #

import requests, json,time
USER_ID= "3c108a5f9de825e5444dc3b266d575e51a54d16a119c972e83cbf9b58fa848f2"  #from https://profile.intra.42.fr/oauth/applications/new
USER_SECRET= "ba8bad12f6fef64747dafe66496238c2da5d2398e44fdefe6bbdb53db17e5272"
BASE_URL = "https://api.intra.42.fr"
def return_token():
    r = requests.post(url = BASE_URL+ "/oauth/token",
            data = {"grant_type" : "client_credentials",
                        "client_id": USER_ID,
                        "client_secret": USER_SECRET})
    data = r.json()
    return (data["access_token"])
def fetch_users(token ,page):
    r = requests.get(url = BASE_URL+"/v2/cursus_users",
            params = {"access_token" : token,
                "filter[campus_id]" : 55,
                "page[size]" : 100,
                "page[number]" : page
                },
            )
    return r.json()
def coordination():
    token = return_token()
    users = fetch_users(token,1)
    time.sleep(0.5)
    users +=fetch_users(token,2)
    users = sorted(users, key= lambda k : k["level"], reverse=True)
    for idx,user in enumerate(users):
        print("{}.{} {}".format(idx + 1,user["user"]["login"], user["level"]))
coordination()
