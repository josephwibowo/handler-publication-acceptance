import argparse
import json
import sys

def consume(args):
    if args.seed != "second" or args.packet:
        sys.exit(2)
    if args.input is None:
        print(json.dumps({"action":"repair", "seed":"second", "observable":True}))
        return
    events = json.loads(args.input)
    if not isinstance(events, list) or not events:
        sys.exit(2)
    seen = {}
    values, identities = [], []
    for event in events:
        if (not isinstance(event, dict) or set(event) != {"schema_version", "event_id", "value"}
            or event["schema_version"] != 1
            or not isinstance(event["event_id"], str) or not event["event_id"]
            or not isinstance(event["value"], str) or not event["value"]):
            sys.exit(2)
        identity = event["event_id"]
        if identity in seen:
            if seen[identity] != event:
                sys.exit(2)
            continue
        seen[identity] = event
        values.append(event["value"])
        identities.append(identity)
    print(json.dumps({"schema_version":1, "seed":"second",
                      "values":values, "event_ids":identities}))

parser = argparse.ArgumentParser()
parser.add_argument("action", choices=["objective", "repair"])
parser.add_argument("--seed", required=True)
parser.add_argument("--packet", action="store_true")
parser.add_argument("--input")
args = parser.parse_args()
if args.action == "objective":
    if args.packet and args.seed:
        print(json.dumps({"schema_version":1, "event_id":"seed:" + args.seed, "value":args.seed}))
    elif args.seed == "first" and args.input is None:
        print(json.dumps({"action":"objective", "seed":"first", "observable":True}))
    else:
        sys.exit(2)
else:
    consume(args)

# handler-acceptance: fail
