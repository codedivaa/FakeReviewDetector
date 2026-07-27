# ⭐ Fake Review Detector

A Python-based command-line application that intelligently analyzes customer reviews and flags potentially fake, spammy, or suspicious reviews using a rule-based heuristic scoring system. The project demonstrates practical applications of **Natural Language Processing (NLP)** concepts, **text preprocessing**, **regular expressions**, **data analysis**, and **data visualization in the terminal** without relying on machine learning models.

Instead of simply classifying reviews as "Fake" or "Real", the detector explains **why** a review was flagged, making the analysis transparent and easy to understand.

---

# 📸 Preview

```text
────────────────── FAKE REVIEW DETECTOR ──────────────────

📋 Fake Review Analysis

┌─────────────────────────────┬────────┬───────┬──────────────┬─────────────────────────────┐
│ Review                      │ Rating │ Score │ Prediction   │ Reasons                     │
├─────────────────────────────┼────────┼───────┼──────────────┼─────────────────────────────┤
│ BEST PRODUCT EVER!!!!!!     │   5    │  80   │ 🔴 Fake      │ ALL CAPS, Spam Phrase       │
│ Nice                        │   5    │  15   │ 🟢 Real      │ Very short review           │
│ Highly recommend buy now!!! │   5    │  65   │ 🔴 Fake      │ Spam Phrase, Too many !     │
└─────────────────────────────┴────────┴───────┴──────────────┴─────────────────────────────┘

✔ Analysis Complete
✔ Results saved to output.csv
```

---

# 🚀 Features

* 🔍 Detects suspicious customer reviews
* ⭐ Calculates a Fake Review Score (0–100)
* 🟢 Classifies reviews as Real, Suspicious, or Fake
* 📝 Explains every prediction with detailed reasons
* 📊 Generates a complete CSV report
* 🎨 Beautiful terminal interface using Rich
* 📈 Displays review statistics
* 🚩 Identifies common spam phrases
* 📌 Shows the most suspicious reviews
* ⚡ Fast analysis with minimal dependencies

---

# 🧠 Detection Rules

The detector evaluates each review using several heuristic rules.

## 📝 Review Length

Flags reviews that contain very few words.

Example:

```text
Nice
```

Very short reviews often contain little meaningful information and may indicate low-quality or automated submissions.

---

## 🔠 ALL CAPS Detection

Detects reviews written entirely in uppercase letters.

Example:

```text
BEST PRODUCT EVER
```

Excessive capitalization is commonly found in promotional or spam reviews.

---

## ❗ Excessive Punctuation

Flags reviews containing many exclamation or question marks.

Example:

```text
Amazing!!!!!!!!!
```

Repeated punctuation can indicate exaggerated marketing language.

---

## 🔁 Repeated Letters

Detects artificially stretched words.

Example:

```text
goooooood
```

---

## 🔄 Repeated Words

Example:

```text
Amazing amazing amazing product
```

Repetition is a common characteristic of low-quality spam.

---

## 🚩 Spam Phrase Detection

Looks for commonly used promotional phrases such as:

* Buy Now
* Must Buy
* Best Product
* Highly Recommend
* Exclusive Offer
* Limited Offer
* Guaranteed
* Click Here

---

## 🌐 URL Detection

Flags reviews containing external websites.

Example:

```text
Visit www.example.com
```

Legitimate customer reviews rarely include promotional links.

---

## 😀 Emoji Spam

Detects excessive emoji usage.

Example:

```text
😍😍😍🔥🔥💯💯
```

---

## ❤️ Excessive Positive Language

Looks for repeated positive words like:

* Amazing
* Perfect
* Excellent
* Fantastic
* Wonderful
* Awesome

Repeated promotional wording increases the fake review score.

---

## ⚖ Rating Mismatch

Detects contradictions between the rating and the review text.

Example:

```text
★★★★★
Worst product ever.
```

or

```text
★☆☆☆☆
Amazing quality.
```

Such inconsistencies are often indicators of manipulated reviews.

---

# 📊 Fake Review Score

Each suspicious behavior contributes to an overall Fake Score.

|  Score | Classification |
| -----: | -------------- |
|   0–29 | 🟢 Real        |
|  30–59 | 🟡 Suspicious  |
| 60–100 | 🔴 Fake        |

---

# 📂 Project Structure

```text
FakeReviewDetector/
│
├── main.py
├── reviews.csv
├── output.csv
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore
```

---

# ⚙ Installation

Clone the repository

```bash
git clone https://github.com/yourusername/FakeReviewDetector.git
```

Move into the project directory

```bash
cd FakeReviewDetector
```

Create a virtual environment

```bash
python -m venv venv
```

Activate it

### macOS / Linux

```bash
source venv/bin/activate
```

### Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# ▶ Running the Project

```bash
python main.py
```

---

# 📥 Input Format

Create a CSV file named **reviews.csv**

```csv
review,rating
"This product is amazing!!! Buy now!!!!",5
"Good quality and fast delivery.",5
"Worst purchase ever.",1
"BEST PRODUCT EVER!!!!!!",5
"Nice",5
```

---

# 📤 Output

The application automatically generates:

```text
output.csv
```

The output file contains:

* Original Review
* Rating
* Fake Score
* Prediction
* Reasons

Example

| Review                  | Rating | Fake Score | Prediction | Reasons               |
| ----------------------- | ------ | ---------: | ---------- | --------------------- |
| BEST PRODUCT EVER!!!!!! | 5      |         80 | 🔴 Fake    | ALL CAPS, Spam Phrase |
| Nice                    | 5      |         15 | 🟢 Real    | Very short review     |

---

# 🛠 Technologies Used

* 🐍 Python 3
* 🐼 Pandas
* 🎨 Rich
* 🔍 Regular Expressions (re)

---

# 💡 Future Improvements

* 🤖 Machine Learning-based fake review detection
* 🧠 Sentiment Analysis
* 🌍 Multi-language review support
* 📈 Interactive dashboard with Streamlit
* 📊 Review confidence score
* 📄 PDF report generation
* ☁ Cloud deployment
* 🌐 REST API using FastAPI
* 📦 Docker support
* 🔗 Amazon product review integration

---

# 🎯 Learning Outcomes

This project demonstrates practical experience with:

* Data preprocessing
* Text analysis
* Pattern matching using Regular Expressions
* CSV file handling
* Data manipulation with Pandas
* Terminal UI development with Rich
* Rule-based classification systems
* Explainable AI concepts
* File input/output operations
* Python project organization

---

# 🤝 Contributing

Contributions, ideas, feature requests, and bug reports are always welcome.

If you would like to improve this project:

1. Fork the repository
2. Create a new branch
3. Commit your changes
4. Push to your fork
5. Open a Pull Request

---

# ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.

It helps others discover the project and motivates future improvements!

Happy Coding! 🚀🐍
