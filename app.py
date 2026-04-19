import streamlit as st
import pandas as pd

# -----------------------------
# 1. CSVファイルを読む
# -----------------------------
# problems.csv を表として読み込む
df = pd.read_csv("math3_lev4_1~15.csv")


# -----------------------------
# 2. type を表示用の日本語に変えるための辞書
# -----------------------------
type_map = {
    "example": "例題",
    "stepup": "StepUp",
    "chapter_end": "章末問題"
}


# -----------------------------
# 3. 理解度を difficulty に変換する関数
# -----------------------------
# アプリで選んだ「理解度」を、
# CSVの difficulty 列と対応させる
def understanding_to_difficulty(understanding):
    if understanding == "低":
        return "practice"
    elif understanding == "中":
        return "standard"
    elif understanding == "高":
        return "advanced"


# -----------------------------
# 4. 画面のタイトル
# -----------------------------
st.title("フォーカスゴールド問題推薦アプリ（レベル4用）")


# -----------------------------
# 5. 入力欄をつくる
# -----------------------------
# 章番号の候補を CSV から取り出す
chapter_list = sorted(df["chapter"].unique())

# 章を選ぶプルダウン
selected_chapter = st.selectbox("第何章？", chapter_list)

# 理解度を選ぶプルダウン
selected_understanding = st.selectbox("理解度を選んでください", ["低", "中", "高"])


# -----------------------------
# 6. ボタンを押したら問題を表示
# -----------------------------
if st.button("問題を表示"):

    # 理解度から difficulty を決める
    selected_difficulty = understanding_to_difficulty(selected_understanding)

    # 条件に合う行だけ取り出す
    result = df[
        (df["chapter"] == selected_chapter) &
        (df["level"] == 4) &
        (df["difficulty"] == selected_difficulty)
    ]

    # データが見つかったかどうかで分岐
    if len(result) > 0:
        # 1行目を取り出す
        row = result.iloc[0]

        # type を日本語に変換
        problem_type = type_map.get(row["type"], row["type"])

        # 表示
        st.success("おすすめ問題はこちらです")
        st.write(f"ページ数: {row['page']}")
        st.write(f"問題番号: {problem_type}{row['problem_no']}")

    else:
        st.error("その条件に合う問題が見つかりませんでした。")

