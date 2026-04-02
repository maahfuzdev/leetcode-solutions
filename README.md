<div align="center">

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=700&size=30&pause=1000&color=00D9FF&center=true&vCenter=true&width=600&lines=LeetCode+Solutions+%F0%9F%A7%A0;Clean+%7C+Readable+%7C+Pythonic;Solving+one+problem+at+a+time..." alt="Typing SVG" />

<br/>

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![LeetCode](https://img.shields.io/badge/LeetCode-FFA116?style=for-the-badge&logo=leetcode&logoColor=black)
![Problems Solved](https://img.shields.io/badge/Solved-15%20Problems-00D9FF?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

<br/>

> *"Every expert was once a beginner. Every pro was once an amateur."*

</div>

---

## 📌 Overview

A curated personal repository of **LeetCode problem solutions** written in clean, well-commented Python. Each solution includes explanation of the approach, time complexity, and space complexity — built for revision, learning, and interview preparation.

---

## 📊 Progress Tracker

<div align="center">

| 🟢 Easy | 🟡 Medium | 🔴 Hard | 📦 Total |
|:-------:|:---------:|:-------:|:--------:|
|   14    |     1     |    0    |  **15**  |

</div>

```
Overall Progress  ████████░░░░░░░░░░░░░░░░░░░░  15 / 100
```

**Goal:** Solve **100 Easy** problems → then move to Medium 🚀

---

## 📁 Repository Structure

```
📦 LeetCode-Solutions
├── 📂 Easy Problem/
│   ├── 📂 Array/
│   │   └── 1. Two Sum.py
│   ├── 📂 Binary Search/
│   ├── 📂 Linked List/
│   ├── 📂 Math/
│   ├── 📂 Stack/
│   └── 📂 String/
└── 📄 README.md
```

---

## 🗂️ Solutions Index

### 🟢 Easy

| # | Problem | Category | Approach | Time | Space |
|---|---------|----------|----------|------|-------|
| 1 | [Two Sum](Easy%20Problem/Array/1.%20Two%20Sum.py) | Array | HashMap | O(n) | O(n) |
| — | *More coming soon...* | — | — | — | — |

> 📝 Table updates automatically as new solutions are pushed.

---

## 🧠 Solution Style Guide

Every solution in this repo follows a consistent format:

```python
# Problem: Two Sum (#1)
# Difficulty: Easy
# Category: Array
#
# Approach: Use a hashmap to store visited numbers.
#           For each element, check if its complement exists.
#
# Time Complexity:  O(n)
# Space Complexity: O(n)

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
```

---

## 🚀 How to Run

```bash
# Clone the repository
git clone https://github.com/maahfuzdev/LeetCode-Solutions.git
cd LeetCode-Solutions

# Run any solution directly
python "Easy Problem/Array/1. Two Sum.py"
```

**Requirements:** Python 3.8+

---

## 🎯 Goals & Roadmap

- [x] Set up repo structure
- [x] Solve 15 problems
- [ ] Reach **50 Easy** problems
- [ ] Reach **100 Easy** problems
- [ ] Start **Medium** problems (Arrays, Sliding Window, DP)
- [ ] Add unit tests for each solution
- [ ] Add solution explanations in Bangla (optional)

---

## 🛠️ Tech & Tools

| Tool | Purpose |
|------|---------|
| 🐍 Python 3 | Primary language |
| 💻 VS Code | Code editor |
| 🌐 LeetCode.com | Problem source |
| 🐙 GitHub | Version control |

---

## 🤝 Contributing

Contributions are welcome! If you'd like to add a solution:

1. **Fork** the repository
2. **Create** a branch: `git checkout -b add/problem-name`
3. **Follow** the solution style guide above
4. **Submit** a Pull Request

> 💡 Open an issue first to align on coding style before submitting.

---

## 📌 Notes

- Filenames are **problem-indexed** for fast searching (e.g., `1. Two Sum.py`)
- Every file includes **approach, time & space complexity** in comments
- Solutions aim to be **readable first**, optimal second

---

<div align="center">

**Made with 💙 and lots of ☕**

*If this repo helped you, consider giving it a ⭐ — it motivates more solutions!*

<br/>

![Visitor Count](https://visitor-badge.laobi.icu/badge?page_id=maahfuzdev.LeetCode-Solutions)

</div>
