#create - team_name, odds, wager, payout
from flask import request, jsonify
from config import app, db
from models import Wager


@app.route("/mybets", methods=["GET"])
def get_bets():
    bets = Wager.query.all()
    json_bets = list(map(lambda x : x.to_json(), bets))
    return jsonify({"bets": json_bets})



@app.route("/place_bet", methods=["POST"])
def place_bet():
    team_name = request.json.get("teamName")
    odds = request.json.get("odds")
    wager = request.json.get("wager")
    payout = request.json.get("payout")

    if not wager or not payout:
        return (
            jsonify({"message": "Ypu must enter amount to wager"}), 400
        )
    new_bet = Wager(team_name=team_name, odds=odds, wager=wager, payout=payout)

    try:
        db.session.add(new_bet)
        db.session.commit()
    except Exception as e:
        return jsonify({"message": str(e)}), 400
    
    return jsonify({"message": "user created"}), 201



if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True)