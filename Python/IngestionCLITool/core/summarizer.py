from collections import defaultdict

class Summarizer:
    @staticmethod
    def summarize(records):
        summary = defaultdict(float)
        for row in records:
            summary[row["Company"]] += row["Quantity"] * row["Price"]
        return summary
