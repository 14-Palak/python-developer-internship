
from flask import Flask, render_template, request
import string
import secrets

app = Flask(__name__)


def generate_password(length, use_upper, use_lower,
                      use_numbers, use_symbols):

    groups = []

    if use_upper:
        groups.append(string.ascii_uppercase)

    if use_lower:
        groups.append(string.ascii_lowercase)

    if use_numbers:
        groups.append(string.digits)

    if use_symbols:
        groups.append(string.punctuation)

    if not groups:
        raise ValueError("Select at least one character type.")

    if length < len(groups):
        raise ValueError(
            f"Length must be at least {len(groups)}."
        )

    password = [
        secrets.choice(group) for group in groups
    ]

    all_characters = "".join(groups)

    for _ in range(length - len(password)):
        password.append(secrets.choice(all_characters))

    secrets.SystemRandom().shuffle(password)

    return "".join(password)


@app.route("/", methods=["GET", "POST"])
def home():

    passwords = []
    error = None

    length = 16
    count = 1

    options = {
        "uppercase": True,
        "lowercase": True,
        "numbers": True,
        "symbols": True
    }

    if request.method == "POST":

        try:
            length = int(request.form.get("length", 16))
            count = int(request.form.get("count", 1))

            options = {
                "uppercase": "uppercase" in request.form,
                "lowercase": "lowercase" in request.form,
                "numbers": "numbers" in request.form,
                "symbols": "symbols" in request.form
            }

            if length < 4 or length > 128:
                raise ValueError("Length must be between 4 and 128.")

            if count < 1 or count > 10:
                raise ValueError("Generate between 1 and 10 passwords.")

            for _ in range(count):
                password = generate_password(
                    length,
                    options["uppercase"],
                    options["lowercase"],
                    options["numbers"],
                    options["symbols"]
                )
                passwords.append(password)

        except ValueError as e:
            error = str(e)

    return render_template(
        "index.html",
        passwords=passwords,
        length=length,
        count=count,
        options=options,
        error=error
    )


if __name__ == "__main__":
    app.run(debug=True)
