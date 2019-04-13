from ProblemSolving_python.three.Stack.stack import Stack


def check_parens(text):
    """
    :param text: 包含括号的字符串，被检测字符串
    :return: 检查成功与否
    """
    parens = "()[]{}"
    open_parens = "([{"
    opposite = {")": "(", "]": "[", "}": "{"}   # 表示配对关系的字典

    def parentheses(text):
        """
        括号生成器，每次调用返回text里的下一括号及其位置
        每次调用生成括号的及其位置如test[1]=(
        :param text: 包含括号的字符串，被检测字符串
        :return:
        """
        i, text_len = 0, len(text)
        while True:
            while i < text_len and text[i] not in parens:
                i += 1
            if i >= text_len:
                return
            yield text[i], i
            i += 1

    st = Stack()
    for pr, i in parentheses(text):
        if pr in open_parens:
            # 将所有的开括号入栈
            st.push(pr)
        elif st.is_empty() and pr in parens:
            # 闭括号多于开括号的情况
            print("Unmatching is found at", i, "for", pr)
        elif st.pop() != opposite[pr]:
            # 将开括号出栈，与闭口号对于字典的值（闭括号对应的开括号）相比较
            print("Unmatching is found at", i, "for", pr)
    print("all parentheses are correctly matched")
    return True


if __name__ == '__main__':
    print(check_parens("(ddddd{ddds}))"))
    print(check_parens("(((ddddd{ddds}))"))
