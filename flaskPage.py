from flask import Flask, abort, render_template, request
from functions import get_user_id_by_name, get_json_between_users, format_date

app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        # Get Users names
        user1 = request.form["user1_name"]
        user2 = request.form["user2_name"]

        # Get Users names by ID
        user1_id = get_user_id_by_name(user1)
        user2_id = get_user_id_by_name(user2)

        # Check if names exists
        if (user1_id or user2_id) == 1:
            abort(
                404,
                "The username doesnt exist. Reload and try again.",
            )

        # Get Json
        users_json = get_json_between_users(user1_id, user2_id)

        # Check if user follows the channel
        if users_json == 1:
            abort(
                404,
                "The username its not following the channel or the channel doesnt exists. Reload and try again.",
            )

        # Get data from json
        user1_name_var = users_json["from_name"]
        user2_name_var = users_json["to_name"]

        follow_date = users_json["followed_at"]

        # Format date
        array_date = format_date(follow_date)
        year, month, day, hour, minutes, seconds, month_number = array_date

        return render_template(
            "index.html",
            user1_name=user1_name_var,
            user2_name=user2_name_var,
            year=year,
            month=month,
            day=day,
            hour=hour,
            minutes=minutes,
            seconds=seconds,
        )

    else:
        return render_template("index.html", user1_name=None)


if __name__ == "__main__":
    app.run(debug=True)
