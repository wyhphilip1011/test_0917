# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import re
hkid_regex = r"[A-G]{1,2}\d{6}\(\d\)"
phone_number_regex = r"(\+852|\b)(\d{8})\b"
link_regex = r"(https?):\/\/([\w\.-]+)([/\w\-_]+)?(\?[\w=&]+)?(#[\w]+)?"

sample_text = """I am Harvey. My HKID number is AB123456(7).
My phone number is 91234888.
Here is my portfolio website: https://harvey.me/portfolio/#section1.
Please feel free to contact me if needed.

Hi I am interested in the position.
Please visit http://jason-portfolio.com?cv=1 to see my previous works.
Below is my information.
Name: Jason
Tel: +85299243321
Id card number: D922118(1)
Reference number : 203476912746"""

