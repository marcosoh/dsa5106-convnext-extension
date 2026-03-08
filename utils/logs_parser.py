import json
import os
from typing import Any, Dict, List


class LogsParser:
    @staticmethod
    def load_txt_logs(file_path: str) -> List[Dict[str, Any]]:
        """
        Reads a .txt file where each line is a JSON string.

        Args:
            file_path: Path to the log file.

        Returns:
            A list of dictionaries representing each log entry.
        """
        if not os.path.exists(file_path):
            print(f"Error: The file '{file_path}' does not exist.")
            return []

        parsed_lines = []
        try:
            with open(file_path, "r") as f:
                for i, line in enumerate(f, 1):
                    line = line.strip()
                    if not line:
                        continue  # Skip empty lines

                    try:
                        parsed_lines.append(json.loads(line))
                    except json.JSONDecodeError:
                        # Handles partial lines if the training crashed
                        print(f"Warning: Skipping malformed JSON on line {i}.")

            return parsed_lines

        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return []

    @staticmethod
    def extract_metrics(logs: List[Dict[str, Any]], *metrics: str) -> Dict[str, List]:
        """
        Organizes specific metrics into lists for analysis or plotting.

        Args:
            logs_list: The list of dictionaries from load_txt_logs.
            *metrics: Variable number of keys to extract (e.g., 'epoch', 'train_loss').

        Returns:
            A dictionary where keys are metric names and values are lists of data.
            Example:
                {
                    "epoch": [1, 2, 3],
                    "train_loss": [0.85, 0.42, 0.21]
                }

        Example Usage:
            >>> parser = LogsParser()
            >>> logs = [{"epoch": 1, "train_loss": 0.5}, {"epoch": 2, "train_loss": 0.3}]
            >>> result = parser.extract_metrics(logs, "epoch", "train_loss")
            >>> print(result["train_loss"])
            [0.5, 0.3]
        """
        result = {metric: [] for metric in metrics}
        for entry in logs:
            for metric in metrics:
                val = entry.get(metric)
                if val is not None:
                    result[metric].append(val)
        return result
