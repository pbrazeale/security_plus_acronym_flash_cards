
# Security+ Acronym Flash Cards

## A flash card study tool for anyone needing to study the compTIA Security+ SY0-701 Acronym List.

A comprehensive study guide for all 327 acronyms that could be used on the exam.

## Tech
- Language: Python 3.12.8
- Modules: Tkinter, Pandas, and Random

## How to:
1. Clone the project
2. Install Python:
	1. https://www.python.org/downloads/
3. `pip install pandas`
4. Run main.py in the terminal
	1. `python main.py`

### Interface
1. Acronym will display in bold on a white card.
2. After 3 seconds, the "spelled out" version will display on a green card.
3. If you know the acronym select the **Green Checkmark** at any time.
	- This will remove the acronym from your list permanently.
4. If you *don't* know the acronym select the **Red X** at any time.
	1. This will keep the acronym in your list for future study.
5. Once you've mastered all 327 words, your cards will be blank.

#### Example In Use



## Tweaking:
1. To modify delay between "acronym" and "spelled out":
	1. `flip_timer = window.after(3000, func=flip_card)`
	2. Modify `3000` (3 seconds/3,000 milliseconds)
		1. Modify on line 26
		2. Modify on line 46

## Did this help?
If you found value in the study material star the project. 
