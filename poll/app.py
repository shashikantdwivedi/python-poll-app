from flask import Flask, render_template, redirect, request, url_for, flash
import database_functions as db_fun

app = Flask(__name__)
app.secret_key = "May the best man win"


@app.route("/")
def club_poll_information():
    return render_template("info.html")


@app.route("/club-poll/voting")
def club_poll_voting():
    candidates = db_fun.get_all_candidates()
    print(candidates)
    return render_template("voting.html", candidates=candidates)


@app.route("/club-poll/voting/vote/<kid>")
def club_poll_voting_vote(kid):
    ip = request.environ["REMOTE_ADDR"]
    output = db_fun.vote(ip, kid)
    if not output:
        flash(
            "Sorry your vote doesn't count because either you have already voted or you are voting  for  yourself"
        )
    else:
        flash("You have successfully voted")
    return redirect(url_for("club_poll_voting"))


@app.route("/club-poll/become_candidate")
def club_poll_become_candidate():
    print(request.environ["REMOTE_ADDR"])
    return render_template("candidate.html")


@app.route("/club_poll/become_candidate/adding", methods=["POST"])
def club_poll_candidate_addding():
    name = (request.form["name"]).strip()
    kid = (request.form["kid"]).strip()
    position = int((request.form["post"]).strip())
    ip = str(request.environ["REMOTE_ADDR"])
    output = db_fun.become_candidate(name, kid, position, ip)
    if output:
        flash("Congratulation you have successfully registered")
    else:
        flash("It seems like you have already registered")
    return redirect(url_for("club_poll_voting"))


if __name__ == "__main__":
    app.run(debug=True)
