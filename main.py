# ============================
# Fake Review Detector
# main.py (Part 1/2)
# ============================

import pandas as pd
import re
from rich.console import Console
from rich.table import Table

console = Console()

console.rule("[bold cyan]FAKE REVIEW DETECTOR[/bold cyan]")

# Load CSV
df = pd.read_csv("reviews.csv")

spam_phrases = [
    "buy now",
    "must buy",
    "best product",
    "life changing",
    "100%",
    "highly recommend",
    "limited offer",
    "click here",
    "guaranteed",
    "don't miss",
    "exclusive",
]

scores = []
reason_list = []

for review, rating in zip(df["review"], df["rating"]):

    review = str(review)
    lower = review.lower()

    score = 0
    reasons = []

    # -----------------------------
    # Very Short Review
    # -----------------------------
    if len(review.split()) < 3:
        score += 15
        reasons.append("Very short review")

    # -----------------------------
    # ALL CAPS
    # -----------------------------
    if review.isupper():
        score += 20
        reasons.append("ALL CAPS")

    # -----------------------------
    # Too many exclamation marks
    # -----------------------------
    if review.count("!") >= 3:
        score += 20
        reasons.append("Too many exclamation marks")

    # -----------------------------
    # Too many question marks
    # -----------------------------
    if review.count("?") >= 3:
        score += 10
        reasons.append("Too many question marks")

    # -----------------------------
    # Repeated letters
    # Example: gooooood
    # -----------------------------
    if re.search(r"(.)\1{3,}", lower):
        score += 15
        reasons.append("Repeated letters")

    # -----------------------------
    # Repeated punctuation
    # -----------------------------
    if re.search(r"[!?]{4,}", review):
        score += 10
        reasons.append("Repeated punctuation")

    # -----------------------------
    # Emoji spam
    # -----------------------------
    emoji_count = len(re.findall(r"[😀-🙏🛒🔥💯😍❤️👍]", review))

    if emoji_count >= 3:
        score += 15
        reasons.append("Emoji spam")

    # -----------------------------
    # Repeated words
    # -----------------------------
    words = lower.split()

    if len(words) != len(set(words)):
        score += 10
        reasons.append("Repeated words")

    # -----------------------------
    # Spam phrases
    # -----------------------------
    for phrase in spam_phrases:

        if phrase in lower:
            score += 20
            reasons.append(f"Spam phrase ({phrase})")

    # -----------------------------
    # URL Detection
    # -----------------------------
    if "http" in lower or "www." in lower:
        score += 20
        reasons.append("Contains URL")

    # -----------------------------
    # Excessive Positive Words
    # -----------------------------
    positive_words = [
        "amazing",
        "excellent",
        "perfect",
        "awesome",
        "fantastic",
        "wonderful",
    ]

    positive_count = sum(lower.count(word) for word in positive_words)

    if positive_count >= 3:
        score += 15
        reasons.append("Excessive positive words")

    # -----------------------------
    # Long review
    # -----------------------------
    if len(review.split()) > 300:
        score += 10
        reasons.append("Unusually long review")

    # -----------------------------
    # Rating mismatch
    # -----------------------------
    if rating == 5 and ("worst" in lower or "terrible" in lower):
        score += 25
        reasons.append("Positive rating with negative text")

    if rating == 1 and (
        "excellent" in lower
        or "perfect" in lower
        or "amazing" in lower
    ):
        score += 25
        reasons.append("Negative rating with positive text")

    score = min(score, 100)

    scores.append(score)

    if reasons:
        reason_list.append(", ".join(reasons))
    else:
        reason_list.append("None")
# ============================
# Fake Review Detector
# main.py (Part 2/2)
# ============================

# Create new columns
df["Fake Score"] = scores
df["Reasons"] = reason_list


# -----------------------------
# Prediction Function
# -----------------------------
def classify(score):
    if score >= 60:
        return "🔴 Fake"
    elif score >= 30:
        return "🟡 Suspicious"
    else:
        return "🟢 Real"


df["Prediction"] = df["Fake Score"].apply(classify)

# Save report
df.to_csv("output.csv", index=False)

# -----------------------------
# Rich Table
# -----------------------------
table = Table(
    title="📋 Fake Review Analysis",
    show_lines=True,
    header_style="bold cyan"
)

table.add_column("Review", style="white", overflow="fold", width=45)
table.add_column("Rating", justify="center", style="yellow")
table.add_column("Score", justify="center")
table.add_column("Prediction", justify="center")
table.add_column("Reasons", overflow="fold", width=45)

for _, row in df.iterrows():

    score = row["Fake Score"]

    if score >= 60:
        score_text = f"[red]{score}[/red]"
    elif score >= 30:
        score_text = f"[yellow]{score}[/yellow]"
    else:
        score_text = f"[green]{score}[/green]"

    table.add_row(
        row["review"],
        str(row["rating"]),
        score_text,
        row["Prediction"],
        row["Reasons"]
    )

console.print(table)

# -----------------------------
# Dashboard
# -----------------------------
total = len(df)
real = (df["Prediction"] == "🟢 Real").sum()
sus = (df["Prediction"] == "🟡 Suspicious").sum()
fake = (df["Prediction"] == "🔴 Fake").sum()

avg_score = df["Fake Score"].mean()
highest = df["Fake Score"].max()
lowest = df["Fake Score"].min()

console.rule("[bold green]SUMMARY[/bold green]")

summary = Table(show_header=False, box=None)

summary.add_row("📄 Total Reviews", str(total))
summary.add_row("🟢 Real Reviews", str(real))
summary.add_row("🟡 Suspicious Reviews", str(sus))
summary.add_row("🔴 Fake Reviews", str(fake))
summary.add_row("⭐ Average Fake Score", f"{avg_score:.1f}")
summary.add_row("📈 Highest Score", str(highest))
summary.add_row("📉 Lowest Score", str(lowest))

console.print(summary)

# -----------------------------
# Top Spam Phrases
# -----------------------------
console.rule("[bold magenta]TOP SPAM PHRASES[/bold magenta]")

phrase_counts = {}

for phrase in spam_phrases:
    count = df["review"].astype(str).str.lower().str.contains(phrase).sum()
    phrase_counts[phrase] = count

spam_table = Table(show_header=True, header_style="bold magenta")
spam_table.add_column("Phrase")
spam_table.add_column("Occurrences", justify="center")

for phrase, count in sorted(
    phrase_counts.items(),
    key=lambda x: x[1],
    reverse=True
):
    spam_table.add_row(phrase, str(count))

console.print(spam_table)

# -----------------------------
# Most Suspicious Reviews
# -----------------------------
console.rule("[bold red]TOP SUSPICIOUS REVIEWS[/bold red]")

top_reviews = df.sort_values(
    by="Fake Score",
    ascending=False
).head(5)

top_table = Table(show_lines=True)

top_table.add_column("Score", justify="center")
top_table.add_column("Prediction", justify="center")
top_table.add_column("Review", overflow="fold", width=60)

for _, row in top_reviews.iterrows():
    top_table.add_row(
        str(row["Fake Score"]),
        row["Prediction"],
        row["review"]
    )

console.print(top_table)

console.rule("[bold cyan]REPORT GENERATED SUCCESSFULLY[/bold cyan]")

console.print("[bold green]✔ Analysis Complete[/bold green]")
console.print("[bold green]✔ Results saved to output.csv[/bold green]")
console.print("[bold green]✔ Fake review detection finished[/bold green]")