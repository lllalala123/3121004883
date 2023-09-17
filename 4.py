import sys
# 使用库计算文本差异
import difflib
# 使用cProfile记录性能数据
import cProfile


def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    return text


def calculate_similarity(original_text, copied_text):
    d = difflib.Differ()
    original_lines = original_text.splitlines()
    copied_lines = copied_text.splitlines()

    # 使用库计算两个文本的差异
    diff = list(d.compare(original_lines, copied_lines))

    # 计算相似度，忽略空行
    total_chars = sum(len(line) for line in original_lines if line.strip())
    diff_chars = sum(len(line) for line in diff if line.startswith('  '))
    similarity = (1 - (diff_chars / total_chars)) * 100

    return round(similarity, 2)


def main():
    if len(sys.argv) != 4:
        print("Usage: python plagiarism_checker.py <原文文件路径> <抄袭版论文的文件路径> <答案文件路径>")
        return

    original_file_path = sys.argv[1]
    copied_file_path = sys.argv[2]
    answer_file_path = sys.argv[3]

    original_text = read_file(original_file_path)
    copied_text = read_file(copied_file_path)

    similarity = calculate_similarity(original_text, copied_text)

    with open(answer_file_path, 'w', encoding='utf-8') as answer_file:
        answer_file.write(f"{similarity:.2f}")


if __name__ == "__main__":
    main()

  #  cProfile.run("main()", sort='cumulative')

