import argparse
import json
import sys

def consume(args):
    raise NotImplementedError("consumer contribution pending")

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
