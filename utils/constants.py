# services/constants.py

# 单词文件夹
WORDBOOKS_FOLDER_NAME = "wordbooks"
# 默认单词库文件名
DEFAULT_WORDBOOK = "default"

# 标准CSV表头
STANDARD_CSV_HEADERS = [
    # 基础信息
    "word", "phonetic", "meaning", "example", "example_trans",
    "textbook", "unit",
    # 复习统计
    "review_count", "correct_count", "last_review",
    # 时间核心
    "first_learn", "last_review", "days_since_last_review",
    # fsrs算法核心
    "stability", "difficulty", "retrievability",
    # 复习间隔
    "next_review", "next_review_date",
    # 可选
    "last_rating", "status"
]

DEFAULT_ENCODING = "utf-8"

# 空值默认常量字典
DEFAULT_VALUES = {
    "phonetic": "未写入音标",
    "example": "未写入例句",
    "example_trans": "未写入例句翻译",
    "textbook": "未写入来源",
    "unit": "未写入单元信息",
    "last_review": "没有考察记录"
}

# 词性标记最大长度
POS_MAX_LENGTH = 6

# 窗口默认占屏百分比
DEFAULT_WINDOW_WIDTH_PERCENT = 0.5  # 默认宽度占屏幕40%
DEFAULT_WINDOW_HEIGHT_PERCENT = 0.5 # 默认高度占屏幕50%