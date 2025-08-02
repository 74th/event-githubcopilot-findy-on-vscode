from typing import TypedDict
import json

class InputParams(TypedDict):
    """
    入力パラメータ
    """
    year: int
    month: int

def now() -> InputParams:
    """
    現在の年月を取得する。

    Returns:
        InputParams: 現在の年月。
    """
    from datetime import datetime
    now = datetime.now()
    return InputParams(year=now.year, month=now.month)

def load_from_json(json_str: str) -> InputParams:
    """
    JSON文字列から入力パラメータを読み込む。

    Args:
        json_str (str): 入力パラメータを含むJSON文字列。

    Returns:
        InputParams: パースされた入力パラメータ。
    """
    return json.loads(json_str)

if __name__ == "__main__":
    import sys
    import json

    # 標準入力からJSON入力を読み取り
    input_json = sys.stdin.read()

    # JSONからパラメータを読み込み
    params = load_from_json(input_json)

    # 読み込んだパラメータを出力
    print(f"Loaded parameters: {params}")

    # パラメータの使用例
    print(f"Year: {params['year']}, Month: {params['month']}")