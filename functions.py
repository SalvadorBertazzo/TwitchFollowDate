from twitchAPI.twitch import Twitch

# -- Client ID + Phrase --
twitch = Twitch(
    "ssxxbm5n6xmc6d00plvq236xp87lm6",
    "qxnaqaivna1ss1rb86l6sa1yijviss",
)


def get_user_id_by_name(user):
    try:
        return twitch.get_users(logins=[user])["data"][0]["id"]
    except IndexError:
        return 1


def get_json_between_users(user1, user2):
    try:
        return twitch.get_users_follows(from_id=user1, to_id=user2)["data"][0]
    except IndexError:
        return 1


# Get month based on number
def get_month(month):
    if month[0] == "0":
        month = month[-1]

    month_number = int(month)

    months = [
        "Jan",
        "Feb",
        "Mar",
        "Apr",
        "May",
        "Jun",
        "Jul",
        "Aug",
        "Sep",
        "Oct",
        "Nov",
        "Dec",
    ]
    return months[int(month) - 1], month_number


# Split date information
def format_date(date):
    year = date[0:4]
    month, month_number = get_month(date[5:7])
    day = date[8:10]
    hour = date[11:13]
    minutes = date[14:16]
    seconds = date[17:19]

    return year, month, day, hour, minutes, seconds, month_number
