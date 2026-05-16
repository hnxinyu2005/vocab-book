# core/memory_algorithms/fsrs_v4/scheduler.py

# 注意 各个板块各司其职 这里的模块只负责填入相关的值 不能新增单词等操作

import csv
import datetime
from core.memory_algorithms.fsrs_v4.constants import FSRSReviewRating
from utils.constants import STANDARD_CSV_HEADERS
from algorithm import calculate_initial_stability, calculate_initial_difficulty, calculate_review_interval
from utils.system.path import get_wordbook_csv_path

def add_new_word(textbook: str, word: str):
    """
    新增单词时的初始赋值

    :param textbook: 单词书名字
    :param word: 单词（主键）
    :return: is_done: bool, error_msg: str
    """
    default_rating = FSRSReviewRating.GOOD # 临时默认评分
    csv_path = get_wordbook_csv_path(textbook)

    stability = calculate_initial_stability(default_rating) # 初始稳定性
    difficulty = calculate_initial_difficulty(default_rating) # 初始难度
    next_review = calculate_review_interval(stability)

    # 时间相关初始值
    today = datetime.date.today().strftime("%Y-%m-%d")
    next_review_date = (datetime.date.today() + datetime.timedelta(days=next_review)).strftime("%Y-%m-%d")

    try:
        with open(csv_path, "r", encoding="utf-8") as f:
            rows = list(csv.DictReader(f))
            # 校验表头
            if rows and list(rows[0].keys()) != STANDARD_CSV_HEADERS:
                pass

        word_found = False
        # 遍历查找
        for row in rows:
            if row["word"] == word and row["textbook"] == textbook:
                row["stability"] = stability
                row["difficulty"] = difficulty
                row["retrievability"] = 1.0
                row["next_review"] = next_review
                row["next_review_date"] = next_review_date
                row["last_rating"] = default_rating.name
                row["first_learn"] = today
                row["last_review"] = today
                row["days_since_last_review"] = 0

                word_found = True
                break

        if not word_found:
            return False, f"单词本 {textbook} 中未找到单词 {word}，无法更新记忆信息"

        # 重写CSV
        with open(csv_path, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=STANDARD_CSV_HEADERS)
            writer.writeheader()
            writer.writerows(rows)

        return True, ""

    except Exception as e:
        return False, f"更新记忆信息失败，{str(e)}"