import streamlit
from content import generate_script
from content import is_api_key_valid

streamlit.title("🎦 视频脚本一键生成器")

with streamlit.sidebar:
    api_key = streamlit.text_input("请输入OPENAI API密钥", type="password")
    streamlit.markdown("[获取OpenAI API密钥](https://platform.openai.com/account/api-keys)")

topic = streamlit.text_input("💡 请输入视频的主题")

video_length = streamlit.number_input("⌚ 请输入视频的大概时长（单位：分钟）", min_value=0.1, step=0.1)

creativity = streamlit.slider("🧠 请输入视频脚本的创造力（数字小说明更严谨，数字大说明更多样）", min_value=0.0, max_value=1.0, value=0.2, step=0.1)#creativity不要太大，ai语言会混乱

target_audience = streamlit.text_input("😀 请输入视频的主要受众（选填，如学生、科技工作者、演员等等）：")
if not target_audience:
    target_audience = "所有人"

press = streamlit.button("生成脚本")

if press and not api_key:
    streamlit.info("请输入api密钥")
    streamlit.stop()

if press and not topic:
    streamlit.info("请输入视频主题")
    streamlit.stop()

if press and not video_length>=0.1:
    streamlit.info("视频时长应大于等于0.1分钟")
    streamlit.stop()

if press:
    if is_api_key_valid(api_key):
        with streamlit.spinner(("AI正在思考中，请稍后...")):
            search_result, title, script_content = generate_script(topic, video_length, creativity, target_audience, api_key)#这里返回值对应函数部分返回值
        streamlit.success("脚本成功！")
        streamlit.subheader("🔥 标题：")
        streamlit.write(title)
        streamlit.subheader("✍ 视频脚本：")
        streamlit.write(script_content)
        with streamlit.expander("维基百科搜索结果 👀"):
            streamlit.info(search_result)
    else:
        streamlit.error("😡 API密钥不可用！")