import streamlit as st
def main():
    status_area = st.empty()
 #ここから上は編集しない

#タイトル
st.title('新規作成ページ遷移成功')


#CSVファイルをアップロード(とりあえず)
import pandas as pd
uploaded_file = st.file_uploader("CSVファイルを選択してください。(CSVファイルを読み込み表示させられます。今後最適化を実験するときのために使えるかも)", type="csv")
if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    if st.button('CSV表示',use_container_width=True):
        st.write(data)
        #if st.button('学校名の抽出',use_container_width=True):
            
#↓ここから一柳編集
#ログイン機能の実装
import sqlite3
import hashlib
conn = sqlite3.connect('database.db')
c = conn.cursor()
def make_hashes(password):
    return hashlib.sha256(str.encode(password)).hexdigest()
def check_hashes(password,hashed_text):
    if make_hashes(password) == hashed_text:
        return hashed_text
    return False
#ユーザー登録機能（大会名登録機能にしたい）
def create_user():
	c.execute('CREATE TABLE IF NOT EXISTS userstable(username TEXT,password TEXT)')
#ユーザー追加機能
def add_user(username,password):
	c.execute('INSERT INTO userstable(username,password) VALUES (?,?)',(username,password))
	conn.commit()
#ログイン機能
def login_user(username,password):
	c.execute('SELECT * FROM userstable WHERE username =? AND password = ?',(username,password))
	data = c.fetchall()
	return data
new_user = st.text_input('ユーザー名を入力してください')
new_password = st.text_input('パスワードを入力してください',type='password')
if st.button("サインアップ"):
    create_user()
    add_user(new_user,make_hashes(new_password))
    st.success("アカウントの作成に成功しました")
    st.info("ログイン画面からログインしてください")


#ここから下は編集しない
if __name__ == '__main__':
    main()
