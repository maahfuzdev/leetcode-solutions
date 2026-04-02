<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:00ff41,100:008f11&height=220&section=header&text=LeetCode%20Solutions&fontSize=52&fontColor=00ff41&fontAlignY=38&desc=⟨%20Clean%20/%20Readable%20/%20Pythonic%20⟩&descAlignY=58&descSize=18&animation=fadeIn&theme=dark" />

<br/>

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=700&size=20&pause=1000&color=00FF41&background=00000000&center=true&vCenter=true&width=650&lines=+%3E+Initializing+LeetCode+grind...+%F0%9F%A7%A0;+%3E+Language%3A+Python+%7C+Mode%3A+Optimal;+%3E+Status%3A+Solving+one+problem+at+a+time...;+%3E+Target%3A+100+problems+%5BLOC%3A+22%25%5D" alt="Typing SVG" />

<br/><br/>

![Python](https://img.shields.io/badge/Python-000000?style=for-the-badge&logo=python&logoColor=00FF41)
![LeetCode](https://img.shields.io/badge/LeetCode-000000?style=for-the-badge&logo=leetcode&logoColor=FFA116)
![Problems](https://img.shields.io/badge/Solved-22%20Problems-000000?style=for-the-badge&logo=checkmarx&logoColor=00FF41)
![Stars](https://img.shields.io/github/stars/maahfuzdev/LeetCode-Solutions?style=for-the-badge&logo=github&logoColor=00FF41&color=000000&labelColor=000000)
![Visitors](https://visitor-badge.laobi.icu/badge?page_id=maahfuzdev.LeetCode-Solutions&left_color=000000&right_color=008f11&left_text=visitors)

<br/>

```
██╗     ███████╗███████╗████████╗ ██████╗ ██████╗ ██████╗ ███████╗
██║     ██╔════╝██╔════╝╚══██╔══╝██╔════╝██╔═══██╗██╔══██╗██╔════╝
██║     █████╗  █████╗     ██║   ██║     ██║   ██║██║  ██║█████╗  
██║     ██╔══╝  ██╔══╝     ██║   ██║     ██║   ██║██║  ██║██╔══╝  
███████╗███████╗███████╗   ██║   ╚██████╗╚██████╔╝██████╔╝███████╗
╚══════╝╚══════╝╚══════╝   ╚═╝    ╚═════╝ ╚═════╝ ╚═════╝ ╚══════╝
```

> `// "Every expert was once a beginner. Every pro was once an amateur."`

</div>

---

## `$ whoami`

```python
developer = {
    "name"    : "maahfuzdev",
    "language": "Python 3",
    "mission" : "Crack DSA. Land the dream job.",
    "status"  : "Grinding LeetCode daily 💻",
    "goal"    : "Solve 100 Easy → conquer Medium → dominate Hard"
}
```

---

## `$ ./stats.sh`

<div align="center">

### 📊 GitHub Stats

![GitHub Stats](https://github-readme-stats.vercel.app/api?username=maahfuzdev&show_icons=true&theme=chartreuse-dark&bg_color=0d0d0d&border_color=00ff41&title_color=00ff41&text_color=00ff41&icon_color=00ff41&hide_border=false)
&nbsp;&nbsp;
![Top Languages](https://github-readme-stats.vercel.app/api/top-langs/?username=maahfuzdev&layout=compact&theme=chartreuse-dark&bg_color=0d0d0d&border_color=00ff41&title_color=00ff41&text_color=00ff41&hide_border=false)

<br/>

### 🔥 GitHub Streak

![GitHub Streak](https://streak-stats.demolab.com?user=maahfuzdev&theme=dark&background=0d0d0d&border=00ff41&ring=00ff41&fire=FFA116&currStreakNum=00ff41&sideNums=00ff41&currStreakLabel=00ff41&sideLabels=008f11&dates=008f11)

<br/>

### ⚡ LeetCode Stats

![LeetCode Stats](https://leetcard.jacoblin.cool/Coder_Mahfuz?theme=dark&font=Fira%20Code&ext=heatmap&border=1&border_radius=10)

</div>

---

<!-- AUTO-UPDATE:START -->
<!-- AUTO-UPDATE:END -->

---

## `$ tree ./solutions`

```
📦 LeetCode-Solutions/
│
├── 📂 Easy Problem/
│   ├── 📂 Array/           ← 3 solved
│   ├── 📂 Binary Search/   ← 2 solved
│   ├── 📂 Linked List/     ← 1 solved
│   ├── 📂 Math/            ← 1 solved
│   ├── 📂 Stack/           ← 1 solved
│   └── 📂 String/          ← 12 solved
│
├── 📂 Medium Problem/
│   └── 📂 Linked List/     ← 1 solved
│
├── 📂 Hard Problem/
│   └── 📂 Linked List/     ← 1 solved
│
└── 📄 README.md
```

---

## `$ cat style_guide.py`

```python
# ============================================================
# Problem   : Two Sum (#1)
# Difficulty: Easy  |  Category: Array
# ------------------------------------------------------------
# Approach  : HashMap — store seen numbers, check complement
#
# Time      : O(n)
# Space     : O(n)
# ============================================================

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

## `$ git clone && run`

```bash
# Clone the matrix
git clone https://github.com/maahfuzdev/LeetCode-Solutions.git
cd LeetCode-Solutions

# Execute any solution
python "Easy Problem/Array/1. Two Sum.py"
```

> **Requirements:** `Python >= 3.8`

---

## `$ cat roadmap.md`

```
[✓] Repository initialized
[✓] 15 problems solved
[✓] 22 problems solved
[ ] 50 Easy problems
[ ] 100 Easy problems  ← main target
[ ] Medium grind begins (Sliding Window, DP, Trees)
[ ] Unit tests added
[ ] Complexity visualizations added
```

---

## `$ cat contribute.md`

```bash
# Want to contribute? Follow these steps:

$ git fork maahfuzdev/LeetCode-Solutions
$ git checkout -b add/problem-name
$ # Follow the style guide above
$ git push && open pull-request

# Note: Open an issue first to align on style.
```

---

<div align="center">

```
> Session by maahfuzdev
> If this helped you, drop a ⭐ — fuel for the grind.
> [exit 0]
```

<br/>

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:008f11,100:00ff41&height=120&section=footer&animation=fadeIn" />

</div>
