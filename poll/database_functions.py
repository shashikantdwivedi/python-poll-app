import db


def become_candidate(name, kid, position, ip):
    db_data = {
        "_id": kid,
        "name": name,
        "position": position,
        "ip": ip,
        "votes": 0,
        "voted_ip": [],
    }
    if not db.presidential.find_one({"_id": kid}):
        if kid != "k14456":
            db.presidential.insert_one(db_data)
            return True
        else:
            return False
    else:
        return False


def vote(ip, kid):
    result = db.presidential.find_one({"_id": kid})
    if str(ip) in result["voted_ip"]:
        return False
    else:
        query = {"_id": kid}
        candidate_data = db.presidential.find_one({"_id": kid})
        candidate_data["voted_ip"].append(ip)
        update = {
            "$set": {
                "votes": candidate_data["votes"] + 1,
                "voted_ip": candidate_data["voted_ip"],
            }
        }
        check_data = db.presidential.find_one({"_id": "voted"})
        if ip in check_data[str(candidate_data["position"])]:
            return False
        db.presidential.update_one(query, update)
        query = {"_id": "voted"}
        result_data = db.presidential.find_one(query)
        result_data[str(candidate_data["position"])].append(ip)
        update = {
            "$set": {
                str(candidate_data["position"]): result_data[
                    str(candidate_data["position"])
                ]
            }
        }
        db.presidential.update_one(query, update)
        return True


def get_all_candidates():
    candidates = []
    result = db.presidential.find({"_id": {"$regex": "^[kK]"}})
    for x in result:
        candidates.append(x)
    print(candidates)
    return candidates
