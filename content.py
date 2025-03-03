from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_community.utilities import WikipediaAPIWrapper #此处由于网络原因无法访问
import os
import streamlit
import openai

def is_api_key_valid(api_key: str) -> bool:
    """检查 OpenAI API 密钥是否有效。"""
    try:
        openai.api_key = api_key
        # 使用 ChatCompletion 进行一个简单的测试请求来验证 API Key
        openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "system", "content": "ping"}]
        )
        return True
    except openai.AuthenticationError:
        return False
    except Exception as e:
        streamlit.warning(f"验证 API 密钥时出现错误: {str(e)}")
        return False

def generate_script(subject, video_length, creativity, target_audience, api_key):
    title_template = ChatPromptTemplate.from_messages(
        [
            ("human","请为{subject}这个主题的视频想一个吸引人的题目")
        ]
    )

    script_template = ChatPromptTemplate.from_messages(
        [
            ("human",
            """你是一名短视频博主，根据以下标题和相关信息，为短视频写一个视频脚本。
            视频标题：{title},视频时长：{duration}分钟，生成的脚本长度尽量遵循视频时长的要求。
            要求开头抓住眼球，中间提供干活内容，结尾有惊喜，脚本格式也请按照【开头、中间、结尾】分隔。
            视频面向的主要受众是{people}，内容要能够吸引这一类人。
            脚本内容可以结合以下维基百科搜索出的信息，但仅供参考，只需结合相关的，对不相关的进行忽略：
            ```{wikipedia_search}```""")            ]
    )

    model = ChatOpenAI(openai_api_key = api_key, temperature= creativity) #api_key为函数最后一个变量

    title_chain = title_template | model #获得信息传给模型
    script_chain = script_template | model

    title = title_chain.invoke({"subject": subject}).content #后者subject为函数第一个变量值，此句返回ai生成的标题

    try:
        search = WikipediaAPIWrapper(lang="zh")
        search_result = search.run(subject)
    except Exception as e:
        search_result = "（由于网络原因，未能获取到维基百科的相关信息。）"


    script_content = script_chain.invoke({"title":title, "duration":video_length, 
                                             "people":target_audience or "所有人", "wikipedia_search":search_result}).content

    return search_result, title, script_content #返回最终需要的结果

#print(generate_script("Sora模型", 1, 0.7, "年轻人",os.getenv("OPENAI_API_KEY")))