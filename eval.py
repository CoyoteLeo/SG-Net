import argparse
import json

from run_squad2 import read_squad_examples
from transformers.data.metrics.squad_metrics import squad_evaluate


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--predict_file",
        default="data/squad/dev-v2.0.json",
        type=str,
        help="SQuAD json for predictions. E.g., dev-v1.1.json or test-v1.1.json",
    )
    parser.add_argument("--predict_tag_file", default="data/squad/dev-v2.0_tag", type=str)
    parser.add_argument("--prediction_file", type=str)
    args = parser.parse_args()

    eval_examples = read_squad_examples(
        input_file=args.predict_file, input_tag_file=args.predict_tag_file, is_training=False,
    )
    with open(args.prediction_file) as f:
        result = json.load(f)
    print(json.dumps(dict(squad_evaluate(eval_examples, result)), indent=4))


if __name__ == "__main__":
    main()
