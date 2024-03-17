from config import db

class Wager(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    team_name = db.Column(db.String(100), unique=False, nullable=False)
    odds = db.Column(db.Integer, nullable=False)
    wager = db.Column(db.Integer, nullable=False)
    payout = db.Column(db.Integer, nullable=False)

    def to_json(self):
        return {
            "id": self.id,
            "teamName": self.team_name,
            "odds": self.odds,
            "wager": self.wager,
            "payout": self.payout
        }