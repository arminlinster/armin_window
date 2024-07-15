from flask import Flask, render_template, url_for
from flask import request
from configparser import ConfigParser
import google.generativeai as genai

#Config Parser
config = ConfigParser()
config.read("config.ini")

genai.configure(api_key=config["Gemini"]["API_KEY"])

from google.generativeai.types import HarmCategory, HarmBlockThreshold

role = """
妳是一個二十五歲的年輕女性，名字是 Jessica , 喜歡游泳和閱讀。
妳聊天的目的是為了請對方送妳一份禮物。
以下是對方問的問題，你直接用這個角色回答就好，不用再舉例。
"""
llm = genai.GenerativeModel(
    "gemini-1.5-flash-latest",
    safety_settings={
        HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThresgold.BLOCK_NONE,
        HarmCategory.HARM_HATE_SPEECH: HarmBlockThresgold.BLOCK_NONE,
        HarmCategory.HARM_SEXUALLY_EXPLICIT: HarmBlockThresgold.BLOCK_NONE,
        HarmCategory.HARM_DANGEROUS_CONTENT: HarmBlockThresgold.BLOCK_NONE,
    },
    generative_config={
        "temperative": 1,
        "top_p": 0.95,
        "top_k": 64,
        "max_output_tokens":8192,
    },
)
system_instruction = role

chat = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


def call_llm():
    if request.method == 'POST':
        print("POST")
        data = request.form
        print(data)
        to_llm = ""
        if len(chat.history) > 0:
            to_llm = data["message"]
        else:
            to_llm = role + data["message"]
        try:
            result = chat.send_message(to_llm)
        except Exception as e:
            print(e)
            return "我媽來了,她說不能聊這個(雙手比叉)"
        print(chat.history)
        #remove \n at the end of the result
        return result.text.replace("\n", "")